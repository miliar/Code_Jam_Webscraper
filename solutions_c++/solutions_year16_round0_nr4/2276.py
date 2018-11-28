#include <stdio.h>

int main() {
	int T;
	scanf("%d", &T);

	for (int tt = 1; tt <= T; tt++) {
		int K, C, S;
		scanf("%d %d %d", &K, &C, &S);

		printf("Case #%d: ", tt);
		for (int i = 1; i <= K; i++) {
			printf("%d ", i);
		}
		printf("\n");
	}
}