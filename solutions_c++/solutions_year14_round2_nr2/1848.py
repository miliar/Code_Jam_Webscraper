#include <cstdio>

using namespace std;

int main() {
	int T, A, B, K, c, i, j, res;
	scanf("%d", &T);
	c = 1;
	while (T--) {
		scanf("%d %d %d", &A, &B, &K);
		res = 0;
		for (i=0; i<A; i++) {
			for (j=0; j<B; j++) {
				if ((i & j) < K) res++;
			}
		}
		printf("Case #%d: %d\n", c++, res);
	}
	return 0;
}
