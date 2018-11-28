//By Lin
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <bitset>
#include <cmath>
#include <string>
#include <cstdlib>
#include <vector>
#include <queue>

#define X first
#define Y second
#define mp make_pair
#define sqr(x) ((x) * (x))
#define Rep(i, n) for(int i = 0; i<(n); i++)
#define foreach(it, n) for(__typeof(n.begin()) it = n.begin(); it != n.end(); it++)

using namespace std;
typedef long long LL;
typedef pair<int, int> pii;

#define esp 1e-8
#define N 210
#define MOD 1000000007

int n, K;
double p[N], pp[N];
long double dp[N][N];

double solve() {
	memset(dp, 0, sizeof dp);
	dp[0][0] = 1;
	Rep(i, K) {
		for (int k = 0; k <= i; k++) {
			dp[i + 1][k + 1] += dp[i][k] * pp[i];
			dp[i + 1][k] += dp[i][k] * (1 - pp[i]);
		}
	}
	return dp[K][K / 2];
}

int count(int msk) {
	int ret = 0;
	while (msk) {
		ret += msk & 1; 
		msk = msk / 2;
	}
	return ret;
}

int main() {
	int cas, tt = 0;
	cin >> cas;
	while (cas --) {
		scanf("%d%d", &n, &K);
		Rep(i, n) scanf("%lf", &p[i]);
		sort(p, p + n);
		double ans = 0;
		Rep(msk, 1<<n) {
			if (count(msk) == K) {	
				int k = 0;
				Rep(i, n) {
					if (msk & (1<<i)) pp[k++] = p[i];
				}
				ans = max(ans, solve());
			}
		}
		printf("Case #%d: %.12lf\n", ++tt, ans);
		// printf("Case #%d: %.12lf\n", ++tt, exp(dp[n][K]));

	}
	return 0;
}
