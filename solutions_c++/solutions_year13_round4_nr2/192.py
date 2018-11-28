#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <vector>
#include <cstring>
#include <cmath>
#include <iostream>
using namespace std;

long long N,P;
bool pd1(long long x)
{
    long long n=N;
    long long ans=0;
    while (x>1)
    {
        x=(x-2)/2+1;
        n--;
        ans=ans*2+1;
    }
    while (n>0)
    {
        n--;
        ans*=2;
    }
    ans++;
    if (ans<=P) return true;
    else return false;
}

bool pd2(long long x)
{
    long long n=N;
    long long ans=0;
   // cout<<x<<' ';
    x=(1ll<<N)-x+1;
    while (x>1)
    {
        x=(x-2)/2+1;
        n--;
        ans=ans*2+1;
    }
    while (n>0)
    {
        n--;
        ans*=2;
    }
    ans++;
    if (ans>=(1ll<<N)-P+1) return true;
    else return false;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    int cas=1;
    scanf("%d",&T);
    while (T--)
    {
        scanf("%lld%lld",&N,&P);
        long long l,r;
        l=1;r=(1ll<<N);
        while (l<r)
        {
            long long mid=(l+r+1)/2;
            if (pd1(mid)) l=mid;
            else r=mid-1;
        }
        long long ans1=l;
        l=1;r=(1ll<<N);
        while (l<r)
        {
            long long mid=(l+r+1)/2;
            if (pd2(mid)) l=mid;
            else r=mid-1;
        }
       // cout<<pd2(8);
        long long ans2=l;
        printf("Case #%d: %lld %lld\n",cas++,ans1-1,ans2-1);
    }
}
