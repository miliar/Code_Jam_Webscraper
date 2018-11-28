#include <string>
#include <iostream>
#include <cstdlib>

using namespace std;

const int SIZE = 4;
const char O = 'O';
const char X = 'X';
const char T = 'T';
const char EMPTY = '.';

void readInput();
void solveCase(int caseNum);
bool isDiagWin(char **board);
char **makeBoard();

int main() {
	readInput();
}

void readInput() {
	int numCases;
	cin >> numCases;
	for (int i = 0; i < numCases; i++) {
		solveCase(i + 1);
	}
}

void solveCase(int caseNum) {
	cout << "Case #" << caseNum << ": ";
	char **board = makeBoard();
	char start;
	bool complete = true;
	bool foundWin = true;
	if (board == NULL) {
		return;
	}

	for (int i = 0; i < SIZE; i++) {
		foundWin = true;
		if (board[0][i] == T) {
			start = board[1][i];
		} else {
			start = board[0][i];
		}
		for (int j = 0; j < SIZE; j++) {
			if (board[j][i] == EMPTY) {
				complete = false;
				foundWin = false;
			} else if (board[j][i] != T && board[j][i] != start) {
				foundWin = false;
			}
		}
		if (foundWin) {
			cout << start << " won\n";
			return;
		}
	}
	if (!isDiagWin(board)) {
		if (complete) {
			cout << "Draw\n";
		} else {
			cout << "Game has not completed\n";
		}
	}
}

bool isDiagWin(char **board) {
	char startLeft;
	char startRight;
	bool leftDiagWin = true;
	bool rightDiagWin = true;
	
	if (board[0][0] == T) {
		startLeft = board[1][1];
	} else {
		startLeft = board[0][0];
	}
	if (board[0][SIZE - 1] == T) {
		startRight = board[1][SIZE - 2];
	} else {
		startRight = board[0][SIZE - 1];
	}
	
	for (int i = 0; i < SIZE; i++) {
		if (board[i][i] != startLeft && board[i][i] != T) {
			leftDiagWin = false;
		}
		if (board[i][SIZE - i - 1] != startRight && board[i][SIZE - i - 1]
				!= T) {
			rightDiagWin = false;
		}
	}
	
	if (leftDiagWin && startLeft != EMPTY) {
		cout << startLeft << " won\n";
		return true;
	}
	if (rightDiagWin && startRight != EMPTY) {
		cout << startRight << " won\n";
		return true;
	}
	return false;
}

char **makeBoard() {
	string row;
	char **board = new char *[SIZE];
	bool horizWin = false;
	for (int i = 0; i < SIZE; i++) {
		board[i] = new char[SIZE];
		cin >> row;
		if (row == "XXXX" || row == "TXXX" || row == "XTXX" || row == "XXTX" ||
				row == "XXXT") {
			cout << "X won\n";
			horizWin = true;
		} else if (row == "OOOO" || row == "TOOO" || row == "OTOO" ||
				row == "OOTO" || row == "OOOT") {
			cout << "O won\n";
			horizWin = true;
		}
		for (unsigned int j = 0; j < row.length(); j++) {
			board[i][j] = row[j];
		}
	}
	if (horizWin) {
		return NULL;
	}
	return board;
}
