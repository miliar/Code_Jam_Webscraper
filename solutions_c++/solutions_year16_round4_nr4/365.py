#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;

int main() {
	int T;
	cin >> T;
	bool dp[1 << 4][1 << 4] = { };
	for (int nc = 1; nc <= T; ++nc) {
		int N;
		cin >> N;
		bool can[5][5];
		bool newcan[5][5];
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				char c;
				while (c = getchar(), c < '0' || c > '1')
					;
				can[i][j] = c - '0';
			}
		}

		int ans = N * N;
		for (int mask = 0; mask < 1 << (N * N); ++mask) {
			bool ok = true;
			int cnt = 0;
			for (int i = 0; i < N; ++i) {
				for (int j = 0; j < N; ++j) {
					if (can[i][j] && (~mask >> (i * N + j) & 1)) {
						ok = false;
						goto end;
					}
					newcan[i][j] = mask >> (i * N + j) & 1;
					if (newcan[i][j] && !can[i][j]) {
						++cnt;
					}
				}
			}
			if (!ok || cnt >= ans)
				continue;

			memset(dp, 0, sizeof dp);
			dp[(1 << N) - 1][(1 << N) - 1] = true;

			for (int pset = (1 << N) - 1; pset >= 0; --pset) {
				for (int mset = (1 << N) - 1; mset >= 0; --mset) {
					if (dp[pset][mset]) {
						for (int i = 0; i < N; ++i) {
							if (pset >> i & 1) {
								bool flag = false;
								for (int j = 0; j < N; ++j) {
									if (newcan[i][j] && mset >> j & 1) {
										dp[pset - (1 << i)][mset - (1 << j)] =
												true;
										flag = true;
									}
								}
								if (!flag) {
									ok = false;
									goto end;
								}
							}
						}
					}
				}
			}

			ans = min(ans, cnt);

			end: {
			}
		}

		printf("Case #%d: %d\n", nc, ans);
	}
}
