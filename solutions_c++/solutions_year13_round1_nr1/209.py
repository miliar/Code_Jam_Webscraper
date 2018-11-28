#include<cstdio>
#include<iostream>
#include<fstream>
#include<cmath>
#include<gmpxx.h>
using namespace std;
int m,l0,layer;
mpz_class r,t,a,b,c,k;
int main()
{
  freopen("alarge.in","r",stdin);
  freopen("a2.out","w",stdout);
  cin>>m;
  for(l0=1;l0<=m;l0++)
  {
    cin>>r>>t;
    a=2;
    b=2*r-1;
    c=-t;
    k=(-b+sqrt(b*b-4*a*c))/2/a;
    printf("Case #%d: ",l0);
    cout<<k<<endl;
  }
  return 0;
}
