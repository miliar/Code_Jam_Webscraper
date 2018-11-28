#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<string>
#include<vector>

using namespace std;
bool SeeDigits(long long n, vector<char>& digs){
    int dNum;
    while(n){
      dNum=n%10;
      n/=10;
      digs[dNum]=1;
    }
    for(int i=0;i<10;i++)if(digs[i]==0)return(false);
    return(true);
}


long long GiveLastNumber(int n){
    if(n==0)return(-1);
    vector<char>digits(10, 0);
    int counter=1;
    long long m;
    while(1){
       m=n*counter++;
       if(SeeDigits(m, digits))return(m);
       if(counter>2000){printf("probably %d does not cover all the digits", n);exit(1);}   
    }
}



int main(){
   FILE*inFile, *outFile;
   inFile=fopen("A-large.in", "rt");
   outFile=fopen("A1.out", "wt");

   int t, n;
   long long lastNum;
   fscanf(inFile, "%d", &t);
   for(int i=0;i<t;i++){
   	fscanf(inFile, "%d", &n);
        lastNum=GiveLastNumber(n);
        if(lastNum>0)fprintf(outFile, "Case #%d: %lld\n", i+1, lastNum);
        else fprintf(outFile, "Case #%d: INSOMNIA\n", i+1);
   }

   fclose(inFile);
   fclose(outFile);
   return(0);
}
