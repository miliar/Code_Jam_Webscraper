#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int cas=1;
long long a1024=1024;
long long all=a1024*a1024*a1024*a1024;
long long a,b;
long long gcd(long long a,long long b)
{
     if(b%a==0)
       return a;
     return gcd(b%a,a);
}
int f(long long x)
{
    long long tmp=all;
    int ans=0;
    while(x<tmp)
      tmp/=2,ans+=1;
    return ans;
}
int main()
{
    freopen("x.in","r",stdin);
    freopen("x.out","w",stdout);
    int t;
    cin>>t;
    while(t--)
    {
      scanf("%lld/%lld",&a,&b);
      if(a>b)
         printf("Case #%d: impossible\n",cas++);
      else
      {
         long long c=gcd(a,b);
         a/=c,b/=c;
         if(all%b!=0)
               printf("Case #%d: impossible\n",cas++);
         else 
         {
            a=all/b*a;
            printf("Case #%d: %lld\n",cas++,f(a));
         }
      }
    }
    return 0;
}
                      
