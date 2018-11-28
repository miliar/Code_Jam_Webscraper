#include <cstdio>
#include <algorithm>

using namespace std;

int const N = 2000 + 20;

int T, n, ans;
int p[N];

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++ t) {
		scanf("%d", &n);
		ans = 2147483647;
		int temp = 0;
		for (int i = 1; i <= n; ++ i) scanf("%d", &p[i]);
		for (int i = 1; i <= 1000; ++ i) {
			temp = 0;
			for (int j = 1; j <= n; ++ j) {
				temp += (p[j] - 1) / i;
			}
			ans = min(ans, i + temp);
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}


