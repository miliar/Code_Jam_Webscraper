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
const int N = 5;

int a[N][N], b[N][N], temp[N];
char s[N][N];
bool vis[N];

int t, n, m, cas = 1;
vector<PII> v;

bool dfs(int pos) {
	if (pos == n) return true;
	int no = temp[pos], cnt = 0;;
	for (int j = 0; j < n; j++) {
		if (vis[j] || !b[no][j]) continue;
		cnt++;
		vis[j] = true;
		if (!dfs(pos+1)) return false;
		vis[j] = false;
	}
	return cnt > 0;
}

bool ck() {
	for (int i = 0; i < n; i++) {
		temp[i] = i;
	}
	do {
		memset(vis, 0, sizeof vis);
		if (!dfs(0)) return false;
	} while (next_permutation(temp, temp + n));
	return true;
}

int main() {
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	while (t--) {
		v.clear();
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%s", s[i]);
			for (int j = 0; j < n; j++) {
				a[i][j] = s[i][j] - '0';
				if (a[i][j] == 0) v.push_back({i, j});
			}
		}

		int ans = 1e9;
		m = v.size();
		int mx = 1 << m;
		for (int i = 0; i < mx; i++) {
			memcpy(b, a, sizeof a);
			for (int j = 0; j < m; j++) {
				if ((1 << j) & i) b[v[j].fi][v[j].se] = 1;
			}
			int cnt = __builtin_popcount(i);
			if (cnt >= ans) continue;
			if (ck()) ans = min(ans, __builtin_popcount(i));
		}
		printf("Case #%d: %d\n", cas++, ans);
	}
	return 0;
}
