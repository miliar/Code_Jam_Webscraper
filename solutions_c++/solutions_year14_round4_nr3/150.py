#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>

#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=n-1;i>=0;i--)
#define FOR(i,n) for(int i=1;i<=(n);i++)
#define FORD(i,n) for(int i=(n);i>=1;i--)

#define SZ(x) ((int)x.size())
#define CC(a,x) memset(a,x,sizeof(a))
#define TWO(x) ((LL)1<<(x))

#define DEBUG

using namespace std;

const int maxn=200000;
const int oo=200000000;
const int maxm=16*maxn;

int pn,d[maxn],vd[maxn],S,T,eh;

struct edge
{
	int t,c;
	edge *op,*next;
}E[maxm],*V[maxn];

void addedge(int a,int b,int c)
{
    //printf("\n%d %d %d", a, b, c);
	E[++eh].next = V[a];  V[a] = E+eh;  V[a]->t = b;  V[a]->c = c;
	E[++eh].next = V[b];  V[b] = E+eh;  V[b]->t = a;  V[b]->c = 0;
	V[a]->op = V[b];  V[b]->op = V[a];
}

int dfs(int u,int flow)
{
	int now=0;
	if (u==T) return flow;
	for (edge *j=V[u];j;j = j->next)
	{
		int v=j->t;
		if (d[u]==d[v]+1 && j->c>0)
		{
			int t=dfs(v,min(flow-now,j->c));
			if (t)
			{
				now+=t;
				j->c -= t;
				j->op->c +=t;
				if (now==flow) return now;
			}
		}
	}
	
	if (d[S]>=pn) return now;
	if (--vd[d[u]] == 0) d[S]=pn;
	vd[++d[u]]++;
	return now;
}

int g[101][501];
int n, m;

int D(int i, int j, int o) {
    return 1 + i * m + j + (o ? n * m : 0);   
}

void solve() {
    CC(V, 0); eh = 0; CC(g, 0); CC(vd, 0); CC(d, 0);
    int q;
    scanf("%d%d%d", &n, &m, &q);
    REP(t, q) {
        int lx, ly, rx, ry;
        scanf("%d%d%d%d", &lx, &ly, &rx, &ry);   
        for (int i = lx; i<= rx; i++)
        for (int j = ly; j<= ry; j++)
            g[i][j] = 1;
    }
    S = 0; T = 2 * n * m + 1; pn = T + 1;
    REP(i, n) REP(j, m) {
        if (j == 0 && !g[i][j]) addedge(S, D(i, j, 0), 1);
        if (j == m-1 && !g[i][j]) addedge(D(i, j, 1), T, 1);
        if (!g[i][j]) addedge(D(i, j, 0), D(i, j, 1), 1);
        if (i>0 && !g[i-1][j]) addedge(D(i, j, 1), D(i-1, j, 0), 1);
        if (i<n-1 && !g[i+1][j]) addedge(D(i, j, 1), D(i+1, j, 0), 1);
        if (j>0 && !g[i][j-1]) addedge(D(i, j, 1), D(i, j-1, 0), 1);
        if (j<m-1 && !g[i][j+1]) addedge(D(i, j, 1), D(i, j+1, 0), 1);
    }
    vd[0] = pn;
    int ans = 0;
	while (d[S]<pn)
        ans += dfs(S, oo);
    printf("%d", ans);
}

typedef long long LL;
int main()
{
#ifdef DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif
    int T;
    scanf("%d",&T);
    FOR(i, T) {
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }
	return 0;
}
