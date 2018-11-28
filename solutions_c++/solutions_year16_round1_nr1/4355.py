#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<string>
#include<vector>

using namespace std;

int GetMax(char* str){
   int retVal=0;
   for(int i=1;i<strlen(str);i++)if(str[i]>str[retVal])retVal=i;
   return(retVal);
}


int main(){
   FILE*inFile, *outFile;
   //inFile=fopen("A-small-attempt2.in", "rt");
   inFile=fopen("A-large.in", "rt");
   outFile=fopen("A1.out", "wt");

   int t, indx, lIndx=0, rIndx=0;
   char str[1001], left[1001], right[1001], lastWord[1001], lastR;
   int appeared;
   fscanf(inFile, "%d", &t);
    
   for(int i=0;i<t;i++){
   	fscanf(inFile, "%s", str);

        rIndx=0;
        lIndx=0;
        appeared=0;
        lastR=str[0];

        indx=GetMax(str);
        //right[rIndx++]=str[0];
        //for(int j=strlen(str)-1;j>=0;j--){
        for(int j=0;j<strlen(str);j++){
            if( (appeared==1 && str[j]==str[indx]) || (appeared==0 && str[j]>=lastR)){
              if(str[j]==str[indx])appeared=1;
              else lastR=str[j];
              left[lIndx++]=str[j];
            }
            else{
	       right[rIndx++]=str[j];
            }
        }

        //left[lIndx]='\0';
        //right[rIndx]='\0';
        //printf("\nleft: %s , \t right: %s\n", left, right);
        //break;

        //for(int j=0;j<lIndx;j++)lastWord[j]=left[j];
        for(int j=lIndx-1;j>=0;j--)lastWord[lIndx-1-j]=left[j];
        for(int j=lIndx;j<rIndx+lIndx;j++)lastWord[j]=right[j-lIndx];
        //for(int j=rIndx-1;j>=0;j--)lastWord[lIndx+rIndx-1-j]=right[j];
        lastWord[rIndx+lIndx]='\0';
       
        fprintf(outFile, "Case #%d: %s\n", i+1, lastWord);
   }

   fclose(inFile);
   fclose(outFile);
   return(0);
}
