#include <cstdio>
#include <iostream>
using namespace std;

long long K, C, S;

int main() {
	int testcase;
	scanf("%d", &testcase);

	for (int i = 1; i <= testcase; i++) {
		scanf("%lld %lld %lld", &K, &C, &S);
		long long tokenSize = 1;

		for (int j = 1; j < C; j++) tokenSize *= K;

		printf("Case #%d: ", i);

		for (int j = 1; j <= K; j++) {
			printf("%lld ", tokenSize * (j - 1) + 1);
		}

		puts("");
	}

	return 0;
}