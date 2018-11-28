#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<queue>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<stdlib.h>
#include<ctype.h>
#include<utility>
#include<cmath>
using namespace std;
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#define eps 1e-7
#define ll long long
#define i64 __int64
#define INF 10000005
#define pb push_back
#define sz(b) (int)b.size()
#define lson k<<1
#define rson k<<1|1
#define MOD 1000000007
#define CLR(t,x) memset(t,x,sizeof(t));
#define REP(k,x,y) for(k=x;k<y;k++)
#define N 1500000
int idx,p[1005],nxt[3005],vv[3005],del[1005],num[1005],node[1005][1005];
inline void add(int u,int v)
{
    nxt[idx]=p[u];
    vv[idx]=v,p[u]=idx++;
}
inline void dfs(int u,int fa)
{
    if(nxt[p[u]]==-1&&vv[p[u]]==fa)
    {
        num[u]=1;
        del[u]=0;
        return;
    }
    int cnt=0;
    num[u]=1;
    for(int i=p[u];i!=-1;i=nxt[i])
    {
        int v=vv[i];
        if(v==fa) continue;
        dfs(v,u);
        num[u]+=num[v];
        node[u][cnt++]=v;
    }
    if(cnt==1) del[u]=num[node[u][0]];
    else if(cnt>=2)
    {
        int sum=0,maxv1=-INF,maxv2=-INF;
        for(int i=0;i<cnt;i++)
        {
            int v=node[u][i];
            sum+=num[v];
            if(num[v]-del[v]>=maxv1) maxv2=maxv1,maxv1=num[v]-del[v];
            else if(num[v]-del[v]>maxv2) maxv2=num[v]-del[v];
        }
        del[u]=sum-maxv1-maxv2;
    }
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int cas,n,tt=1,u,v;
    scanf("%d",&cas);
    while(cas--)
    {
        scanf("%d",&n);
        idx=0;for(int i=1;i<=n;i++) p[i]=-1;
        for(int i=0;i<n-1;i++)
        {
            scanf("%d%d",&u,&v);
            add(u,v),add(v,u);
        }
        int ans=INF;
        for(int i=1;i<=n;i++)
        {
            CLR(del,0);
            CLR(num,0);
            dfs(i,0);
            ans=min(ans,del[i]);
            if(ans==0) break;
        }
        printf("Case #%d: %d\n",tt++,ans);
    }
    return 0;
}
