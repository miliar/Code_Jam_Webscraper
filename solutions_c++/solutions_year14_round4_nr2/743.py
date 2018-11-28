#include <algorithm>
#include <cstdio>

using std::sort;

const int MaxN = 1111;

int T, N, a[MaxN], b[MaxN];

int main() {
	int cs = 0;
	freopen("B-large.in", "r", stdin);
	freopen("out", "w", stdout);
	scanf("%d", &T);
	while(T--) {
		scanf("%d", &N);
		for(int i = 1; i <= N; ++i) {
			scanf("%d", a + i);
			b[i] = a[i];
		}
		int ans = 0;
		while(N > 0) {
			int k = 1;
			for(int i = 2; i <= N; ++i) {
				if(a[i] < a[k]) {
					k = i;
				}
			}
			ans += k - 1 < N - k ? k - 1 : N - k;
			memcpy(a + k, a + k + 1, (sizeof (int)) * (N - k));
			--N;
		}
		printf("Case #%d: %d\n", ++cs, ans);
	}
	return 0;
}