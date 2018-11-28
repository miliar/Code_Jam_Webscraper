#include <stdio.h>
#include <stdlib.h>

int main() {
	int N, K;
	char S[1000];
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%s %d", &S, &K);
		bool b[1000];
		int len = 0;
		for (len = 0; len < 1000; len++) {
			if (S[len] == '+') {
				b[len] = true;
			} else if (S[len] == '-') {
				b[len] = false;
			} else {
				break;
			}
		}
		int count = 0;
		for (int j = 0; j <= len - K; j++) {
			if (!b[j]) {
				for (int k = 0; k < K; k++) {
					b[j + k] = !b[j + k];
				}
				count++;
			}
        }
		for (int j = len - K + 1; j < len; j++) {
			if (!b[j]) {
				printf("Case #%d: IMPOSSIBLE\n", i + 1);
				count = -1;
				break;
			}
		}
		if (count != -1) printf("Case #%d: %d\n", i + 1, count);
	}
	return 0;
}

