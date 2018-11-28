#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<string>
#include<vector>

using namespace std;

int UpdateFirstChange(char* stack){
   int n=strlen(stack);
   if(n==0)return(-1);
   char ch=stack[0];
   for(int i=1;i<n;i++){
      if(stack[i]!=ch){
         for(int j=0;j<i;j++)stack[j]=stack[i];
         return(i);
      }
   }
   return(-1);
}

int main(){
   FILE*inFile, *outFile;
   inFile=fopen("B-large.in", "rt");
   outFile=fopen("B1.out", "wt");

   int t, n;
   char stack[201];
   fscanf(inFile, "%d", &t);

   int minChanges;
   for(int i=0;i<t;i++){
        minChanges=0;
   	fscanf(inFile, "%s", stack);

        while(UpdateFirstChange(stack)!=-1)minChanges++;
        if(stack[0]=='-')minChanges++;
        fprintf(outFile, "Case #%d: %d\n", i+1, minChanges);
   }

   fclose(inFile);
   fclose(outFile);
   return(0);
}
