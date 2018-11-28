#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int N;
long long P;
bool judge(long long k)
{
    long long s=0,res;
    res=(1LL<<N)-k;
    for(int i=N-1;i>=0;i--)
    {
        if(res>1)
        {
            res/=2;
        }
        else s+=(1LL<<i);
    }
    return s<P;
}
long long dfs(long long l,long long r)
{
    if(l==r) return l;
    long long mid=(l+r)/2;
    if(judge(mid+1)) return dfs(mid+1,r);
    else return dfs(l,mid);
}

bool judge1(long long k)
{
    long long s=0,res;
    res=k+1;
    for(int i=N-1;i>=0;i--)
    {
        if(res>1)
        {
            s+=(1LL<<i);
            res/=2;
        }
    }
    return s<P;
}
long long dfs1(long long l,long long r)
{
    if(l==r) return l;
    long long mid=(l+r)/2;
    if(judge1(mid+1)) return dfs1(mid+1,r);
    else return dfs1(l,mid);
}
int main()
{
    freopen("BB.in","r",stdin);
    freopen("BB.out","w",stdout);
    int i,j,k;
    int T;scanf("%d",&T);
    int tt=0;
    while(T--)
    {tt++;
        scanf("%d%lld",&N,&P);
        printf("Case #%d: %lld %lld\n",tt,dfs1(0,(1LL<<N)-1),dfs(0,(1LL<<N)-1));
    }
    return 0;
}
