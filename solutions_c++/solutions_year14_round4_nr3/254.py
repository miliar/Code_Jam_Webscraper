#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<cmath>
#define ll long long
using namespace std;


const int oo = 2000000010;
const int maxn = 105000;
struct EE
{
    int to,ne,c;
}e[500010];
int head[maxn],L,st,ed,N;
int d[maxn],pre[maxn],pree[maxn],gap[maxn],low[maxn],cur[maxn];
void adde(int u,int v,int c)
{
   // cout<<u<<' '<<v<<endl;
    e[L].to = v;
    e[L].c = c;
    e[L].ne = head[u];
    head[u] = L++;
    e[L].to = u;
    e[L].c = 0;
    e[L].ne = head[v];
    head[v] = L++;
}
int sap()
{
    int ret = 0;
    bool fail;
    for (int i = 0; i <= N; i++) {
        cur[i] = head[i];
        d[i] = 0;
        low[i] = 0;
        gap[i] = 0;
    }
    low[st] = oo;
    gap[0] = N;
    int u = st;
    while (d[st] < N) {
        fail = true;
        for (int i = cur[u]; i != -1; i = e[i].ne) {
            int  v = e[i].to;
            cur[u] = i;
            if (e[i].c && d[u] == d[v] + 1) {
                pre[v] = u;
                pree[v] = i;
                low[v] = min(low[u],e[i].c);
                u = v;
                if (u == ed) {
                    do
                    {
                        e[pree[u]].c -= low[ed];
                        e[pree[u]^1].c += low[ed];
                        u = pre[u];
                    }while (u != st);
                    ret += low[ed];
                }
                fail = false;
                break;
            }
        }
        if (fail) {
            gap[d[u]]--;
            if (!gap[d[u]]) return ret;
            d[u] = N;
            for (int i = head[u]; i != -1; i = e[i].ne)
            if (e[i].c) d[u] = min(d[u],d[e[i].to] + 1);
            gap[d[u]]++;
            cur[u] = head[u];
            if (u != st) u = pre[u];
        }
    }
    return ret;
}

int W,H,B;
struct PP
{
    int x[2];
    int y[2];
}p[1100];
const int dir[4][2] = {0,1,0,-1,1,0,-1,0};
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T;
    cin>>T;
    int cas = 1;
    while (T--) {
        scanf("%d%d%d",&W,&H,&B);
        for (int i = 0; i < B; i++) {
            scanf("%d%d%d%d",&p[i].x[0],&p[i].y[0],&p[i].x[1],&p[i].y[1]);
        }
        L = 0;
        memset(head,-1,sizeof(head));
        st = 2 * W * H;
        ed = st + 1;
        N = ed + 1;
        for (int i = 0 ;i < W; i++)
            for (int j = 0; j < H; j++) {
                bool fail = false;
                for (int k = 0 ;k < B; k++) {
                    if (i >= p[k].x[0] && i <= p[k].x[1] && j >= p[k].y[0] && j <= p[k].y[1]) fail = true;
                }
                if (fail) continue;
            //cout<<i<<' '<<j<<endl;
                int n = i * H + j;
                adde(2 * n,2 * n  + 1,1);
                for (int k = 0; k < 4 ;k ++) {
                    int ni = i + dir[k][0];
                    int nj = j + dir[k][1];
                    if (ni >= 0 && ni < W && nj >= 0 && nj < H) {
                    //    cout<<ni<<'x'<<nj<<' '<<i<<' '<<j<<endl;
                        int nn = ni * H + nj;
                        adde(2 * nn + 1,2 * n,1);
                    }
                }
                if (j == 0) adde(st,2 * n,1);
                if (j == H - 1) adde(2 * n + 1,ed,1);
            }
        int ans = sap();
        printf("Case #%d: %d\n",cas++,ans);
    }
}
