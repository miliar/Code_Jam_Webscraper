#include <cstdio>
int map1[10][10], map2[10][10], T, n, m;
void work()
{
	scanf("%d", &n);
	for (int i = 1; i <= 4; i++) {
		for (int j = 1; j <= 4; j++) {
			scanf("%d", &map1[i][j]);
		}
	}
	scanf("%d", &m);
	for (int i = 1; i <= 4; i++) {
		for (int j = 1; j <= 4; j++) {
			scanf("%d", &map2[i][j]);
		}
	}
	int cnt = 0, pos;
	for (int i = 1; i <= 4; i++) {
		for (int j = 1; j <= 4; j++) {
			if (map1[n][i] == map2[m][j]) {
				cnt++;
				pos = map1[n][i];
			}
		}
	}
	if (cnt == 0) {
		printf("Volunteer cheated!\n");
	} else if (cnt > 1) {
		printf("Bad magician!\n");
	} else {
		printf("%d\n", pos);
	}
}
int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		work();
	}
}
