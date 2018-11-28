#include <bits/stdc++.h>
using namespace std;

int main(void) {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		int K, C, S; scanf("%d%d%d", &K, &C, &S);
		printf("Case #%d:", i);
		if (K == S) {
			for (int j = 1; j <= K; j++)
				printf(" %d", j);
		}
		printf("\n");
	}
}
