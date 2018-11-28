#include <iostream>
#include <string>
#include <sstream>
#include <stdio.h>
#define COLS 4
#define ROWS 4

using namespace std;

string magicTrick(int answer1, int matrix1[][4], int answer2, int matrix2[][4]);
void insertIntoMatrix(int p[][COLS], int r, int c, int i);

int main() {
	int tt, t, i, j, n, matrix1[ROWS][COLS], matrix2[ROWS][COLS], currentRow = 0, currentCol = 0, matrix = 0;
	int answer1, answer2;
	char *line;
	freopen( "A-small-attempt1.in", "r", stdin );
	freopen( "output.out", "w", stdout );
	scanf( "%d\n", &tt );
	for(t = 1; t <= tt; t++) {
		scanf("%d\n", &answer1);
		for(i = 0; i < ROWS; i++) {
			for(j = 0; j < COLS; j++) {
				scanf("%d", &n);
				insertIntoMatrix(matrix1, i, j, n);
			}
		}
		scanf("%d\n", &answer2);
		for(i = 0; i < ROWS; i++) {
			for(j = 0; j < COLS; j++) {
				scanf("%d", &n);
				insertIntoMatrix(matrix2, i, j, n);
			}
		}
		cout << (t > 1 ? "\n" : "") << "Case #" << t << ": " + magicTrick(answer1, matrix1, answer2, matrix2);
	}
}

void insertIntoMatrix(int p[][COLS], int r, int c, int i) {
	p[r][c] = i;
}

string magicTrick(int answer1, int matrix1[][4], int answer2, int matrix2[][4]) {
	int *firstSelectedRow, i, j, flag = 0, coincidences, coincidence;
	char *res;
	std::stringstream out;

	firstSelectedRow = matrix1[answer1-1];
	coincidences = 0;
	for(i = 0; i < 4; i++) {
		for(j = 0; j < 4; j++) {
			if(matrix2[answer2-1][i] == firstSelectedRow[j]) {
				coincidence = matrix2[answer2-1][i];
				coincidences ++;
			}
		}
	}
	if(coincidences == 1) {
		out << coincidence;
		return out.str();
	} else if(coincidences > 1) {
		return "Bad magician!";
	} else {
		return "Volunteer cheated!";
	}
}