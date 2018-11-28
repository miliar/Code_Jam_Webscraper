#include<stdio.h>
#include<iostream>

using namespace std;

int main(){
  int T,t,i,k;
  float C,F,X,N;
  float time,time2,c1=0,c2=0;
  cin>>T;
  for(t=0;t<T;t++){
    cin>>C>>F>>X;
    k = (int) (X/C -2/F);
    if(k < 0) k=0;
    for(i=0;i<k;i++)
      time += C/(2+i*F);
    time += X/(2+(k*F));
    printf("Case #%d: %.7lf\n", t, time);
  }
}

        
