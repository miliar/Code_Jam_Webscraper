//c++  #pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define INF (1<<29)
#define eps (1e-5)
#define pb push_back
using namespace std;
/*
struct Edge{
    int v,next,w;
}edge[MAXN*3];
int E,list[MAXN];
void init() {memset(list,E=-1,sizeof(list)); }
void add(int u,int v,int w)
{
    edge[++E].v=v; edge[E].w=w; edge[E].next=list[u]; list[u]=E;
}
*/

int w[205],b[25],n;
int a[25][205];
vector<int> ans[1<<21];

bool jud(int a,int b)
{
    if (ans[a].size()==0) return true;
    for (int i=0;i<ans[a].size();i++)
        if (ans[a][i]<ans[b][i])
            return true;
        else
        if (ans[a][i]>ans[b][i])
            return false;
    return false;
}
void dfs(int s)
{
    //printf("%d\n",s);
    if (ans[s].size()) return;
    if (s==0) return;
    rep(i,1,n)
        if (s&(1<<i-1))
            ans[s].pb(n+1);
    rep(i,1,n)
        if (s&(1<<i-1))
        {
            int pre=s^(1<<i-1);
            int tmp=w[b[i]];
            rep(j,1,n)
                if (pre&(1<<j-1))
                {
                    tmp+=a[j][ b[i] ];
                    if (b[j]==b[i]) tmp--;
                }
            if (tmp>0)
            {
                dfs(pre);
                if (!jud(pre,s)) continue;
                ans[s]=ans[pre];
                ans[s].pb(i);
            }
        }

}

int main()
{
    freopen("D-small-attempt4.in","r",stdin);
    freopen("d.out","w",stdout);
    int T,cas=0,K;
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d%d",&K,&n);
        //printf("%d %d\n",K,n);
        memset(w,0,sizeof(w));
        memset(a,0,sizeof(a));
        rep(i,1,K)
        {
            int tmp;
            scanf("%d",&tmp);
            //printf("%d ",tmp);
            w[tmp]++;
        }
        //puts("");
        rep(i,1,n)
        {
            int tmp;
            scanf("%d%d",&b[i],&tmp);
            //printf("%d %d",b[i],tmp);
            while (tmp--)
            {
                int x;scanf("%d",&x);a[i][x]++;
                //printf(" %d",x);
            }
            //puts("");
        }
        printf("Case #%d:",++cas);
        for (int i=0;i<(1<<n);i++) ans[i].clear();
        dfs((1<<n)-1);
        if (ans[(1<<n)-1][0]==n+1) puts(" IMPOSSIBLE");
        else
        {
            rep(i,1,n) printf(" %d",ans[(1<<n)-1][i-1]); puts("");
        }
    }
    //system("pause");
    return 0;
}
