#include <iostream>
#include <cstdio>
#include <map>
#include <algorithm>
#include <cstring>

using namespace std;

map<int, int> f;
int cnt, n, m;
bool flag[333];
int ans[333], now[333], a[333];
int g[333][333];
bool pool[1111111];
bool found;

int num() {
	int x; cin >> x;
	if (f.find(x) == f.end()) f[x] = cnt++;
	return f[x];
}

void dfs(int step, int s) {
	if (found || pool[s]) return ;

	pool[s] = true;
	if (step >= n) {
		found = true; return ;
	}

	for (int i = 0; i < n; ++i) if (!flag[i] && now[a[i]] > 0) {
		flag[i] = true;
		ans[step] = i;
		for (int j = 0; j < cnt; ++j) now[j] += g[i][j];
		now[a[i]]--;

		dfs(step + 1, s | (1 << i));
		if (found) return ;

		flag[i] = false;
		for (int j = 0; j < cnt; ++j) now[j] -= g[i][j];
		now[a[i]]++;
	}
}

void work() {
	f.clear(); cnt = 0; cin >> m >> n;

	memset(now, 0, sizeof(now));
	for (int i = 0; i < m; ++i) now[num()]++;

	memset(g, 0, sizeof(g));
	for (int i = 0; i < n; ++i) {
		a[i] = num();

		int tot; cin >> tot;
		for (int j = 0; j < tot; ++j) g[i][num()]++;
	}

	memset(flag, 0, sizeof(flag));
	found = false;
	memset(pool, 0, sizeof(pool));
	dfs(0, 0);

	if (found) {
		for (int i = 0; i < n; ++i) printf(" %d", ans[i] + 1);
		puts("");
	}
	else puts(" IMPOSSIBLE");
}

int main(){
	int T; cin >> T;
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d:", i);
		work();
	}

	return 0;
}
