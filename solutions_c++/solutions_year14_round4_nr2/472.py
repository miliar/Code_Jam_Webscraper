#include <cstdio>
#include <algorithm>
using namespace std;

int T, n, a[1100];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d", &n);
		for (int i = 1; i <= n; i++)	scanf("%d", &a[i]);
		int ans = 0;
		for (int i = 1; i <= n; i++) {
			int t1 = 0, t2 = 0;
			for (int j = 1; j < i; j++)	if (a[j] > a[i])	t1++;
			for (int j = i + 1; j <= n; j++)	if (a[j] > a[i])	t2++;
			ans += min(t1, t2);
		}
		printf("Case #%d: %d\n", t, ans);
	}
}
