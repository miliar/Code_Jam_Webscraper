#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

#define N 2100000

int len, m[N], next[N], go[N], till[N], fa[N], dep[N], ss[N], s[N], n, d, a, c, r;
vector <int> ve[N];
bool ok[N];

void add(int x, int y) {
	next[++len] = till[x];
	till[x] = len;
	go[len] = y;
}

int gf(int x) {
	if (fa[x] != x)
		fa[x] = gf(fa[x]);
	return fa[x];
}

void Merge(int x, int y) {
	x = gf(x);
	y = gf(y);
	if (dep[x] > dep[y])
		swap(x, y);
	ss[x] += ss[y];
	fa[y] = x;
}

void dfs(int k, int fa) {
	if (fa >= 0) dep[k] = dep[fa] + 1;
	for (int i = till[k]; i; i = next[i])
		if (go[i] != fa) dfs(go[i], k);
}

int dfs1(int k) {
	fa[k] = k;
	ok[k] = false;
	int sum = 1;
	for (int i = till[k]; i; i = next[i])
		if (dep[go[i]] > dep[k] && ok[go[i]]) sum += dfs1(go[i]);
	return sum;
}

void solve() {
	scanf("%d%d", &n, &d);
	scanf("%d%d%d%d", &s[0], &a, &c, &r);
	for (int i = 1; i < n; i++) {
		s[i] = (1LL * s[i - 1] * a + c) % r;
	}
	scanf("%d%d%d%d", &m[0], &a, &c, &r);
	for (int i = 1; i < n; i++) {
		m[i] = (1LL * m[i - 1] * a + c) % r;
	}
	for (int i = 0; i <= n; i++)
		till[i] = 0;
	len = 0;
	for (int i = 1; i < n; i++) {
		add(i, m[i] % i);
		add(m[i] % i, i);
	}
	for (int i = 0; i < n; i++)
		fa[i] = i, ss[i] = 1;
	for (int i = 0; i <= 1000000; i++)
		ve[i].clear();
	for (int i = 0; i < n; i++)
		ve[s[i]].push_back(i);
	int ans = n - 1;
	for (int i = 0; i < n; i++)
		ok[i] = false;
	dfs(0, -1);
	for (int i = 0; i <= d; i++)
		for (int j = 0; j < (int) ve[i].size(); j++) {
			ok[ve[i][j]] = true;
			int t = ve[i][j];
			for (int p = till[t]; p; p = next[p])
				if (ok[go[p]]) Merge(t, go[p]);
		}
	ans = min(ans, n - ss[gf(0)]);
	for (int i = 1; i <= 1000000; i++) {
		for (int j = 0; j < (int) ve[i - 1].size(); j++) {
			int t = ve[i - 1][j];
			if (!ok[t]) continue;
			int k = gf(t);
			ss[k] -= dfs1(t);
		}
		for (int j = 0; j < (int) ve[i + d].size(); j++) {
			int t = ve[i + d][j];
			ok[t] = true;
			for (int p = till[t]; p; p = next[p])
				if (ok[go[p]]) Merge(t, go[p]);
		}
		ans = min(ans, n - ss[gf(0)]);
	}
	printf("%d\n", n - ans);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}
