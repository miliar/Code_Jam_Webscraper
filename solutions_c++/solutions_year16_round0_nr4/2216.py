#include<iostream>
#include<fstream>
#include<algorithm>
#include<unistd.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

using namespace std;

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int N, K, C, S, n, k;
	long long int start;
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		printf("Case #%d:", i+1);
		scanf("%d %d %d", &K, &C, &S);
		if (S <= K - C) {
			printf(" IMPOSSIBLE\n");
			continue;
		}
		n = K;
		start = 0;
		for (int j = 0; j < C - 1; ++j) {
			if (n <= S)
				break;
			if (n > 1)
				--n;
			start = start * K + K - n;
		}
		for (int j = 0; j < n; ++j) {
			printf(" %lld", start + j + 1);
		}
		printf("\n");
	}
	return 0;
}