#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int T;
int n;
int a[1024];
int ans1, ans2;

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d: ", test);
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", a + i);
		ans1 = ans2 = 0;
		int sp = 0;
		for (int i = 1; i < n; ++i)
			if (a[i] < a[i - 1])
				ans1 += a[i - 1] - a[i];
		for (int i = 1; i < n; ++i)
			if (a[i] < a[i - 1])
				sp = max(sp, a[i - 1] - a[i]);
		for (int i = 1; i < n; ++i) {
			int t = min(a[i - 1], sp);
			ans2 += t;
		}
		printf("%d %d\n", ans1, ans2);
	}
	return 0;
}