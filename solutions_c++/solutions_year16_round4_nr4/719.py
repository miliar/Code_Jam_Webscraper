#include <bits/stdc++.h>
using namespace std;
int n, ans, tans;
char a[10][10];
vector<int> b;
bool flag[10];

bool dfs2(int p, int q) {
	if (q >= b.size()) return 1;
	int v = b[q];
	for (int i = 1; i <= n; i++) 
		if (i != p && a[v][i] == '1') {
			if (!flag[i]) {
				flag[i] = true;
				if (dfs2(p, q + 1)) return 1;
				flag[i] = false;
			}
		}
	return 0;
}
bool check(int p) {
	memset(flag, 0, sizeof(flag));
	return dfs2(p, 0);
}
void dfs(int p, int q, int sum) {
	if (p == n + 1) {
		for (int j = 1; j <= n; j++) {
			b.clear();
			for (int i = 1; i <= n; i++)
				if (a[i][j] == '1')
					b.push_back(i);
			if (b.size() == 0) return;
			if (b.size() == n) continue;
			if (check(j)) return;
		}
		ans = min(ans, sum);
		return;
	}
	if (sum >= ans) return;
	if (q != n) dfs(p, q + 1, sum);
	else dfs(p + 1, 1, sum);
	if (a[p][q] == '0') {
		a[p][q] = '1';
		if (q != n) dfs(p, q + 1, sum + 1);
		else dfs(p + 1, 1, sum + 1);
		a[p][q] = '0';
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) scanf("%s", a[i] + 1);
		ans = n * n + 1;
		dfs(1, 1, 0);
		printf("Case #%d: %d\n", tt, ans);
	}
}
