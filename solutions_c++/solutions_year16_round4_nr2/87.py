#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
const int N(222);
double a[N], b[N], dp[N], dp1[N];
int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
		int n, k;
		scanf("%d%d", &n, &k);
		for(int i(0); i < n; i++) {
			scanf("%lf", &a[i]);
		}
		sort(a, a + n);
		double ans(0);
		for(int i(0); i <= k; i++) {
			for(int j(0); j <= i; j++) {
				b[j] = a[j];
			}
			for(int j(0); j <= k - i; j++) {
				b[i + j] = a[n - k + i + j];
			}
			dp[0] = 1;
			for(int j(1); j <= k; j++) {
				dp[j] = 0;
			}
			for(int j(0); j < k; j++) {
				for(int _(0); _ <= k; _++) {
					dp1[_] = dp[_] * (1 - b[j]) + (_ >= 1 ? dp[_ - 1] * b[j] : 0.);
				}
				for(int _(0); _ <= k; _++) {
					dp[_] = dp1[_];
				}
			}
			ans = max(ans, dp[k / 2]);
		}
		printf("Case #%d: %.10f\n", qq, ans);
	}
}
