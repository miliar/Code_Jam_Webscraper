#include <bits/stdc++.h>

using namespace std;

int able[33][33];
int table[33][33];

int N = 0;
int order[33];
bool op[33];
bool dfs(int cur)
{
	bool result = true;
	if (cur == N) {
		for(int i = 0;i < N;i++) result &= op[i];
		return result;
	}

	int cnt = 0;
	for (int i = 0;i < N;i++) {
		if (!op[i] && table[order[cur]][i]) {
			op[i] = true;
			result &= dfs(cur + 1);
			op[i] = false;
			cnt++;
		}
	}
	return result && cnt;
}

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", ++TK);

		scanf("%d", &N);

		for (int i = 0;i < N;i++) {
			for (int j = 0;j < N;j++) {
				scanf("%1d",&able[i][j]);
			}
		}

		int ans = N*N;
		for (int msk = 0;msk < (1 << (N*N));msk++)
		{
			if (__builtin_popcount(msk) >= ans) continue;

			memcpy(table, able, sizeof(able));
			for (int i = 0;i < N;i++) {
				for (int j = 0;j < N;j++) {
					if (msk & (1 << (i * N + j))) {
						table[i][j] = 1;
					}
				}
			}

			for (int t = 0;t < N;t++) order[t] = t;

			bool okay = true;
			do {
				memset(op, 0, sizeof(op));
				okay &= dfs(0);
			} while (next_permutation(order, order + N));
			if (okay) ans = min(ans, __builtin_popcount(msk));
		}
		printf("%d\n", ans);
	}
	return 0;
}