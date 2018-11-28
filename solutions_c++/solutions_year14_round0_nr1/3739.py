#include <cstdio>

const int n = 4;

int a[10][10];
int b[10][10];
int x, y;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int qwe;
	scanf("%d", &qwe);
	for (int t = 1; t <= qwe; t++) {
		scanf("%d", &x);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				scanf("%d", &a[i][j]);
		scanf("%d", &y);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				scanf("%d", &b[i][j]);
		x--; y--;
		int cnt = 0, ans;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				if (a[x][i] == b[y][j]) {
					cnt++;
					ans = a[x][i];
				}
		printf("Case #%d: ", t);
		if (cnt == 1)
			printf("%d\n", ans);
		else
			if (!cnt)
				printf("Volunteer cheated!\n");
			else
				printf("Bad magician!\n");

	}
	return 0;
}
