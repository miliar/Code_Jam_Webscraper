#include <cstdio>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		int K, C, S;
		scanf("%d%d%d", &K, &C, &S);
		printf("Case #%d:", tc);
		long long KC = 1;
		for (int i = 1; i < C; i++) {
			KC *= K;
		}
		for (long long j = 1; j <= KC*K; j+=KC) {
			printf(" %lld", j);
		}
		puts("");
	}
	return 0;
}