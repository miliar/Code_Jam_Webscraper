#include <bits/stdc++.h>
using namespace std;

int a[11][11][11];

typedef pair<int, int> pii;

map<pii, int> cnt[3];

int main(void) {

	int cases; scanf("%d", &cases);

	int cas = 0;
	while (cases--) {
		printf("Case #%d: ", ++cas);

		int X, Y, Z; scanf("%d %d %d", &X, &Y, &Z);
		int K; scanf("%d", &K);

		for (int i = 0; i < 3; ++i) cnt[i].clear();

		printf("%d\n", min(K, Z) * X * Y);
		for (int i = 0; i < X; ++i)
		for (int j = 0; j < Y; ++j)
		for (int k = 0; k < min(K, Z); ++k) {
			printf("%d %d %d\n", i+1, j+1, (i+j+k) % Z+1);
			cnt[0][pii(i+1, j+1)]++;
			cnt[1][pii(i+1, (i+j+k)%Z+1)]++;
			cnt[2][pii(j+1, (i+j+k)%Z+1)]++;
		}
		for (int i = 0; i < 3; ++i)
			for (auto x : cnt[i]) {
				assert(x.second <= K);
			}
	}

	return 0;
}