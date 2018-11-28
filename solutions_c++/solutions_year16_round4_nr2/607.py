#include <cstring>
#include <cstdio>
#include <algorithm>
#define N 210
using namespace std;

int T, n, k, tot, q[N];
double f[N][N * 2], ans, p[N];

void calc() {
	memset(f, 0, sizeof f);
	f[0][k] = 1;
	for(int i = 1; i <= k; i++)	{
		int now = q[i];
		for(int j = 0; j <= 2 * k; j++) {
			if (2 * k > j) f[i][j] += f[i-1][j+1] * (1 - p[now]);
			if (0 < j) f[i][j] += f[i - 1][j - 1] * p[now];
		}
	}
	ans = max(ans, f[k][k]);
}

/*
void awner() {
	siz[u] = 1;
	vis[u] = 1;
	for (int i = r[u]; i; i = e[i].n) {
		int v = e[i].t;
		if (vis[v]) continue;
		dep[v] = dep[u] + 1;
		fa[v] = u;
		dfs1(v);
		siz[u] += siz[v];
		if (!son[u] || siz[son[u]] < siz[v]) son[u] = v;
	}
	vis[u] = 1;
	top[u] = per;
	pos[u] = ++tim;
	fp[tim] = u;
	if (!son[u]) return;
	dfs2(son[u], per);
	for (int i = r[u]; i; i = e[i].n) {
		int v = e[i].t;
		if (vis[v]) continue;
		if (v != son[u]) dfs2(v, v);
	}
}

*/
void init() {
	scanf("%d%d", &n, &k);
	for (int i = 1; i <= n; i ++) scanf("%lf", &p[i]);
	sort(p + 1, p + 1 + n);
	ans = 0;
}

void work() {
	for (int i = 0; i <= k; i ++) {
		tot = 0;
		for (int j = 1; j <= i; j ++) q[++tot] = j;
		for (int l = 1, j = n; l + i <= k; l ++, j --) q[++tot] = j;
		if (tot != k) printf("\n");
		calc();
	}
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++) {
		printf("Case #%d: ", t);
		for (int j = 1; j <= 100000; j++){} //rp++++++++
		init();
		work();
		printf("%.5f\n", ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}