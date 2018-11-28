#include <iostream>
#include <stdio.h>
using namespace std;
long long b[41]={1};
long long gcd(long long m,long long n)
{
  if (n==0) return m;
  return gcd(n,m%n);
}
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);
  int t,k,i,j,f;
  long long p,q,g;
  for (i=1;i<=40;i++) b[i]=b[i-1]*2;
  cin>>t;
  for (k=1;k<=t;k++)
  {
    scanf("%lld/%lld",&p,&q);
    g=gcd(p,q);
    p/=g;q/=g;f=0;
    for (i=0;i<=40;i++)
      if (q<b[i]) break;
      else if (q==b[i]) {f=1;break;}
    cout<<"Case #"<<k<<": ";
    if (f)
    {
      j=0;
      while (p>0) {p/=2;j++;}
      cout<<i-j+1<<endl;
    }
    else cout<<"impossible"<<endl;
  }
  return 0;
}
