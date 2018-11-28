#include <stdio.h>
int a[10][10];
int b[10][10];

int main()
{
	int T;
	scanf("%d", &T);
	int icase = 0;
	while (T--) {
		++icase;
		int r1, r2;
		scanf("%d", &r1);
		for (int i = 1; i <= 4; ++i) {
			for (int j = 1; j <= 4; ++j) {
				scanf("%d", &a[i][j]);
			}
		}
		scanf("%d", &r2);
		for (int i = 1; i <= 4; ++i) {
			for (int j = 1; j <= 4; ++j) {
				scanf("%d", &b[i][j]);
			}
		}
		int ans = 0;
		int x;
		for (int i = 1; i <= 4; ++i) {
			for (int j = 1; j <= 4; ++j) {
				if (a[r1][i] == b[r2][j]) {
					++ans;
					x = a[r1][i];
				}
			}
		}
		if (ans == 1) {
			printf("Case #%d: %d\n", icase, x);
		} else if (ans == 0) {
			printf("Case #%d: Volunteer cheated!\n", icase);
		} else printf("Case #%d: Bad magician!\n", icase);
	}
	return 0;
}
