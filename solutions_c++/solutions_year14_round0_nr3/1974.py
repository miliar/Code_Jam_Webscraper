#include <iostream>
#include <cstring>
using namespace std;

char board[10][10];
char board2[10][10];
int T, R, C, M;

bool valid(int x, int y) {
	return x >= 0 && y >= 0 && x < R && y < C;
}

int reveal(int r, int c) {
	if (board2[r][c] != '.') return 0;
	int result = 1;
	board2[r][c] = 'X';
	bool number = false;
	for (int i = -1; i <= 1; i++) {
		for (int j = -1; j <= 1; j++) {
			int x = r + i;
			int y = c + j;
			if (valid(x, y) && board2[x][y] == '*') number = true;
		}
	}
	if (!number) {
		for (int i = -1; i <= 1; i++) {
			for (int j = -1; j <= 1; j++) {
				int x = r + i;
				int y = c + j;
				if (valid(x, y)) result += reveal(x, y);
			}
		}
	}
	return result;
}

bool check(int r, int c) {
	if (board[r][c] == '*') return false;
	memcpy(board2, board, sizeof board);
	if (reveal(r, c) == R * C - M) {
		return true;
	}
	return false;
}

bool check() {
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (check(i, j)) {
				board[i][j] = 'c';
				return true;
			}
		}
	}
	return false;
}

bool solve(int r, int c, int M) {
	if (M == 0) {
		return check();
	} else if (r == R) {
		return false;
	} else if (c == C) {
		return solve(r + 1, 0, M);
	} else {
		if (solve(r, c + 1, M)) {
			return true;
		}
		board[r][c] = '*';
		if (solve(r, c + 1, M - 1)) {
			return true;
		}
		board[r][c] = '.';
		return false;
	}
}

int main() {
	cin >> T;
	for (int I = 1; I <= T; I++) {
		cin >> R >> C >> M;
		cout << "Case #" << I << ":" << endl;
		memset(board, '.', sizeof board);
		if (solve(0, 0, M)) {
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					cout << board[i][j];
				}
				cout << endl;
			}
		} else {
			cout << "Impossible" << endl;
		}
	}
	return 0;
}
