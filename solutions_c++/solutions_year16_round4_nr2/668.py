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
const int N = 25;

double a[N];
double dp[N][N];
vector<double> v;
int n, k, t, cas = 1;

double solve() {
	memset(dp, 0, sizeof dp);
	dp[0][0] = 1.0;
	for (int i = 0; i < k; i++) {
		for (int j = 0; j <= i; j++) {
			dp[i+1][j+1] += dp[i][j] * v[i];
			dp[i+1][j] += dp[i][j] * (1.0 - v[i]);
		}
	}
	return dp[k][k/2];
}
int main() {
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	while (t--) {
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i++) {
			scanf("%lf", a+i);
		}
		int mx = 1 << n;
		double ans = 0.0;
		for (int i = 0; i < mx; i++) {
			if (__builtin_popcount(i) != k) continue;
			v.clear();
			for (int j = 0; j < n; j++) {
				if (i & (1 << j)) v.push_back(a[j]);
			}
			ans = max(ans, solve());
		}
		printf("Case #%d: %.8f\n", cas++, ans);
	}
	return 0;
}
