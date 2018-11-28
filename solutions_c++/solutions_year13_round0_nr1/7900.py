/*
 * File name: qualification.cpp
 *
 * Author:  Maysoun Hindawi
 *          maysoun.h16@gmail.com
 *
 */

#include <iostream>

using namespace std;
#define N 4
typedef enum {
	NO_RESULT_YET = -1, DRAW = 0, X_WON = 1, O_WON = 2, NOT_COMPLETE = 3
} result;

void getMatrix(char matrix[][N]) {
	for (int row = 0; row < N; row++) {
		for (int col = 0; col < N; col++) {
			cin >> matrix[row][col];
		}
	}
}

result checkCompletion(char matrix[][N]) {
	for (int row = 0; row < N; row++) {
		for (int col = 0; col < N; col++) {
			if (matrix[row][col] == '.')
				return NOT_COMPLETE;
		}
	}
	return DRAW;
}

result checkColumns(char matrix[][N]) {
	for (int column = 0; column < N; column++) {
		char possible_winner;
		bool flag = true;
		if (matrix[0][column] == 'T')
			possible_winner = matrix[1][column];
		else
			possible_winner = matrix[0][column];

		for (int row = 1; row < N; row++) {
			if ((matrix[row][column] != possible_winner)
					&& (matrix[row][column] != 'T')) {
				flag = false;
				break;
			}
		}
		if (flag) {
			if (possible_winner == 'X')
				return X_WON;
			else if (possible_winner == 'O')
				return O_WON;
		}
	}
	return NO_RESULT_YET;
}
result checkRows(char matrix[][N]) {
	for (int row = 0; row < N; row++) {
		char possible_winner;
		bool flag = true;
		if (matrix[row][0] == 'T')
			possible_winner = matrix[row][1];
		else
			possible_winner = matrix[row][0];

		for (int col = 1; col < N; col++) {
			if ((matrix[row][col] != possible_winner) && (matrix[row][col]
					!= 'T')) {
				flag = false;
				break;
			}
		}
		if (flag) {
			if (possible_winner == 'X')
				return X_WON;
			else if (possible_winner == 'O')
				return O_WON;
		}
	}
	return NO_RESULT_YET;
}

result checkDiagonals(char matrix[][N]) {
	char possible_winner;
	bool flag = true;

	// main diagonal

	if (matrix[0][0] == 'T')
		possible_winner = matrix[1][1];
	else
		possible_winner = matrix[0][0];

	for (int i = 1; i < N; i++) {
		if ((matrix[i][i] != possible_winner) && (matrix[i][i] != 'T')) {
			flag = false;
			break;
		}
	}
	if (flag) {
		if (possible_winner == 'X')
			return X_WON;
		else if (possible_winner == 'O')
			return O_WON;
	}

	// second diagonal

	flag = true;
	if (matrix[0][3] == 'T')
		possible_winner = matrix[1][2];
	else
		possible_winner = matrix[0][3];

	for (int i = 1; i < N; i++) {
		if ((matrix[i][N - i - 1] != possible_winner) && (matrix[i][N - i - 1]
				!= 'T')) {
			flag = false;
			break;
		}
	}
	if (flag) {
		if (possible_winner == 'X')
			return X_WON;
		else if (possible_winner == 'O')
			return O_WON;
	}

	return NO_RESULT_YET;
}

result check(char matrix[][N]) {
	result res;
	res = checkRows(matrix);
	if (res == X_WON || res == O_WON) {
		return res;
	}
	res = checkColumns(matrix);
	if (res == X_WON || res == O_WON) {
		return res;
	}
	res = checkDiagonals(matrix);
	if (res == X_WON || res == O_WON) {
		return res;
	}
	return checkCompletion(matrix);
}
int main(int argc, char** argv) {
	char matrix[N][N];
	int length; // dataset length
	cin >> length;
	result *results = new result[length];

	for (int counter = 0; counter < length; counter++) {
		getMatrix(matrix);
		results[counter] = check(matrix);
		cin.get();
	}
	for (int counter = 0; counter < length; counter++) {
		cout << "Case #" << (counter + 1);
		switch (results[counter]) {
		case X_WON: {
			cout << ": X won";
			break;
		}
		case O_WON: {
			cout << ": O won";
			break;
		}
		case DRAW: {
			cout << ": Draw";
			break;
		}
		default: {
			cout << ": Game has not completed";
			break;
		}
		}
		cout << endl;
	}
	return 0;
}
