#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXBUF 8192
#define MAXITEMS 2100
#define MAXS        1000
#define MAXCUST     100

// int malts[MAXFLAVORS][MAXCUST];
// int shakes[MAXFLAVORS][MAXCUST];

struct array { long long item[MAXITEMS]; };

void ProcessCase(int caseNum, int credit, int numItems, int* ItemCosts);
void ReverseWords(int caseNum, char* text);
void ConvertToT9(int caseNum, char* text);
void ScalarProduct(int caseNum, int ValA, array ValXs, array ValYs);

FILE* fout;

int GetInteger(char * buf, FILE* fin)
{
  fgets(buf,MAXBUF,fin);
//   printf("%s\n",buf);
  return atoi(buf);
}
char* GetNextInteger(char* buf, long long& num)
{
  long i;
  bool neg = false;
  num=0;
  for (i=0; i<MAXBUF; i++)
  {
    if ((buf[i]>='0') && (buf[i]<='9'))
    {
      num *= 10LL;
      num += (long long)(buf[i]-'0');
    }
    else if (buf[i] == '-')
    {
      neg = true;
    }
    else if ((buf[i] == '\r')||(buf[i] == '\n'))
    {
      i++;
      break;
    }
    else
    {
      i++;
      break;
    }
  }
  if (neg)
    num = 0LL-num;
  return &buf[i];
}
void GetArray(char* buf, FILE* fin,int size, array& vector)
{
  int i, j, k;
  bool neg = false;
  int first = 0;
  long long num;
  char* cp = buf;

  fgets(buf,(int)MAXBUF,fin);
  if (size == 0)
  {
    first = 1;
    cp = GetNextInteger(cp,num);
    vector.item[0] = num;
  }
  for (j=0; j<=(vector.item[0]); j++)
  {
//    for (k=0; k<2; k++)
    {
//       cp = GetNextInteger(cp,num);
      vector.item[j+1]= cp[j] - '0';
    }
  }
}

int main(int Argc, char **Argv)
{
  FILE* fin;
  char buf[MAXBUF];
  int linelen, numTests,i,j,k;
  int ValA, ValB, numItems;
  array ValXs;
  array ValYs;

//   printf("%s\n",Argv[1]);
  printf("size of =%d\n",sizeof(long long));
  fin = fopen(Argv[1],"r");
  fout = fopen("CodeJam.txt","w");
  if (fin != NULL)
  {
    numTests = GetInteger(buf, fin);
//     printf("%d Cases\n",numTests);
    for (i=0; i<numTests; i++)
    {
//       ValA = GetInteger(buf,fin);
//       printf("Flavors = %d\n",ValA);
//       ValB = GetInteger(buf, fin);
//       printf("Customers = %d\n",ValB);
//       for (j=0; j<ValB; j++)
//       {
        GetArray(&buf[0],fin,0,ValXs);
//        printf("Smax %d",ValXs.item[0]);
//         for (k=1; k<(1+(ValXs.item[0]*2)); k+=2)
//         {
//           int flav = ValXs.item[k];
//           int opt  = ValXs.item[k+1];
//           if (opt)
//           {
//             malts[0][0]++;  // treat as # customers
//             malts[flav][0]++;
//           }
//           else
//           {
//             shakes[0][0]++;
//             shakes[flav][0]++;
//           }
//         }
//         for(k=0;k<ValXs.item[0];k++)
//         {
//           printf("%d ",ValXs.item[k+1]);
//         }
//         printf("\n");
//       }
//      GetArraywoCt(&buf[0],fin,ValA,ValYs);
//       fgets(buf,MAXBUF,fin);
//       ValA = atoi(buf);
//        printf("\n\nCase #%02d: ValA = %d \n",i+1,ValA);
//       fgets(buf,MAXBUF,fin);
//       numItems = atoi(buf);
//        printf(" # items = %d\n",numItems);
//        printf("        : ValBs\n");
//       fgets(buf,MAXBUF,fin);
//       for (j=0,k=0; j<numItems; j++)
//       {
//         ValBs[j]=0;
//         for ( ; k<MAXBUF; k++)
//         {
//           if ((buf[k]>='0') && (buf[k]<='9'))
//           {
//             ValBs[j] *= 10;
//             ValBs[j] += buf[k]-'0';
//           }
//           else if ((buf[k] == '\r')||(buf[k] == '\n'))
//           {
//             k++;
//             break;
//           }
//           else
//           {
//             k++;
// 
//             break;
//           }
//         }
//       }
//        for (j=0; j<ValA; j++)
//          printf("%d ",ValXs.item[j]);
//        printf("\n");
//        for (j=0; j<ValA; j++)
//          printf("%d ",ValYs.item[j]);
//        printf("\n");
//       ProcessCase(i+1,ValA,numItems,&ValBs[0]);
//      ConvertToT9(i+1, buf);
//       ScalarProduct(i+1,ValA,ValXs,ValYs);
      int standing = 0;
      int required;
      int Maxs = ValXs.item[0];
      for (j=1,k=0,required=0; required<=Maxs; j++, required++)
      {
        if (standing < required)
        {
          k++;
          standing++;
        }
        standing += ValXs.item[j];
      }
      fprintf(fout,"Case #%d: %d\n",i+1,k);
    }
  }
  if (fin != NULL)
  {
    fclose(fin);
    fclose(fout);
  }
}

char* AscToT9[] = {
  "0",  // space
  "2", "22", "222", "3", "33", "333", // A B C D E F
  "4", "44", "444", "5", "55", "555", // G H I J K L
  "6", "66", "666", "7", "77", "777", "7777", // M N O P Q R S
  "8", "88", "888", "9", "99", "999", "9999", // T U V W X Y Z
};

int minArray(const void* itemA, const void* itemB)
{
  void* pi1 = const_cast<void*>(itemA);
  void* pi2 = const_cast<void*>(itemB);
  long long* pa1 = static_cast<long long*>(pi1);
  long long* pa2 = static_cast<long long*>(pi2);


  return (*pa1 - *pa2);
}

int maxArray(const void* itemA, const void* itemB)
{
  void* pi1 = const_cast<void*>(itemA);
  void* pi2 = const_cast<void*>(itemB);
  int* pa1 = static_cast<int*>(pi1);
  int* pa2 = static_cast<int*>(pi2);

  return (*pa2 - *pa1);
}

void ScalarProduct(int caseNum, int ValA, array ValXs, array ValYs)
{
  int j;
  long long sum = 0;
  long long oldsum = 0;
  fprintf(fout,"Case #%d: ",caseNum);
  qsort(ValXs.item,ValA,sizeof(long),minArray);
  qsort(ValYs.item,ValA,sizeof(long),minArray);
  for (int i=0; i<ValA; i++)
  {
    sum += ValXs.item[i]*ValYs.item[(ValA-1)-i];
//     printf("%d = %d * %d\n",sum,ValXs.item[i],ValYs.item[(ValA-1)-i]);
  }
//   for (j=0; j<ValA; j++)
//     printf("%d ",ValXs.item[j]);
//   printf("\n");
//   for (j=0; j<ValA; j++)
//     printf("%d ",ValYs.item[j]);
  fprintf(fout,"%lld\n",sum);
//   printf("\n");
}

void ConvertToT9(int caseNum, char* text)
{
  char c;
  int i, j=0, k;
  int len = (int)strlen(text);

  fprintf(fout,"Case #%d: ",caseNum);
  for (i=0; i<len; i++)
  {
    if ((text[i] == '\n') || (text[i] == '\r'))
      continue;
    c = (text[i] & 0x1f);
    if (AscToT9[c][0] == j)
    {
      fprintf(fout," ");
    }
    fprintf(fout,"%s",AscToT9[c]);
    j = AscToT9[c][0];
  }
  fprintf(fout,"\n");
}
void ReverseWords(int caseNum, char* text)
{
  int i, j, k;
  int len = (int)strlen(text);
  char* Words[5000];
  fprintf(fout,"Case #%d: ",caseNum);
  Words[0] = text;
  for (i=0,j=1; i<len; i++)
  {
    if ((text[i] == ' ') || text[i] == '\n')
    {
      text[i] = 0;
      Words[j++] = &text[i+1];
    }
  }
  for (i=(j-1); i>=0; i--)
  {
    fprintf(fout,"%s",Words[i]);
    if (i)
      fprintf(fout," ");
  }
  fprintf(fout,"\n");
}
void ProcessCase(int caseNum, int credit, int numItems, int* ItemCosts)
{
  int i, j, k;

  fprintf(fout,"Case #%d: ",caseNum);
  for (i=0; i<numItems; i++)
  {
    if (ItemCosts[i]>credit)
      continue;
    for (j=i+1; j<numItems; j++)
    {
      if ((ItemCosts[i] + ItemCosts[j]) == credit)
      {
        fprintf(fout,"%d %d\n",i+1,j+1);
      }
    }
  }
}