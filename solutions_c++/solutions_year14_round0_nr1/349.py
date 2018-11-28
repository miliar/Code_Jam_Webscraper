#include <cstdio>
int a[4][4], b[4][4], x, y;
void solve() {
	scanf("%d", &x); x--;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			scanf("%d", &a[i][j]);
	scanf("%d", &y); y--;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			scanf("%d", &b[i][j]);
	int cnt = 0, ans = -1;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (a[x][i] == b[y][j])
				ans = a[x][i], cnt++;
	if (cnt == 0) puts("Volunteer cheated!");
	else if (cnt > 1) puts("Bad magician!");
	else printf("%d\n", ans);
}
int main() {
	int T; scanf("%d", &T);
	for (int _ = 1; _ <= T; _++)
		printf("Case #%d: ", _), solve();
	return 0;
}
