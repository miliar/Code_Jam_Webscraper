#include<bits/stdc++.h>

using namespace std;

int p[25], sz[25], f[25], dp[1 << 25];

int dsu_get(int v) {
	if (p[v] != v) p[v] = dsu_get(p[v]);
	
	return p[v];
}

void dsu_merge(int u, int v) {
	u = dsu_get(u);
	v = dsu_get(v);
	
	if (u != v) {
		sz[v] += sz[u];
		f[v] += f[u];
		p[u] = v;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, ans = 0, zeros = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) p[i] = i, sz[i] = 1, f[i] = 0;
		
		for (int i = 0; i < n; i++) {
			char s[32];
			scanf(" %s", s);
			
			for (int j = 0; j < n; j++)
				for (int k = 0; k < n; k++)
					if (s[j] == '1' && s[k] == '1')
						dsu_merge(j, k);
			
			for (int j = 0; j < n; j++) {
				ans -= s[j] - '0';
			}
			
			zeros += 1;
			for (int j = 0; j < n; j++)
				if (s[j] == '1') {
					f[dsu_get(j)] += 1;
					
					zeros -= 1;
					
					break;
				}
		}
		
		vector<pair<int, int>> sizes;
		for (int i = 0; i < n; i++)
			if (dsu_get(i) == i) {
				if (f[i] == sz[i]) ans += sz[i] * sz[i];
				else sizes.emplace_back(sz[i], f[i]);
			}
		
		for (int i = 0; i < zeros; i++) sizes.emplace_back(0, 1);
		
		n = sizes.size();
		
		dp[0] = 0;
		for (int i = 1; i < (1 << n); i++) {
			dp[i] = 123456789;
			for (int j = i; j > 0; j = (j - 1) & i) {
				int a = 0, b = 0;
				for (int k = 0; k < n; k++)
					if (((j >> k) & 1) == 1) {
						a += sizes[k].first;
						b += sizes[k].second;
					}
				
				if (a == b) dp[i] = min(dp[i], dp[i ^ j] + a * a);
			}
		}
		
		ans += dp[(1 << n) - 1];
		
		printf("Case #%d: %d\n", t, ans);
	}
	
	return 0;
}
