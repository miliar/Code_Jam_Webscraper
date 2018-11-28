#include <bits/stdc++.h>
using namespace std;

int B;
long long M;

int MAP[55][55];

long long f[55];

int main(void) {


	int cases; scanf("%d", &cases);

	int cas = 0;
	while (cases--) {
		printf("Case #%d: ", ++cas);

		scanf("%d %lld", &B, &M);

		memset(MAP, 0, sizeof MAP);

		if (M > (1ll<<(B-2))) {
			puts("IMPOSSIBLE");
			continue;
		}
		puts("POSSIBLE");
		for (int i = 2; i <= B-1; ++i) {
			for (int j = 1; j < i; ++j) {
				MAP[j][i] = 1;
			}
		}

		int len = 0;
		long long ans = M;
		if (M == (1ll << (B-2))) {
			for (int i = 1; i < B; ++i) MAP[i][B] = 1;
			M = 0;
		}
		while (M) {
			if (M & 1) {
				MAP[len+2][B] = 1;
			}
			M >>= 1;
			len++;
		}
		for (int i = 1; i <= B; ++i) {
			for (int j = 1; j <= B; ++j) {
				putchar('0' + MAP[i][j]);
			}
			puts("");
		}


		memset(f, 0, sizeof f);
		f[1] = 1;
		for (int i = 2; i <= B; ++i) {
			for (int j = 1; j < i; ++j) if (MAP[j][i]) {
				f[i] += f[j];
			}
		}
		assert(f[B] == ans);

	}

	return 0;
}