#include <cstdio>
#include <cstring>
#include <iostream>
#define ROWS 4
#define COLS 4

char board[ROWS][COLS + 1];

void clearBoard() {
	for (int i = 0; i < ROWS; i++)
		for (int j = 0; j < COLS; j++)
			board[i][j] = '.';
}

void printBoard() {
	printf("\n");
	for (int i = 0; i < ROWS; i++) {

		for (int j = 0; j < COLS; j++) {
			printf("%c ", board[i][j]);
		}
		printf("\n");
	}
}

int countColumn(char t, int col) {
	int total = 0;
	for (int i = 0; i < ROWS; i++) {
		if (board[i][col] == t)
			total++;
	}
	return total;
}

int countRow(char t, int row) {
	int total = 0;
	for (int i = 0; i < COLS; i++) {
		if (board[row][i] == t)
			total++;
	}
	return total;
}
bool verifyColumn(char player, int col) {
	int total = 0;
	total += countColumn(player, col);
	total += countColumn('T', col);

	return total == 4;
}
bool verifyRow(char player, int row) {
	int total = 0;
	total += countRow(player, row);
	total += countRow('T', row);

	return total == 4;
}

bool verifyDiagonal(char t) {
	int total = 0;
	for (int i = 0; i < COLS; i++) {
		if ((board[i][i] == t) || (board[i][i] == 'T')) {
			total += 1;
		}
	}
	if (total == 4)
		return true;

	total = 0;

	for (int i = 0; i < COLS; i++) {
		if ((board[i][(COLS - 1) - i] == t)
				|| (board[i][(COLS - 1) - i] == 'T')) {
			total += 1;
		}
	}
	return (total == 4);
}
using namespace std;
int main() {

	int cases;
	char aux;
	char status;
	string line;

	while (scanf("%d", &cases) == 1) {

		for (int c = 1; c <= cases; c++) {

			for (int i = 0; i < ROWS; i++) {
				cin >> line;
				strcpy(board[i], line.c_str());
			}

			//printBoard();
			status = 'N';
			// ROWS
			for (int i = 0; i < ROWS && status == 'N'; ++i) {
				if (verifyRow('X', i)) {
					status = 'X';
					printf("Case #%d: X won\n", c);
				}
				if (verifyRow('O', i) && status == 'N') {
					status = 'O';
					printf("Case #%d: O won\n", c);
				}
			}
			// Columns
			for (int i = 0; i < COLS && status == 'N'; ++i) {
				if (verifyColumn('X', i)) {
					status = 'X';
					printf("Case #%d: X won\n", c);
				}
				if (verifyColumn('O', i) && status == 'N') {
					status = 'O';
					printf("Case #%d: O won\n", c);
				}
			}
			if (verifyDiagonal('X') && status == 'N') {
				printf("Case #%d: X won\n", c);
				status = 'X';
			}
			if (verifyDiagonal('O') && status == 'N') {
				status = 'O';
				printf("Case #%d: O won\n", c);
			}
			bool draw = false;
			for (int i = 0; i < ROWS && status == 'N'; ++i) {
				for (int j = 0; j < COLS; ++j) {
					if (board[i][j] == '.') {
						draw = true;
						break;
					}
				}
				if (draw)
					break;
			}
			if (draw && status == 'N') {
				printf("Case #%d: Game has not completed\n", c);
			} else if (status != 'X' && status != 'O') {
				printf("Case #%d: Draw\n", c);
			}
		}

	}
	return 0;
}
