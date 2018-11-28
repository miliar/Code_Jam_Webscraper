#include <stdio.h>

int main() {
	int n, ans[2], cards[2][4][4];
	FILE *in = fopen("A-small-attempt1.in", "r");
	FILE *out = fopen("out.txt", "w");
	fscanf(in, "%d", &n);

	for (int i = 0; i < n; i++) {

		for (int j = 0; j < 2; j++) {
			fscanf(in, "%d", &ans[j]);
			for (int k = 0; k < 4; k++) {
				for (int l = 0; l < 4; l++) {
					fscanf(in, "%d", &cards[j][k][l]);
				}
			}
			ans[j]--;
		}

		int card = -1;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (cards[0][ans[0]][j] == cards[1][ans[1]][k]) {
					if (card == -1) {
						card = cards[0][ans[0]][j];
					}
					else if (card != -1) {
						card = -2;
						goto end;
					}
				}
			}
		}

end:
		if (card == -1) {
			fprintf(out, "Case #%d: Volunteer cheated!\n", i + 1);
		}
		else if (card == -2) {
			fprintf(out, "Case #%d: Bad magician!\n", i + 1);
		}
		else {
			fprintf(out, "Case #%d: %d\n", i + 1, card);
		}

	}

	return 0;
}