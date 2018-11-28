#include <cstdio>
#include <memory.h>
using namespace std;

int T, w, h, b, x0, y0, x1, y1, s, t, len;
bool used[3000][3000];

#define INF 1000000000
#define min(x, y) ((x) < (y) ? (x) : (y))
int n, m, i, till[1100000], go[6100000], next[6100000], f[6100000], deg[1100000], D[1100000], n1[1100000];
bool cc[1100000];

void add(int x, int y, int z) {
	next[++len] = till[x];
	till[x] = len;
	go[len] = y;
	f[len] = z;
}

void Ad(int x, int y, int z) {
	add(x, y, z);
	add(y, x, 0);
}

bool bfs() {
	int q, h, i;
	for (i = s; i <= t; i++)	D[i] = 0, cc[i] = 1;
	for (D[n1[q = h = 1] = s] = 1; q <= h; q++)
		for (i = till[n1[q]]; i; i = next[i])
			if (f[i] && !D[go[i]])	D[n1[++h] = go[i]] = D[n1[q]] + 1;
	return D[t];
}

int dfs(int k, int mi) {
	if (k == t)	return mi;
	int i, tmp, sum = 0;
	for (i = till[k]; i && mi; i = next[i])
		if (f[i] && D[go[i]] == D[k] + 1 && cc[go[i]]) {
			tmp = dfs(go[i], min(mi, f[i]));
			sum += tmp;
			mi -= tmp;
			f[i] -= tmp;
			f[i ^ 1] += tmp;
		}
	if (!sum)	cc[k] = false;
	return sum;
}

int maxFlow() {
	int sum = 0;
	while (bfs())	sum += dfs(s, INF);
	return sum;
}

int it(int x, int y, int p) {
	return p * w * h + x * h + y + 1;
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("c1.out", "w", stdout);
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		scanf("%d%d%d", &w, &h, &b);
		memset(used, false, sizeof used);
		while (b--) {
			scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
			for (int i = x0; i <= x1; i++)
				for (int j = y0; j <= y1; j++)
					used[i][j] = true;
		}
		len = 1;
		memset(till, 0, sizeof till);
		s = 0;
		t = 2 * w * h + 1;
		for (int i = 0; i < w; i++)	Ad(s, it(i, 0, 0), 1);
		for (int i = 0; i < w; i++)	Ad(it(i, h - 1, 1), t, 1);
		for (int i = 0; i < w; i++)
			for (int j = 0; j < h - 1; j++)	Ad(it(i, j, 1), it(i, j + 1, 0), 1), Ad(it(i, j + 1, 1), it(i, j, 0), 1);
		for (int i = 0; i < w - 1; i++)
			for (int j = 0; j < h; j++)	Ad(it(i, j, 1), it(i + 1, j, 0), 1), Ad(it(i + 1, j, 1), it(i, j, 0), 1);
		for (int i = 0; i < w; i++)
			for (int j = 0; j < h; j++)	if (!used[i][j])	Ad(it(i, j, 0), it(i, j, 1), 1);
		printf("Case #%d: %d\n", tt, maxFlow());
	}
}
