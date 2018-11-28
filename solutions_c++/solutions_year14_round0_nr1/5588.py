#include <stdio.h>

int main(int argc, char** argv) {
	int T;
	scanf("%d%*c", &T);
	int matching, answerone, answertwo;
	int squareone[16];
	int squaretwo[16];
	int matches[4];
	for (int i = 0; i < T; ++i) {
		matching = 0;
		scanf("%d", &answerone);
		answerone--;
		for (int j = 0; j < 4; ++j) {
			scanf("%d %d %d %d", &squareone[j * 4], &squareone[j * 4 + 1], &squareone[j * 4] + 2, &squareone[j * 4] + 3);
		}
		scanf("%d", &answertwo);
		answertwo--;
		for (int j = 0; j < 4; ++j) {
			scanf("%d %d %d %d", &squaretwo[j * 4], &squaretwo[j * 4 + 1], &squaretwo[j * 4 + 2], &squaretwo[j * 4 + 3]);
		}
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				if (squareone[answerone * 4 + j] == squaretwo[answertwo * 4 + k])
					matches[matching++] = squareone[answerone * 4 + j];
			}
		}
		if (matching == 0) {
			printf("Case #%d: Volunteer cheated!\n", i+1);
		}
		else if (matching == 1) {
			printf("Case #%d: %d\n", i+1, matches[0]);
		}
		else {
			printf("Case #%d: Bad magician!\n", i + 1);
		}
	}
}