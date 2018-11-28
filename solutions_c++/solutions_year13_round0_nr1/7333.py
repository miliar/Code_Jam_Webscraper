#include <cstdio>

int main() {

	int t;
	scanf("%d\n", &t);

	for (int testCase = 1; testCase <= t; ++testCase) {

		char table[4][5];
		for (int i = 0; i < 4; ++i) {
			scanf("%s\n", table[i]);
		}

		bool gameEnded = true;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (table[i][j] == '.') {
					gameEnded = false;
					i = j = 4;
				}
			}
		}

		bool oWon = false;
		bool xWon = false;

		int oRow[4] = { 0, 0, 0, 0 };
		int oCol[4] = { 0, 0, 0, 0 };
		int oDia[2] = { 0, 0 };

		int xRow[4] = { 0, 0, 0, 0 };
		int xCol[4] = { 0, 0, 0, 0 };
		int xDia[2] = { 0, 0 };

		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				int dia = -1;
				if (i == j) {
					dia = 0;
				}
				else
				if (i + j == 3) {
					dia = 1;
				}

				if (table[i][j] != '.' && table[i][j] != 'X') {
					++oRow[i];
					++oCol[j];

					if (dia >= 0) {
						++oDia[dia];
					}
				}

				if (table[i][j] != '.' && table[i][j] != 'O') {
					++xRow[i];
					++xCol[j];

					if (dia >= 0) {
						++xDia[dia];
					}
				}
			}
		}

		for (int i = 0; i < 4; ++i) {
			if (oRow[i] == 4 || oCol[i] == 4) {
				oWon = true;
			}

			if (xRow[i] == 4 || xCol[i] == 4) {
				xWon = true;
			}
		}

		for (int i = 0; i < 2; ++i) {
			if (oDia[i] == 4) {
				oWon = true;
			}

			if (xDia[i] == 4) {
				xWon = true;
			}
		}

		if (!(oWon || xWon)) {
			if (gameEnded) {
				printf("Case #%d: Draw\n", testCase);
			}
			else {
				printf("Case #%d: Game has not completed\n", testCase);
			}
		}
		else
		if (oWon) {
			printf("Case #%d: O won\n", testCase);
		}
		else {
			printf("Case #%d: X won\n", testCase);
		}
	}

	return 0;
}
