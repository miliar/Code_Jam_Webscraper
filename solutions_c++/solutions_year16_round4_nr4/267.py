#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int M = 5;
int dp[1<<M][1<<M], mask[M], n, t;

int pop(int x) {
	return __builtin_popcount(x);
}

void run(int t) {
	cout << "Case #" << t+1 << ": ";
	cin >> n;
	memset(mask, 0, sizeof(mask));
	for (int i = 0; i < n; ++i) {
		string g; cin >> g;
		for (int j = 0; j < n; ++j)
			if (g[j] == '1')
				mask[i] += (1<<j);
		// cout << mask[i] << endl;
	}

	for (int i = 0; i < (1<<n); ++i)
		for (int j = 0; j < (1<<n); ++j)
			dp[i][j] = n*n+5;

	dp[0][0] = 0;
	for (int i = 1; i < (1<<n); ++i)
		for (int j = 1; j < (1<<n); ++j) {
			if (pop(i) != pop(j))
				continue;
			for (int k = 1; k < (1<<n); ++k)
				for (int p = 1; p < (1<<n); ++p) {
					if ((k|i) != i)
						continue;
					if ((p|j) != j)
						continue;
					if (pop(k) != pop(p))
						continue;
					int sum = 0;
					bool y = true;
					for (int m = 0; m < n; ++m) {
						if ((k|(1<<m)) != k)
							continue;
						if ((mask[m]|p) != p)
							y = false;
						sum += pop(k)-pop(mask[m]);
					}

					if (y) {
						// cout << i << ' ' << j << ' ' << k << ' ' << p << endl;
						dp[i][j] = min(dp[i-k][j-p]+sum, dp[i][j]);
					}
				}
		}

	cout << dp[(1<<n)-1][(1<<n)-1] << endl;
}

int main() {
	cin >> t;
	for (int i = 0; i < t; ++i)
		run(i);
}
