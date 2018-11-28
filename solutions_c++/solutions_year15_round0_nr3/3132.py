#include <stdio.h>

static char mult_table[8][8] = 
{
   {'a','b','i','j','k','l','m','n'},
   {'b','a','l','m','n','i','j','k'},
   {'i','l','b','k','m','a','n','j'},
   {'j','m','n','b','i','k','a','l'},
   {'k','n','j','l','b','m','i','a'},
   {'l','i','a','n','j','b','k','m'},
   {'m','j','k','a','l','n','b','i'},
   {'n','k','m','i','a','j','l','b'}
};

int conv(const char p)
{
   switch(p)
   {
   case 'a':/*1*/
      return 0;
   case 'b':/*-1*/
      return 1;
   case 'i':
      return 2;
   case 'j':
      return 3;
   case 'k':
      return 4;
   case 'l':
      return 5;
   case 'm':
      return 6;
   case 'n':
      return 7;
   }
   return 0;
}

char mul(const char p1,const char p2)
{
   int x = conv(p1);
   int y = conv(p2);
   return mult_table[x][y];
}

char* check(char* p,char& prod,int& flag,char check)
{
   while(*p != '\0')
   {
      prod = mul(prod,p[0]);
      p++;
      if(prod == check )
      {
         flag = 1;
         return p;
      }
   }
   flag = 0;
   return p;
}

int main()
{
   int i, nProblem;
   FILE* input = fopen("C-small-attempt0.in","r");
   FILE* output = fopen("output.txt","w");

   fscanf(input,"%d\n",&nProblem);
   if(!nProblem)
      return 0;
   
   for(i = 0; i < nProblem; i++)
   {
      int j,subLen;
      int nRepeat;
      int bI=0, bJ=0, bK=0;
      char* substr;
      char residue = 'a';
      char prodI = 'a', prodJ = 'a', prodK = 'a';

      fscanf(input,"%d %d\n",&subLen,&nRepeat);
      substr = new char [subLen+1];
      fscanf(input,"%s\n",substr);

      for(j = 0; j < nRepeat;j++)
      {
         char *p = substr;

         if(!bI)
            p = check(p,prodI,bI,'i');
         if(!bJ)
            p = check(p,prodJ,bJ,'j');
         if(!bK)
            p = check(p,prodK,bK,'k');
         
         while(*p != '\0')
         {
            residue = mul(residue,p[0]);
            p++;
         }
      }

      if((residue =='a') && (bI && bJ && bK))
         fprintf(output,"Case #%d: YES\n",i+1);
      else
         fprintf(output,"Case #%d: No\n",i+1);

      delete []substr;
   }
}