#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAX_N = 1007;

int n;
int a[MAX_N];

int main() {
	int T;
	scanf("%d", &T);
	int cas = 0;
	while (T-- > 0) {
		scanf("%d", &n);
		int limit = 0;
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]), limit = max(limit, a[i]);
		int ans = limit;
		for (int i = 1; i <= limit; ++i) {
			int now = i;
			for (int j = 0; j < n; ++j) {
				now += (a[j] - 1) / i;
			}
			ans = min(ans, now);
		}
		printf("Case #%d: %d\n", ++cas, ans);

	}
	return 0;
}
