#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int T;
int n;
int p[1024];

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d: ", test);
		scanf("%d", &n);
		int M = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", p + i);
			M = max(M, p[i]);
		}
		int ans = M;
		for (int i = 1; i <= M; i++) {
			int sum = i;
			for (int j = 0; j < n; j++)
				sum += (p[j] - 1) / i;
			ans = min(ans, sum);
		}
		printf("%d\n", ans);
	}
	return 0;
}