#include <stdio.h>
#include <string.h>
typedef int ll;
const int MAXN= 150000;
const int MAXM= MAXN * 50;
const ll inf=1<<30;
const ll Inf = 1 << 30;

int cnt,box[MAXN],pre[MAXN],gap[MAXN],h[MAXN],cur[MAXN];
int N,NS,NT;
ll flow[MAXN];

struct edge{
    int to,next;
    ll w;
} e[MAXM*2];

void adds(int u,int v,ll w)
{
    e[cnt].to=v;e[cnt].w=w;
    e[cnt].next=box[u];box[u]=cnt++;
}

void add(int u,int v,ll w)
{
    adds(u,v,w);
    adds(v,u,0LL);
}

ll mins(ll x,ll y)
{
    return x<y?x:y;
}

int qu[MAXN];

void bfs()
{
    memset(h,-1,sizeof(h));
    memset(gap,0,sizeof(gap));
    h[NT]=0;gap[0]=1;
    int st=0,ed=1;
    qu[ed]=NT;
    while(st!=ed)
    {
        int u=qu[++st];
        for(int p=box[u];p!=-1;p=e[p].next)
         if (h[e[p].to]==-1)
         {
             h[e[p].to]=h[u]+1;
             qu[++ed]=e[p].to;
             ++gap[ h[e[p].to]=h[u]+1 ];
         }
    }
}

ll sap()
{
    int u,v,p;

    ll flowans=0;
    //memset(gap,0,sizeof(gap));gap[0]=N;
   // memset(h,0,sizeof(h));
    bfs();
    for(int i=0;i<N;i++) cur[i]=box[i];
    flow[NS]=inf;
    u=NS;
    while(h[NS]<N)
    {
        for(p=cur[u];p!=-1;p=e[p].next)
         if (e[p].w&&h[e[p].to]+1==h[u])
         {
             cur[u]=p;
             v=e[p].to;
             flow[v]=mins(flow[u],e[p].w);
             pre[v]=p;
             u=v;
             if (u==NT)
             {
                 flowans+=flow[NT];
                 while(u!=NS)
                 {
                     e[pre[u]].w-=flow[NT];
                     e[pre[u]^1].w+=flow[NT];
                     u=e[pre[u]^1].to;
                 }
             }
             break;
         }
        if (p==-1)
        {
            cur[u]=box[u];
            if (--gap[h[u]]==0) break;
            h[u]=N;
            for(p=box[u];p!=-1;p=e[p].next)
             if (e[p].w&&h[e[p].to]+1<h[u])
                h[u]=h[e[p].to]+1;
            gap[h[u]]++;
            if (u!=NS) u=e[pre[u]^1].to;
        }
    }
    return flowans;
}
int a[1010][1010];
int wayx[10] = {-1, 0, 0, 1};
int wayy[10] = {0, -1, 1, 0};
int main()
{
    freopen("C-small-attempt5.in", "r", stdin);
        freopen("C-small-attempt5.out", "w", stdout);
    //freopen("gao.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int w, h, b;
        scanf("%d%d%d", &w, &h, &b);
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                a[i][j] = 0;
            }
        }
        for (int i = 0; i < b; i++) {
            int x0, y0, x1, y1;
            scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
            for (int j = y0; j <= y1; j++) {
                for (int k = x0; k <= x1; k++) {
                    a[j][k] = 1;
                }
            }
        }
        N = w * h * 2 + 2;
        NS = w * h * 2;
        NT = w * h * 2 + 1;
        memset(box, -1, sizeof(box));
        cnt = 0;
        for (int i = 0; i < w; i++) {
            if (!a[0][i]) {
                int id = i;
                add(NS, id * 2, Inf);
            }
            if (!a[h - 1][i]) {
                int id = (h - 1) * w + i;
                add(id * 2 + 1, NT, Inf);
            }
        }
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                int id = i * w + j;
                add(id * 2, id * 2 + 1, 1);
            }
        }
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (a[i][j]) continue;
                for (int k = 0; k < 4; k++) {
                    int tx = i + wayx[k];
                    int ty = j + wayy[k];
                    if (tx >= 0 && tx < h && ty >= 0 && ty < w && a[tx][ty] == 0) {
                        int id1 = i * w + j;
                        int id2 = tx * w + ty;
                        add(id1 * 2 + 1, id2 * 2, Inf);
                    }
                }
            }
        }
        ll ans=sap();
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
