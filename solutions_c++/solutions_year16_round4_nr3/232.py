#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <set>
#include <map>
#define fi first
#define se second
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
// head
const int N = 36;

// Â·¾¶Ñ¹Ëõ
struct DisjointSetUnion {
	int fa[N*4];

	int find(int x) {
		return (x == fa[x]) ? x : (fa[x] = find(fa[x]));
	}
	void init(int n) {
		for (int i = 0; i <= n; i++) fa[i] = i;
	}
	void joint(int u, int v) {
		u = find(u), v = find(v);
		if (u != v)	fa[u] = v;
	}
	bool same(int u, int v) {
		return find(u) == find(v);
	}
};

int t, n, m, tot, cnt, cas = 1;
int a[N], pos[N];
PII b[N];
bool g[N][N];
DisjointSetUnion dsu;

int get(int r, int c, int f) {
	return r * (4 * m) + 4 * c + f;
}

void init() {
	for (int i = 0; i < m; i++) {
		pos[i] = get(0, i, 0);
		pos[n+m+i] = get(n-1, m-1-i, 2);
	}
	for (int i = 0; i < n; i++) {
		pos[m+i] = get(i, m-1, 1);
		pos[n+m+m+i] = get(n-1-i, 0, 3);
	}
}

bool ck() {
	dsu.init(cnt * 4);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (i > 0) dsu.joint(get(i, j, 0), get(i-1, j, 2));
			if (j > 0) dsu.joint(get(i, j, 3), get(i, j-1, 1));
			if (g[i][j]) {
				dsu.joint(get(i, j, 0), get(i, j, 3));
				dsu.joint(get(i, j, 1), get(i, j, 2));
			} else {
				dsu.joint(get(i, j, 0), get(i, j, 1));
				dsu.joint(get(i, j, 2), get(i, j, 3));
			}
		}
	}
	for (int i = 0; i < tot; i += 2) {
		if (!dsu.same(pos[a[i]], pos[a[i+1]])) return false;
	}
	return true;
}

int main() {
	freopen("out1.txt", "w", stdout);
	scanf("%d", &t);
	while (t--) {
		scanf("%d%d", &n, &m);
		tot = 2 * (n + m);
		for (int i = 0; i < tot; i++) {
			scanf("%d", a+i);
			a[i]--;
		}

		cnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				b[cnt++] = {i, j};
			}
		}
		init();
		bool ans = false;
		int mx = 1 << cnt;
		for (int i = 0; i < mx && !ans; i++) {
			for (int j = 0; j < cnt; j++) {
				g[b[j].fi][b[j].se] = ((1 << j) & i) >> j;
				if (ck()) {
					ans = true;
					break;
				}
			}
		}
		printf("Case #%d:\n", cas++);
		if (ans) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					putchar(g[i][j] ? '/' : '\\');
				}
				puts("");
			}
		} else {
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}
