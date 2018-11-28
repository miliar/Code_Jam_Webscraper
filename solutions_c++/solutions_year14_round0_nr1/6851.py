#include <cstdio>
void solve() {
	int an, bn, a[5][5], b[5][5], ans = 0;
	scanf("%d", &an);
	for (int i = 1 ; i <= 4 ; ++i)
		for (int j = 1 ; j <= 4 ; ++j)
			scanf("%d", &a[i][j]);
	scanf("%d", &bn);
	for (int i = 1 ; i <= 4 ; ++i)
		for (int j = 1 ; j <= 4 ; ++j)
			scanf("%d", &b[i][j]);
	for (int i = 1 ; i <= 4 ; ++i)
		for (int j = 1 ; j <= 4 ; ++j)
			if (a[an][i] == b[bn][j]) {
				if (ans == 0) ans = a[an][i];
				else ans = -1;
			}
	if (ans == 0) puts("Volunteer cheated!");
	else if (ans == -1) puts("Bad magician!");
	else printf("%d\n", ans);
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1 ; i <= t ; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
