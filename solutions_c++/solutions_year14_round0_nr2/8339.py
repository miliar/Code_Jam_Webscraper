#include<iostream>
#include<cstdio>
using namespace std;

int main(){
  int tc;
  cin>>tc;
  for(int i=1;i<=tc;i++){
    double c,f,x;
    double r=2.0;
    double t =0;
    scanf("%lf%lf%lf",&c,&f,&x);
    while(x/r-(c/r+x/(r+f))>0){
      t=t+c/r;
      r=r+f;
    }
    t=t+x/r;
    //cout<<"Case "<<"#"<<i<<": " <<t<<endl;
    printf("Case #%d: %lf\n",i,t);
  }
}
