#include <bits/stdc++.h>
using namespace std;

int C, D, V;
int a[111];

int solve() {
	scanf("%d%d%d", &C, &D, &V);
	for (int i = 0; i < D; i++) scanf("%d", a + i);
	
	vector<int> dp(V + 1, 0);
	dp[0] = 1;
	for (int i = 0; i < D; i++) {
		for (int j = V; a[i] <= j; j--) {
			dp[j] |= dp[j - a[i]];
		}
	}
	
	int mask = 0;
	for (int i = 1; i < D; i++) {
		mask |= dp[i] << i - 1;
	}
	
	int ret = 1 << 30;
	for (int i = 0; i < 1 << V; i++) {
		if (i & mask) continue;
		if (5 < __builtin_popcount(i)) continue;
		vector<int> v;
		for (int j = 0; 1 << j <= i; j++) {
			if (i & 1 << j) v.push_back(j + 1);
		}
		auto tmp = dp;
		for (int& j : v) {
			for (int k = V; j <= k; k--) {
				tmp[k] |= tmp[k - j];
			}
		}
		int sum = 0;
		for (int& j : tmp) sum += j;
		if (sum == V + 1) ret = min(ret, (int)v.size());
		if (ret == 0 || ret == 1) break;
	}
	
	return ret;
	
	/*
	vector<int> ng;
	for (int i = 1; i <= V; i++) {
		if (!dp[i]) ng.push_back(i);
	}
	*/
	//for (int& i : ng) printf("%d ", i); puts("");
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}

