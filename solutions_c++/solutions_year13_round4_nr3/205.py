#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
#define DEBUG 0
#define debug(x) if(DEBUG)cout<<#x<<": "<<x<<endl;
#define FOR(i,j,k) for(i=j;i<=k;++i)
#define REP(i,j) for(i=0;i<j;++i)
#define FORD(i,j,k) for(i=j;i>=k;--i)
#define met(i,j) memset(i,j,sizeof(i))
#define sz(i) ((int)i.size())
#define PB push_back
#define MK make_pair
#define IOopen ios_base::sync_with_stdio(0)
const int inf=~0U>>1;
typedef pair<int, int> PII;
typedef unsigned long long ULL;
typedef long long LL;
#define N 25
int n,a[N],b[N],f2[N],f1[N],x[N],bj[N];

void init()
{
    int i;
    scanf("%d",&n);
    FOR(i,1,n)scanf("%d",a+i);
    FOR(i,1,n)scanf("%d",b+i);
}

bool check()
{
    int i,j;
    FORD(i,n,1)
    {
        f2[i]=1;
        FOR(j,i+1,n)
        {
            if(x[j]<x[i])f2[i]=max(f2[i],f2[j]+1);
        }
        if(f2[i]!=b[i])return 0;
    }
    return 1;
}

bool dfs(int ii)
{
    int i,j;
    if(ii>n)
    {
        return check();
    }else
    {
        FOR(i,1,n)
        if(!bj[i])
        {
            bj[i]=1;
            x[ii]=i;
            f1[ii]=1;
            FOR(j,1,ii-1)
            {
                if(x[j]<i)f1[ii]=max(f1[ii],f1[j]+1);
            }
            if(f1[ii]==a[ii]){if(dfs(ii+1))return 1;}
            bj[i]=0;
        }
        return 0;
    }
}

void work()
{
    int i;
    met(bj,0);
    dfs(1);
    FOR(i,1,n)printf("%d ",x[i]);
    printf("\n");
}

int main()
{
    int i,T;
    scanf("%d",&T);
    FOR(i,1,T)
    {
        printf("Case #%d: ",i);
        init();
        work();
    }
}
