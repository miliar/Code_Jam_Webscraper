#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define ll long long

ll cs,c,a,b;

bool palindrome(ll n)
{
  int i,z;
  char str[1001];

  sprintf(str,"%lld",n);
  for(i=0,z=strlen(str);i<z && str[i]==str[z-1-i];i++);
  return i==z;
}
ll f(ll n)
{
  ll s=0,i;

  for(i=1;i*i<=n;i++)
    if(palindrome(i) && palindrome(i*i))
      s++;
  return s;
}
int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%lld%lld",&a,&b);
    printf("Case #%lld: %lld\n",c,f(b)-f(a-1));
  }
  return 0;
}
