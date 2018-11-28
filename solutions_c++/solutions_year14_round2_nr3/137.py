#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>
#include <deque>
#include <stack>

using namespace std;

string name[111];
vector<int> g[111];
int n, dep;
bool vis[111], old[111], del[111], mark[111];
string ans;
bool f[111][111];
int s[111];

inline bool cmp(const int& a, const int& b) {
	return f[a][b];
}

void dfs(int x) {
	mark[x] = true;
	for (size_t i = 0; i < g[x].size(); ++i) {
		int k = g[x][i]; if (mark[k] || old[k] || del[k]) continue;
		dfs(k);
	}
}

bool checkdel(int d) {
	memset(del, 0, sizeof(del));
	memset(mark, 0, sizeof(mark));
	for (int i = d; i <= dep; ++i) del[s[i]] = true;
	for (int i = 1; i <= n; ++i)
		if (!del[i] && old[i]) {
			dfs(i); break;
		}
	for (int i = 1; i <= n; ++i)
		if (!mark[i] && !old[i] && !del[i]) return false;
	return true;
}

void find() {
	int nd = -1, t = -1, d = dep;
	while (d) {
		int x = s[d];
		for (size_t i = 0; i < g[x].size(); ++i) {
			int k = g[x][i]; if (vis[k]) continue;
			if (t == -1 || f[k][t]) {
				t = k; nd = d;
			}
		}
		if (d > 1 && checkdel(d)) --d;
		else break;
	}

	for (int i = nd + 1; i <= dep; ++i) old[s[i]] = true;
	s[dep = nd + 1] = t; vis[t] = true; ans += name[t];
}

void work() {
	int m; cin >> n >> m;
	for (int i = 1; i <= n; ++i) cin >> name[i];
	for (int i = 1; i <= n; ++i) g[i].clear();
	for (int i = 0; i < m; ++i) {
		int x, y; cin >> x >> y;
		g[x].push_back(y); g[y].push_back(x);
	}
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= n; ++j)
			f[i][j] = name[i] < name[j];

	vector<int> r; for (int i = 1; i <= n; ++i) r.push_back(i);
	sort(r.begin(), r.end(), cmp);

	int p = r[0]; memset(vis, 0, sizeof(vis));
	memset(s, 0, sizeof(s));
	dep = 1; int now = r[0]; s[dep] = now; ans += name[now];
	memset(vis, 0, sizeof(vis)); memset(old, 0, sizeof(old));
	for (int t = 1; t < n; ++t) find();

	cout << ans << endl;
}

int main() {
	int T; scanf("%d", &T);

	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		work();
	}

	return 0;
}
