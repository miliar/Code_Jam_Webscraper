#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<string>
#include<cstring>
#include<vector>

using namespace std;

int SearchStr(char* input, char c){
  for(int i=0;i<strlen(input);i++){
    if(input[i]==c){
      for(int k=i+1;k<=strlen(input);k++)input[k-1]=input[k];
      return(1);
    }
  }
  return(-1);
}

int HasDigit(char* input, int digit){
   switch(digit){
     case 0:
      if(SearchStr(input, 'Z')==-1)return(-1);
      SearchStr(input, 'E');
      SearchStr(input, 'R');
      SearchStr(input, 'O');
      break;
     case 1:
      if(SearchStr(input, 'O')==-1)return(-1);
      SearchStr(input, 'E');
      SearchStr(input, 'N');
      break;
     case 2:
      if(SearchStr(input, 'W')==-1)return(-1);
      SearchStr(input, 'T');
      SearchStr(input, 'O');
      break;
     case 3:
      if(SearchStr(input, 'H')==-1)return(-1);
      SearchStr(input, 'T');
      SearchStr(input, 'R');
      SearchStr(input, 'E');
      SearchStr(input, 'E');
      break;
     case 4:
      if(SearchStr(input, 'U')==-1)return(-1);
      SearchStr(input, 'F');
      SearchStr(input, 'O');
      SearchStr(input, 'R');
      break;
     case 5:
      if(SearchStr(input, 'F')==-1)return(-1);
      SearchStr(input, 'I');
      SearchStr(input, 'V');
      SearchStr(input, 'E');
      break;
     case 6:
      if(SearchStr(input, 'X')==-1)return(-1);
      SearchStr(input, 'S');
      SearchStr(input, 'I');
      break;
     case 7:
      if(SearchStr(input, 'S')==-1)return(-1);
      SearchStr(input, 'E');
      SearchStr(input, 'V');
      SearchStr(input, 'E');
      SearchStr(input, 'N');
      break;
     case 8:
      if(SearchStr(input, 'G')==-1)return(-1);
      SearchStr(input, 'E');
      SearchStr(input, 'I');
      SearchStr(input, 'H');
      SearchStr(input, 'T');
      break;
     case 9:
      if(SearchStr(input, 'I')==-1)return(-1);
      SearchStr(input, 'N');
      SearchStr(input, 'N');
      SearchStr(input, 'E');
      break;

   }
   return(1);
}

int main(){
   FILE*inFile, *outFile;
   inFile=fopen("A-large.in", "rt");
   //inFile=fopen("A-large.in", "rt");
   outFile=fopen("A1.out", "wt");

   int t, digitCounter[10], order[10]={0, 2, 4, 6, 8, 3, 5, 7, 1, 9};
   char input[2001];

   fscanf(inFile, "%d", &t);
   for(int i=0;i<t;i++){
       fscanf(inFile, "%s", input);
       for(int j=0;j<10;j++)digitCounter[j]=0;
       for(int j=0;j<10;j++){
         int c;
         while(HasDigit(input, order[j])!=-1)digitCounter[order[j]]++; 
       }         
       fprintf(outFile, "Case #%d: ", i+1);
       for(int j=0;j<10;j++)for(int k=0;k<digitCounter[j];k++)fprintf(outFile, "%c", '0'+j);
       if(i<t-1)fprintf(outFile, "\n");
   }

   fclose(inFile);
   fclose(outFile);
   return(0);
}
