#include<iostream>
#include<stdio.h>
using namespace std;
int N;
double X,V;
double C[101];
double R[101];
double solv(){
  if(N==1){
    if(C[0]==X)return V/R[0];
    else return -1;
  }else{
    if((C[0]<X&&C[1]<X)||(C[0]>X &&C[1]>X))return -1;
    if(C[0]==C[1])return V/(R[0]+R[1]);
  double s0,s1;
  s0 = (C[1]-X)*V/((C[1]-C[0])*R[0]);
  s1 = (C[0]-X)*V/((C[0]-C[1])*R[1]);
  return max(s0,s1);
  }
}
int main(void){
  int T;
  cin>>T;
  for(int testcase = 1; testcase<=T;testcase++){
    cin>>N;
    cin>>V>>X;
    for(int i = 0; i<N;i++){
      cin>>R[i]>>C[i];
    }
    double ans = solv();
    if(ans < 0 ){
      printf("Case #%d: IMPOSSIBLE\n", testcase );
    }else{
      printf("Case #%d: %lf\n", testcase, ans );
    }
  }
  return 0;
}


  
