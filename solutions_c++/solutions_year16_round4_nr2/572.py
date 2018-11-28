#include <cstdio>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <vector>
using namespace std;
double ans;
int n, k;
vector <int> lis;
double p[300];
double f[300][300];
double dp() {
	f[0][0] = 1;
	for (int i = 1; i <= k; ++ i) {
		for (int j = 0; j <= i; ++ j) {
			f[i][j] = f[i - 1][j] * (1. - p[lis[i]]);
			if (j > 0) f[i][j] += f[i - 1][j - 1] * p[lis[i]];
		}
	}
	return f[k][k >> 1];
}
int count(int x) {
	int ret = 0;
	while (x) {
		ret ++;
		x = x & (x - 1);
	}
	return ret;
}
int main() {
	int T;
	freopen("B-large.in", "r", stdin);
	freopen("out1.txt", "w", stdout);
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++ cas) {
		scanf("%d%d", &n, &k);
		ans = 0;
		for (int i = 1; i <= n; ++ i) scanf("%lf", &p[i]);
		sort(p + 1, p + n + 1);
	/*
		for (int i = 1; i < (1 << n); ++ i) {
			if (count(i) != k) continue;
			lis.clear();
			lis.push_back(0);
			for (int j = 1; j <= n; ++ j) {
				if ((1 << (j - 1)) & i) {
					lis.push_back(j);
				}
			}
			//printf("%d\n", lis.size());
			*/
			for (int i = 1; i <= k + 1; ++ i) {
				lis.clear();
				lis.push_back(0);
				for (int j = 1; j <= n; ++ j) 
					if (j < i || j >= i + n - k) lis.push_back(j);
				ans = max(ans, dp());
			}
		
		printf("Case #%d: %f\n", cas, ans);
	}
	return 0;
}