#include <cstdio>

int ans[2];
int cards[2][4][4];

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		for (int i = 0; i < 2; i++) {
			scanf("%d", &ans[i]);
			for (int j = 0; j < 4; j++) {
				for (int k = 0; k < 4; k++) {
					scanf("%d", &cards[i][j][k]);
				}
			}
		}
		int column = -1;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (cards[0][ans[0] - 1][i] == cards[1][ans[1] - 1][j]) {
					if (column == -1) {
						column = cards[0][ans[0] - 1][i];
					} else {
						column = 0;
						i = 4;
						j = 4;
					}
				}
			}
		}
		printf("Case #%d: ", t);
		if (column == -1)
			printf("Volunteer cheated!\n");
		else if (column == 0)
			printf("Bad magician!\n");
		else
			printf("%d\n", column);
	}
	return 0;
}