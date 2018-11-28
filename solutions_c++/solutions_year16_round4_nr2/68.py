#include <cstdio>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <algorithm>

using namespace std;


const int N = 18;
double p[N], q[N], dp[N][N];
int cnt[1<<N];

double calc(int n) {
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1.0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j <= i; j++) {
			dp[i+1][j] += dp[i][j] * (1-q[i]);
			dp[i+1][j+1] += dp[i][j] * q[i];
		}
	return dp[n][n/2];
}

void run(int cas) {
	int n, k;
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; i++)
		scanf("%lf", &p[i]);
	cnt[0] = 0;
	for (int i = 1; i < (1 << n); i++)
		cnt[i] = cnt[i >> 1] + (i & 1);
	double ans = 0;
	for (int i = 0; i < (1 << n); i++)
		if (cnt[i] == k) {
			int t = 0;
			for (int j = 0; j < n; j++)
				if (1 & (i >> j))
					q[t++] = p[j];
			double cur = calc(k);
			ans = max(ans, cur);
		}
	printf("Case #%d: %.8f\n", cas, ans);
}

int main() {
    int tt, cas;
    scanf("%d", &tt);
    for (cas = 1; cas <= tt; cas++)
        run(cas);
    return 0;
}

