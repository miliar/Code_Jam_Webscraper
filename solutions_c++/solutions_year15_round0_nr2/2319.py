#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
using namespace std;

int T, D;
int P[1024];

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		scanf("%d", &D);

		int ans = 0, maxval = 0;
		for (int i = 1; i <= D; i++) {
			scanf("%d", P + i);
			maxval = max(maxval, P[i]);
		}

		ans = maxval;
		for (int i = 1; i <= maxval; i++) {
			int cnt = 0;
			for (int k = 1; k <= D; k++) {
				cnt += (P[k] + i - 1) / i - 1;
			}
			ans = min(ans, cnt + i);
		}

		printf("Case #%d: %d\n", test, ans);
	}

	return 0;
}
