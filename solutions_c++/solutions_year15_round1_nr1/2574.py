#include<stdio.h>
#define rep(i,n) for(i=0;i<n;i++)
#define each(i,x,n) for(i=x;i<n;i++)
#define repb(i,n) for(i=n;i>0;i++)
#define eachb(i,x,n) for(i=n;i>x;i++)
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
ll t,res[100000][2],m[100000];
void output()
{ll i;
 rep(i,t)
{
 printf("Case #%lld: %lld %lld\n",i+1,res[i][0],res[i][1]);
}
}
ll max(ll a[],ll n)
{ll i,ma=0;
 rep(i,n)
 {
  if(a[i]>ma)
  ma=a[i];
}
return ma;
}
int main()
{
 ll i,j,n,sum,sum2,maxi;
 scanf("%lld",&t);
 rep(i,t)
{ll g[100000];
scanf("%lld",&n);
sum=0;
sum2=0;
maxi=0;
rep(j,n)
scanf("%lld",&m[j]);


rep(j,n-1)
{
 if(m[j]>m[j+1])
 {sum+=m[j]-m[j+1];
  g[j]=m[j]-m[j+1]; 
 }
else
g[j]=0;
}
maxi=max(g,n-1);
rep(j,n-1)
{if(m[j]<=maxi)
sum2+=m[j];
else
sum2+=maxi;
}
if(n==2)
{sum=m[0]-m[1];
sum2=m[0]-m[1];
}
res[i][0]=sum;
res[i][1]=sum2;

}
output();
}
