#include <iostream>
#include <cmath>
using namespace std;
int T, K, C, S;
int main() {
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cin >> K >> C >> S;
		printf("Case #%d:", t);
		if (S == K) {
			for (int i = 1; i <= K; ++i)
				printf(" %d", i);
			printf("\n");
			continue;
		}
		if (K > C * S) printf(" IMPOSSIBLE\n");
		else {
			for (int i = 0; i < K; i += C) {
				long long cur = 0L;
				for (int j = 0; j < C && (i + j) < K; ++j) {
					cur += (i + j) * (long long) pow(K, C - 1 - j);
				}
				printf(" %lld", cur + 1);
			}
			printf("\n");
		}
	}
	return 0;
}