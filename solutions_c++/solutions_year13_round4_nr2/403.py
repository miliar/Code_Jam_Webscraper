#include<iostream>
#include<cstdio>
#include<string.h>
#include<algorithm>
#include<map>
#include<math.h>
#include<vector>
using namespace std;
int N;
long long p,n;
long long l,r,mid,x,ma,mi,ans1,ans2;
int i,j,k;
int cas,tst;
long long pd1(long long x)
{
     long long ret=0,tt=n;
     mi=x;
     ma=n-x-1;
     while (tt>1)
     {
           if (mi>0)
           {
              mi--;
              ret+=(tt>>1);
              if (mi%2==0)
              {
                 mi>>=1;
                 ma>>=1;
              }
              else
              {
                 mi>>=1;
                 ma>>=1;
                 ma++;
              }
           }
           else
           {
              ma--;
              ma>>=1;
           }
           tt>>=1;
     }
     return ret+1;
}
long long pd2(long long x)
{
     long long ret=0,tt=n;
     mi=x;
     ma=n-x-1;
     while (tt>1)
     {
           if (ma>0)
           {
              ma--;
              if (ma%2==0)
              {
                 ma>>=1;
                 mi>>=1;
              }
              else
              {
                 ma>>=1;
                 mi>>=1;
                 mi++;
              }
           }
           else
           {
               ret+=(tt>>1);
               mi--;
               mi>>=1;
           }
           tt>>=1;
     }
     return ret+1;
}
int main()
{
    cin>>tst;
    for (cas=1;cas<=tst;cas++)
    {
        cin>>N>>p;
        n=1;
        for (i=0;i<N;i++) n*=2;
        l=0;r=n;
        while (l+1<r)
        {
              mid=(l+r)>>1;
              if (pd1(mid)<=p) l=mid;
                 else r=mid;
        }
        ans1=l;
        l=0;r=n;
        while (l+1<r)
        {
              mid=(l+r)>>1;
              if (pd2(mid)<=p) l=mid;
                 else r=mid;
        }
        ans2=l;
        cout<<"Case #"<<cas<<": "<<ans1<<" "<<ans2<<endl;
    }
    return 0;
}
