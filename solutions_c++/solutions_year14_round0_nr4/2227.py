#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1010;

double a[MAXN], b[MAXN]; int n;

inline int Make(double a[], double b[]) {
	int last = 0;
	for (int k = 0; k <= n; k++) {
		int ok = 1;
		for (int i = 1, j = n - k + 1; i <= k; i++, j++) ok &= a[j] > b[i];
		if (ok) last = k;
	}
	return last;
}

int main(void) {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int kase; scanf("%d", &kase); for (int _ = 1; _ <= kase; _++) {
		scanf("%d", &n); 
		for (int i = 1; i <= n; i++) scanf("%lf", a + i);
		for (int i = 1; i <= n; i++) scanf("%lf", b + i);
		sort(a + 1, a + n + 1);
		sort(b + 1, b + n + 1);
		printf("Case #%d: %d %d\n", _, Make(a, b), n - Make(b, a));
	}
	return 0;
}

