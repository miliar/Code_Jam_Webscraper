#include<iostream>
#include<cstdio>

using namespace std;

double fun(double r, double c, double x, double f){
  int num=(r-2)/f;
  if(num>(x/c))return 100000.0;
  return min((x/r), (c/r)+fun(r+f,c,x,f));
}

int main(){
  int T,t=0;
  cin>>T;
  while(t<T){
    double c,x,f;
    cin>>c>>f>>x;
    double sum=fun(2,c,x,f);
    printf("Case #%d: %0.7f\n",t+1,sum);
    t++;
  }
  return 0;
}
