#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#define ll long long
using namespace std;

int main() {
	int T, K, C, S; scanf("%d", &T);
	for (int k = 1; k <= T; k++) {
		scanf("%d%d%d", &K, &C, &S);
		printf("Case #%d: ", k);
		
		if (K == 1 || (C == 1 && S == K)) {
			for (int j = 1; j <= K; j++) {
				printf("%d ", j);
			}
		}
		else if (C != 1 && S >= K-1) {
			for (int j = 2; j <= K; j++) {
				printf("%d ", j);
			}
		}
		else printf("IMPOSSIBLE");
		printf("\n");
	}
	return 0;
}