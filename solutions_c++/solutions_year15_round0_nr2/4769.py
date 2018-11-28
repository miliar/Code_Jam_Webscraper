#include <cstring>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
int const N = 1e4 + 10, M = N * 100, mod = 1e9 + 7;
typedef unsigned long long ull;
int n, k, u, v, w, cnt, ans, h[N], s[N], f[N], root, dep[N];
bool used[N];
struct Edge {
	int v, n, l;
} g[N << 1];
void insert(int f, int t, int l) {
	g[cnt].v = t;
	g[cnt].l = l;
	g[cnt].n = h[f];
	h[f] = cnt++;
	g[cnt].v = f;
	g[cnt].l = l;
	g[cnt].n = h[t];
	h[t] = cnt++;
}
void centro(int rt, int fa, int sz) {
	s[rt] = 1, f[rt] = 0;
	for (int i = h[rt], t; ~i; i = g[i].n)
		if ((t = g[i].v) != fa && !used[t]) {
			centro(t, rt, sz);
			s[rt] += s[t];
			f[rt] = max(f[rt], s[t]);
		}
	f[rt] = max(f[rt], sz - s[rt]);
	if (f[rt] < f[root]) root = rt;
}
void search(int rt, int fa, vector<int> &deps) {
	deps.push_back(dep[rt]);
	s[rt] = 1;
	for (int i = h[rt], t; ~i; i = g[i].n)
		if ((t = g[i].v) != fa && !used[t]) {
			dep[t] = dep[rt] + g[i].l;
			search(t, rt, deps);
			s[rt] += s[t];
		}
}
int calc(int rt, int d = 0) {
	vector<int> deps;
	dep[rt] = d;
	search(rt, 0, deps);
	sort(deps.begin(), deps.end());
	int ret = 0;
	for (int l = 0, r = deps.size() - 1; l < r;)
		if (deps[l] + deps[r]  <= k) ret += r - l++;
		else r--;
	return ret;
}
void work() {
	ans += calc(root);
	used[root] = true;
	for (int i = h[root], t; ~i; i = g[i].n)
		if (!used[t = g[i].v]) {
			ans -= calc(t, g[i].l);
			centro(t, root = 0, f[0] = s[t]);
			work();
		}
}
int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	while (~scanf("%d%d", &n, &k)) {
		if (0 == n && 0 == k) break;
		memset(h, -1, sizeof(h));
		memset(used, false, sizeof(used));
		ans = cnt = 0;
		for (int i = 1; i < n; i++) {
			scanf("%d%d%d", &u, &v, &w);
			insert(u, v, w);
		}
		centro(1, root = 0, f[0] = n);
		work();
		cout << ans << endl;
	}
	return 0;
}