#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAXN=100000+10;
const int MAXM=500000*2+2*MAXN;
const ll inf=1LL<<50;
const ll GG = 1LL << 30;

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

int ans[1100][1100], a[1100], b[1100];

vector<int> g[30];
int id[300];
map<string, int> mp;
char s[10000], ts[10000];

int gao(char *s) {
    if (mp.find(s) == mp.end()) {
        int id = mp.size();
        mp[s] = id;
    }
    return mp[s];
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    gets(s);
    for (int cas = 1; cas <= T; cas++) {
        memset(box,-1,sizeof(box));
        cnt=0;
        mp.clear();
        int n;
        scanf("%d", &n);
        gets(s);
        for (int i = 0; i < n; i++) {
            gets(s);
            int len = strlen(s);
            g[i].clear();
            for (int j = 0; j < len; j++) {
                if (s[j] != ' ') {
                    int pos = j, cnt = 0;
                    while (pos < len && s[pos] != ' ') {
                        ts[cnt++] = s[pos];
                        pos++;
                    }
                    ts[cnt] = 0;
                    g[i].push_back(gao(ts));
                    j = pos;
                }
            }
        }
        N = (mp.size() + n) * 2 + 2;
        NS = N - 1;
        NT = N - 2;
        int cnt = mp.size();
        for (int i = 0; i < cnt; i++) {
            int id = (i + n);
            add(id * 2, id * 2 + 1, 1);
        }
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                add(NS, i * 2, GG);
                add(i * 2 + 1, NT, inf);
            } else if (i == 1) {
                add(NS, i * 2, inf);
                add(i * 2 + 1, NT, GG);
            } else {
                add(NS, i * 2, GG);
                add(i * 2 + 1, NT, GG);
            }
            add(i * 2, i * 2 + 1, inf);
                for (auto x : g[i]) {
                    int id = x + n;
                    add(i * 2, id * 2, inf);
                    add(id * 2 + 1, i * 2 + 1, inf);
                }
        }
        ll res = sap() - n * GG;
        printf("Case #%d: %I64d\n", cas, res);
        fprintf(stderr, "%d %I64d\n", cas, res);
    }
    return 0;
}