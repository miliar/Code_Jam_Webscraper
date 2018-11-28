#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<stdlib.h>
#include<algorithm>
#include<limits.h>
using namespace std;
long long int minim(long long int m,long long int n)
{
     if(m<n)
     return m;
     else
     return n;
}
long long int a[200000];
int main()
{
    freopen("A-large (1).in","r",stdin); freopen("gcjalarge.txt","w",stdout);
    long long int T,t,ans1,ans2,i,maxi,n;
    scanf("%lld",&T);
    for(t=1;t<=T;t++)
    {
              scanf("%lld",&n);
              for(i=1;i<=n;i++)
              {
                               scanf("%lld",&a[i]);
              }
              ans1=0;
              for(i=2;i<=n;i++)
              {
                               if(a[i]<a[i-1])
                               {
                                              ans1=ans1+a[i-1]-a[i];
                               }
              }
              maxi=0;
              for(i=1;i<n;i++)
              {
                               if(a[i]>=a[i+1])
                               {
                                              if(a[i]-a[i+1]>maxi)
                                              {
                                                                  maxi=a[i]-a[i+1];
                                              }
                               }
              }
              ans2=0;
              for(i=1;i<n;i++)
              {
                              ans2=ans2+minim(maxi,a[i]);
              }
              printf("Case #%lld: %lld %lld\n",t,ans1,ans2);
    }    
    return 0;
}
