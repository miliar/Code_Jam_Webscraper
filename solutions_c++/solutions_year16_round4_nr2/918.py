#include <bits/stdc++.h>

using namespace std;

const int MAXN = 300;

int n, k;
double ans, tans;
double p[MAXN], a[MAXN];

void dfs(int dep, int less, double q) {
	if (dep == k) {
		if (less == 0) tans += q;
		return;
	}
	if (less > 0) {
		dfs(dep+1, less-1, q * a[dep]);
		dfs(dep+1, less, q * (1-a[dep]));
	}
	else 
		dfs(dep+1, less, q * (1-a[dep]));
}

void dfs2(int dep, int q) {
	if (dep == n || q == k) {
		return;
	}
	if (n - dep < k - q) return;
	if (q < k){
		a[q] = p[dep];
		if (q == k-1) {
			tans = 0;
			dfs(0, k / 2, 1);
			ans = max(ans, tans);
		}
		dfs2(dep+1, q + 1);
		dfs2(dep+1, q);
	}
	else
		return;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i++) scanf("%lf", &p[i]);
		ans = 0;
		dfs2(0, 0);
		printf("Case #%d: %.9f\n", tt, ans);
	}
	return 0;
}
