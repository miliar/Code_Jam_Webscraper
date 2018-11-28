/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;

int ans[55][55];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, K = 1;
	scanf("%d", &T);
	while (T--) {
		int n, i, j;
		long long m;
		scanf("%d %lld", &n, &m);

		memset(ans, 0, sizeof ans);

		long long f[55] = {};
		f[1] = 1;

		for (i = 2; i <= n; ++i) {
			long long sum = 0;
			for (j = 1; j < i; ++j) sum += f[j];
			f[i] = sum;
			if (sum >= m) break;
		}

		if (i > n) {
			printf("Case #%d: IMPOSSIBLE\n", K);
			++K;
			continue;
		}

		while (f[i] > m) {
			for (j = i - 1; j > 1; --j) {
				if (f[j] > f[j - 1]) {
					if (f[j] - f[j - 1] < f[i] - m) {
						f[i] -= f[j] - f[j - 1];
						f[j] = f[j - 1];
					} else {
						f[j] -= f[i] - m;
						f[i] = m;
						break;
					}
				}
			}
		}

		for (j = 1; j < i; ++j) ans[j][n] = 1;

		for (i = i - 1; i > 1; --i) {
			long long cnt = f[i];
			for (j = i - 1; j >= 1; --j) {
				if (cnt >= f[j]) {
					cnt -= f[j];
					ans[j][i] = 1;
				}
			}
			if (cnt != 0) assert(false);
		}

		printf("Case #%d: POSSIBLE\n", K);
		++K;
		for (i = 1; i <= n; ++i) {
			for (j = 1; j <= n; ++j) {
				printf("%d", ans[i][j]);
			}
			puts("");
		}
	}
	return 0;
}
