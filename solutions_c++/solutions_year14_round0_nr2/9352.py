#include <bits/stdc++.h>

#define eps 0.0000001

using namespace std;

int main()
{
  int t;
  cin>>t;
  for(int k=1;k<=t;++k){
    double c,f,x;
    cin>>c>>f>>x;
    double curr=0,extra=0,capa=2,cookie=0;
    while(x-cookie>eps){
      extra=curr+c/capa+x/(capa+f);//等下一次买=当前时间+攒夠时间+期望
      curr=curr+x/capa;//不买，时间等于现在时间+期望
      cookie=x+eps;
      if(curr-extra>eps){
        curr=curr-x/capa+c/capa;
        cookie=0;
        capa+=f;
      }
    }
    cout.setf(ios::fixed);
    cout<<"Case #"<<k<<": "<<setprecision(7)<<curr<<endl;
  }
  return 0;
}
