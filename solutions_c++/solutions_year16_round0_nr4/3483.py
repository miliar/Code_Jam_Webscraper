#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long int64;

#define MAX 120
int64 T;
int64 K, C, S;


int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%lld %lld %lld", &K, &C, &S);
		printf("Case #%d:", t);
		int64 K_C_1 = 1;
		for (int i = 0; i < C - 1; ++i) {
			K_C_1 *= K;
		}
		for (int i = 0; i < S; ++i) {
			printf(" %lld", i * K_C_1 + 1);
		}
		printf("\n");
	}
	return 0;
}