#include <cstdio>
#include <algorithm>
using namespace std;

int i, j, k, a[100000], b[100000], tn, ti, n, ps[100000], pos, f[100000], f1, f2;

int main () {
	freopen("input.txt", "r", stdin);
	scanf("%d", &tn);
	for(ti = 1; ti <= tn; ti++) {
		scanf("%d", &n);
		for(i = 1; i <= n; i++) {
			scanf("%d", &a[i]);
			b[i] = a[i];
		}
		sort(b + 1, b + n + 1);
		for(i = 1; i <= n; i++) a[i] = lower_bound(b + 1, b + n + 1, a[i]) - b;
		for(i = 1; i <= n; i++) {
			for(j = 1; j <= n; j++) if (a[j] == n - i + 1) pos = j;
			ps[i] = pos;
			if (i == 1) {
				f[i] = 0;
				continue;
			}
			f1 = f2 = 0;
			for(j = 1; j < i; j++) if (pos > ps[j]) ++f1;
			for(j = 1; j < i; j++) if (pos < ps[j]) ++f2;
			f[i] = f[i - 1] + min(f1, f2);
		}
		printf("Case #%d: %d\n", ti, f[n]);
	}
	return 0;
}