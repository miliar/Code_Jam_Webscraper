#include <cstdio>

int main() {
	int T;
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ca++) {
		int A, B, K;
		scanf("%d%d%d", &A, &B, &K);
		int cnt = 0;
		for (int i = 0; i < A; i++) {
			for (int j = 0; j < B; j++) {
				int t = i & j;
				if (t >= 0 && t < K) cnt++;
			}
		}
		printf("Case #%d: %d\n", ca, cnt);
	}
	return 0;
}
