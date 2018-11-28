#include <cstdio>
#include <cstring>

int cnt[17];
int mat[4][4];

int main() {
	int T;
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ca++) {
		memset(cnt, 0, sizeof(cnt));
		for (int run = 0; run < 2; run++) {
			int a;
			scanf("%d", &a);
			a--;
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					scanf("%d", &mat[i][j]);
				}
			}
			for (int i = 0; i < 4; i++) {
				cnt[ mat[a][i] ]++;
			}
		}
		int x = 0, y = 0;
		for (int i = 1; i <= 16; i++) {
			if (cnt[i] == 2) {
				x++;
				y = i;
			}
		}
		printf("Case #%d: ", ca);
		if (x == 1) {
			printf("%d\n", y);
		} else if (x > 1) {
			printf("Bad magician!\n");
		} else {
			printf("Volunteer cheated!\n");
		}
	}
	return 0;
}
