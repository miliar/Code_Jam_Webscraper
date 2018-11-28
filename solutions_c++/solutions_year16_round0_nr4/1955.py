#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<string>
#include<vector>
#include<cmath>

using namespace std;

vector<unsigned long long> GetList(int K, int C){
   vector<unsigned long long> sList;
   if(K==1){sList.push_back(1);return(sList);}
   if(C==1){
     for(int i=0;i<K;i++)sList.push_back(i+1);
     return(sList);
   }
   unsigned long long indx=2, step, K_C;
   step=pow(K, C-1);
   K_C=pow(K, C);

   bool addOdd=false;
   if(K%2==1){K--;addOdd=true;}
   for(int i=2;i<=K;i+=2){
     indx=step*(i-2)+i;
     sList.push_back(indx);
   }
   if(addOdd){
      K++;
      indx=step*(K-2)+K;
      sList.push_back(indx);
   }
   return(sList);
}

int main(){
   FILE*inFile, *outFile;
   inFile=fopen("D-small-attempt2.in", "rt");
   //inFile=fopen("D-test.in", "rt");
   outFile=fopen("D1.out", "wt");

   int t, n;
   char stack[201];
   fscanf(inFile, "%d", &t);

   int K, C, S;
   vector<unsigned long long> sList;
   for(int i=0;i<t;i++){
        sList.clear();
   	fscanf(inFile, "%d %d %d", &K, &C, &S);
        sList=GetList(K, C);
        if(sList.size()>S){
           if(i>0)fprintf(outFile,"\n");
           fprintf(outFile, "Case #%d: IMPOSSIBLE", i+1);
        }
        else{
           if(i>0)fprintf(outFile,"\n");
           fprintf(outFile, "Case #%d:", i+1);
	   for(int j=0;j<sList.size();j++)fprintf(outFile, " %lld", sList[j]);
        }
   }

   fclose(inFile);
   fclose(outFile);
   return(0);
}
