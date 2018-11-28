#include <cstdio>
#include <algorithm>
double x[1000], y[1000];
int n;
void solve() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) scanf("%lf", &x[i]);
	for (int i = 0; i < n; i++) scanf("%lf", &y[i]);
	std::sort(x, x + n);
	std::sort(y, y + n);
	for (int i = 0; i <= n; i++) {
		int flag = 1;
		for (int j = 0; j < n-i; j++)
			if (x[i+j] < y[j]) flag = 0;
		if (flag) {
			printf("%d ", n-i);
			break;
		}
	}
	int cnt = 0;
	for (int i = 0, j = 0; i < n; i++) {
		while (j < n && y[j] < x[i]) j++;
		if (j == n) cnt++;
		else j++;
	}
	printf("%d\n", cnt);
}
int main() {
	int T; scanf("%d", &T);
	for (int _ = 1; _ <= T; _++)
		printf("Case #%d: ", _), solve();
	return 0;
}
