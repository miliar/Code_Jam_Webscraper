#include<iostream>
#include <cstdio>
using namespace std;

int main(){
    int t,CASE;
    double Sec,C,F,X,TF,NTF,NSec,CpS=2,cookie,time=0;
    cin>>t;
    double arr[t];
    for(CASE = 1;CASE<=t;CASE++){
        cin>>C;
        cin>>F;
        cin>>X;
        CpS = 2;
        time = 0;
        while(1){
                 TF=C/CpS;
                 NTF=X/(CpS+F);
                 NSec=TF+NTF;
                 Sec=X/CpS;
                 if(Sec>NSec){
                       CpS+=F;
                       time+=TF;
                 }else{
                       time+=Sec;
                       break;
                 }
        }
        printf("Case #%d: %.7f\n",CASE,time);
    }
} 
