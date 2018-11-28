#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
using namespace std;

typedef long long lld;
int main() {
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int T;
	scanf("%d", &T);

	for (int TestCase = 1; TestCase <= T; TestCase++) {
		int K, C, S;
		scanf("%d %d %d", &K, &C, &S);

		printf("Case #%d:", TestCase);

		for (int i = 1; i <= K; i++) {
			printf(" %d", i);
		}
		printf("\n");
	}
	return 0;
}