#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
using namespace std;

int main(){
ifstream in("B-large.in");
FILE* f=fopen("outL.txt","w");
//read in number of test cases
int tc=0;
in>>tc;
for(int i=1;i<=tc;i++){
    double C=0;
    in>>C;
    double F=0;
    in>>F;
    double X=0;
    in>>X;
    
    double r=2;//cooky rate
    double t2s=0;//
    double tt2s=0;
    double t2ba=0;
    double ptt2ba=X;
    double tt2ba=X/2;
    while(ptt2ba>tt2ba){//difference should be greater than 10-6
    //while((ptt2ba-tt2ba)>0.000001){
        ptt2ba=tt2ba;
        t2s=C/r;
        tt2s+=t2s;
        r +=F;
        t2ba=X/r;
        tt2ba=tt2s+t2ba;
        
        
    }
fprintf(f,"Case #%d: %.7f\n",i,ptt2ba);
}
in.close();
}