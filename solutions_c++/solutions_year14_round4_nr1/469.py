#include <cstdio>
#include <algorithm>
using namespace std;

int T, n, X, a[11000];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d%d", &n, &X);
		for (int i = 1; i <= n; i++)	scanf("%d", &a[i]);
		sort(a + 1, a + n + 1);
		int q = 1;
		for (int i = n; i > q; i--)
			if (a[i] + a[q] <= X)	q++;
		printf("Case #%d: %d\n", t, n - q + 1);
	}
}
