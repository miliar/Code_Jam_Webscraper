#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#define inf 2100000000
using namespace std;
const int maxn = 100010;
int n, m, k,s,t;
int tot, start, end1;
int h[maxn],vh[maxn];
int mp[510][510];
int dx[maxn],dy[maxn];
struct edge
{
    int u,v,f,next;
}e[maxn*8];
int box[maxn],cnt;
int gap[maxn],d[maxn],curedge[maxn],pre[maxn];
void init()
{
    memset(box,-1,sizeof(box));
    cnt=0;
}
void add(int u,int v,int f)
{
    e[cnt].u=u;
    e[cnt].v=v;
    e[cnt].f=f;
    e[cnt].next=box[u];
    box[u]=cnt++;
    e[cnt].u=v;
    e[cnt].v=u;
    e[cnt].f=0;
    e[cnt].next=box[v];
    box[v]=cnt++;
}
int SAP()
{
    int cur_flow,flow_ans=0,u,tmp,neck,i,v;
    memset(d,0,sizeof(d));
    memset(gap,0,sizeof(gap));
    memset(pre,-1,sizeof(pre));
    for(i=0;i<=n;i++)
        curedge[i]=box[i];
    gap[0]=n+1;
    u=s;
    while(d[s]<n+1)
    {
        if(u==t)
        {
            cur_flow=inf;
            for(i=s;i!=t;i=e[curedge[i]].v)
            {
                if(cur_flow>e[curedge[i]].f)
                {
                    neck=i;
                    cur_flow=e[curedge[i]].f;
                }
            }
            for(i=s;i!=t;i=e[curedge[i]].v)
            {
                tmp=curedge[i];
                e[tmp].f-=cur_flow;
                e[tmp^1].f+=cur_flow;
            }
            flow_ans+=cur_flow;
            u=neck;
        }
        for(i=curedge[u];i!=-1;i=e[i].next)
        {
            v=e[i].v;
            if(e[i].f&&d[u]==d[v]+1)
                break;
        }
        if(i!=-1)
        {
            curedge[u]=i;
            pre[v]=u;
            u=v;
        }
        else
        {
            if(0==--gap[d[u]])
                break;
            curedge[u]=box[u];
            for(tmp=n+5,i=box[u];i!=-1;i=e[i].next)
                if(e[i].f)
                    tmp=min(tmp,d[e[i].v]);
            d[u]=tmp+1;
            ++gap[d[u]];
            if(u!=s)
                u=pre[u];
        }
    }
    return flow_ans;
}
int id(int x,int y)
{
    return x*m+y;
}
int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int ncase,T=0;
    scanf("%d",&ncase);
    while(ncase--)
    {
        printf("Case #%d: ",++T);
        scanf("%d %d %d",&m,&n,&k);
        memset(mp,0,sizeof(mp));
        int x1,x2,y1,y2;
        for(int i = 0; i < k; ++i)
        {
            scanf("%d %d %d %d", &y1, &x1, &y2, &x2);
            for(int x = x1; x <= x2; ++x)
                for(int y = y1; y <= y2; ++y)
                    mp[x][y] = 1;
        }
        init();
        tot = n * m * 2 + 2, start = tot - 2, end1 = tot - 1;
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < m; ++j)
            {
                if(mp[i][j]) continue;
                for(int k = 0; k < 4; ++k)
                {
                    int ii = i + dx[k], jj = j + dy[k];
                    if(mp[ii][jj] == 0)
                    add(id(i, j)+n*m,id(ii, jj),inf);
                }
            }
        cout << SAP() << endl;
    }
    return 0;
}
