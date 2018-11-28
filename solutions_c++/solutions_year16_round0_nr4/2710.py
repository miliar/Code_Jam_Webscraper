#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
	int T, K, S, C;
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		scanf("%d %d %d", &K, &C, &S);
		printf("Case #%d: ", i);
		if (S == K) {
			for (int j = 1; j <= S; ++j) 
				printf(" %d", j);
		}
		printf("\n");
	}
	return 0;
}

