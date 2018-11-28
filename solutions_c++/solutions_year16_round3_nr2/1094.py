#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;

typedef long long lld;
int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d", &T);

	for (int TestCase = 1; TestCase <= T; TestCase++) {
		int B;
		lld M;
		int adj[51][51] = { 0, };
		scanf("%d %lld", &B, &M);

		for (int i = 1; i <= B; i++) {
			for (int j = i + 1; j <= B; j++) {
				adj[i][j] = 1;
			}
		}

		printf("Case #%d: ", TestCase);

		if (M > (1 << (B - 2))) {
			printf("IMPOSSIBLE\n");
		}
		else {
			printf("POSSIBLE\n");
			lld diff = (1 << (B - 2)) - M;

			int t = 2;
			while (diff > 0) {
				if (diff % 2 == 1) {
					adj[t][B] = 0;
				}
				diff >>= 1;
				t++;
			}

			for (int i = 1; i <= B; i++) {
				for (int j = 1; j <= B; j++) {
					printf("%d", adj[i][j]);
				}
				printf("\n");
			}
		}

	}


	return 0;
}