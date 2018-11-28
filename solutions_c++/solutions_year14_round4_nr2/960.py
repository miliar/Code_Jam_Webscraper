#include <cstdio>

int casei, cases, n;
int a[10000];

int main() {
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) scanf("%d", a + i);
		int l = 0, r = n - 1, ans = 0;
		
		while (l < r) {
			int m = l;
			for (int i = l + 1; i <= r; ++i) if (a[i] < a[m]) m = i;
			
			if (m - l < r - m) {
				ans += m - l;
				int t = a[m];
				for (int i = m; i > l; --i) a[i] = a[i - 1];
				a[l] = t;
				++l;
			}
			else {
				ans += r - m;
				int t = a[m];
				for (int i = m; i < r; ++i) a[i] = a[i + 1];
				a[r] = t;
				--r;
			}
		}
		
		//for (int i = 0; i < n; ++i) printf("%d ", a[i]);
		//printf("\n");
		
		printf("Case #%d: %d\n", casei, ans);
	}

	return 0;
}
