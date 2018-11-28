#include <cstdio>
#include <algorithm>

using namespace std;

char s[32];
int a[32], b[32];

int main() {
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc, tcn;
	scanf("%d", &tcn);
	for (tc = 1; tc <= tcn; tc++) {
		int i, j, k, l, n, t, r = 999;
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%s", s);
			a[i] = 0;
			for (j = 0; j < n; j++) a[i] = (a[i] << 1) | (s[j] & 1);
		}
		for (k = 0; k < (1 << n * n); k++) {
			t = 0;
			for (i = 0; i < n; i++) {
				for (j = 0; j < n; j++) {
					if ((a[i] >> j & 1) && !(k >> (i * n + j) & 1)) break;
					if (!(a[i] >> j & 1) && (k >> (i * n + j) & 1)) t++;
				}
				if (j < n) break;
				b[i] = k >> (i * n) & ((1 << n) - 1);
			}
			if (i < n) continue;
			for (i = 0; i < n; i++) if (!b[i]) break;
			if (i < n) continue;
			for (i = 0; i < n; i++) {
				for (j = 0; j < n; j++) if ((b[i] & b[j]) && b[i] != b[j]) break;
				if (j < n) break;
			}
			if (i < n) continue;
			for (i = 0; i < n; i++) {
				l = 0;
				for (j = 0; j < n; j++) {
					if (b[i] == b[j]) l++;
					if (b[i] >> j & 1) l--;
				}
				if (l) break;
			}
			if (i < n) continue;
			r = min(r, t);
		}
		printf("Case #%d: %d\n", tc, r);
	}
}