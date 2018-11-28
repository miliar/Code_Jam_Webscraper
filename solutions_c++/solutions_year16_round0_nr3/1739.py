#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<string>
#include<vector>
#include<cmath>

using namespace std;

typedef unsigned long long myint;

myint GetPrimeFactor(myint num){
   for(myint i=2;i<sqrt(num)+1;i++)if(num%i==0)return(i);
   return(-1);
}

string GetNextNumber(string preNum){
   int indx=-1;
   string retVal(preNum);
   //for(int i=0;i<preNum.size();i++)if(preNum[i]=='0'){indx=i;break;}  
   for(int i=preNum.size()-1;i>=0;i--)if(preNum[i]=='0'){indx=i;break;}  
   if(indx==-1)return("0");
   //for(int i=0;i<indx;i++)retVal[i]='0';
   for(int i=preNum.size()-1;i>indx;i--)retVal[i]='0';
   retVal[indx]='1';
   return(retVal);
}

vector<string> GetProofList(int N, int J, vector<vector<myint> >& jProof){
   vector<string> jList(J);
   string num(N-2, '0'), pJNumStr;

   myint pJNum, cnt=0, pFact;
   bool found;
   while(cnt<J){
      found=true;
      pJNumStr='1' + num + '1';
      for(int k=2;k<11;k++){
        pJNum=stoll(pJNumStr, NULL, k);
        pFact=GetPrimeFactor(pJNum);
        if(pFact!=-1)jProof[cnt][k-2]=pFact;
        else{jProof[cnt].clear();found=false;break;}
      }
      if(found)jList[cnt++]=pJNumStr;
      num=GetNextNumber(num);
   }
   return(jList);
}
 
int main(){
   FILE*inFile, *outFile;
   //inFile=fopen("D-small-attempt2.in", "rt");
   inFile=fopen("C-test.in", "rt");
   outFile=fopen("C2.out", "wt");

   int t, N, J;
   fscanf(inFile, "%d", &t);

   for(int i=0;i<t;i++){
   	fscanf(inFile, "%d %d", &N, &J);
        vector<string> jList(J);
        vector<vector<myint> >jProof(J, vector<myint>(9));
        
        jList=GetProofList(N, J, jProof);

        fprintf(outFile, "Case #%d:\n", i+1);
	for(int k=0;k<jList.size();k++){
	   fprintf(outFile, "%s", (jList[k]+jList[k]).c_str());
           for(int l=0;l<9;l++)fprintf(outFile, " %lld", jProof[k][l]);
           fprintf(outFile, "\n");
        }
   }

   fclose(inFile);
   fclose(outFile);
   return(0);
}
