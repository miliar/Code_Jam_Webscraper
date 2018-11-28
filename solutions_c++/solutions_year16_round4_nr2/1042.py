#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

const int N = (int) 2e3;

int n, k;
ld dp[N][N], p[N];


void solve(int test) {
	cin >> n >> k;
	for (int i = 1; i <= n; ++i) {
		cin >> p[i];
	}
	cout << "Case #" << test << ": ";
	ld ans = 0;
	for (int mask = 0; mask < (1 << n); ++mask) {
		int cnt = 0;
		for (int i = 0; i < n; ++i) {
			if (((1 << i) & mask) != 0) ++cnt;
		}
		if (cnt != k) continue;
		for (int i = 0; i <= k; ++i) {
			for (int j = 0; j <= k/2; ++j) {
				dp[i][j] = 0;
			}
		}
		dp[0][0] = 1;
		int pt = 0;
		for (int i = 0; i < n; ++i) {
			if (((1 << i) & mask) == 0) continue;
			for (int j = 0; j <= k/2; ++j) {
				dp[pt+1][j+1] += dp[pt][j] * p[i+1];
				dp[pt+1][j] += dp[pt][j] * (1 - p[i+1]);
			}
			++pt;
		}
		ans = max(ans, dp[pt][k/2]);
	}
	cout << fixed << setprecision(10) << ans << '\n';
}


int main()
{
	ios_base::sync_with_stdio(0);
#ifdef KOBRA
	freopen("testor", "r", stdin);
	freopen("output", "w", stdout);
#else
//	freopen("minimization.in", "r", stdin);
//	freopen("minimization.out", "w", stdout);
#endif // KOBRA
	int cases;
	cin >> cases;
	for (int i = 1; i <= cases; ++i) {
		solve(i);
	}
	return 0;
}

