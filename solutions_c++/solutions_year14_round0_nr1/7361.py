#include <stdio.h>

int layout[4][4];

void read(int *row) {
	scanf("%i", row);
	(*row)--;
	for (int y = 0; y < 4; y++) {
		for (int x = 0; x < 4; x++) {
			scanf("%i", &(layout[x][y]));
			layout[x][y]--;
		}
	}
}
void doCase(int i) {
	bool plausible[16];
	int row;
	read(&row);
	for (int r = 0; r < 4; r++) {
		for (int c = 0; c < 4; c++) {
			plausible[layout[c][r]] = r == row;
		}
	}
	read(&row);
	for (int r = 0; r < 4; r++) {
		for (int c = 0; c < 4; c++) {
			plausible[layout[c][r]] = plausible[layout[c][r]] && r == row;
		}
	}
	int res = -1;
	for (int j = 0; j < 16; j++) {
		if (plausible[j]) {
			if (res == -1) {
				res = j;
			}
			else {
				res = -2;
			}
		}
	}
	switch (res) {
		case -2:
			printf("Case #%i: Bad magician!\n", i + 1);
		break;
		case -1:
			printf("Case #%i: Volunteer cheated!\n", i + 1);
		break;
		default:
			printf("Case #%i: %i\n", i + 1, res + 1);
		break;
	}
}
int main() {
	int nCases;
	scanf("%i", &nCases);
	for (int i = 0; i < nCases; i++) {
		doCase(i);
	}
	return 0;
}
