#include <iostream>
using namespace std;

bool check_row(char b[4][4], int i, char c)
{
	for (int j = 0; j < 4; j++) {
		if (b[i][j] != c && b[i][j] != 'T')
			return false;
	}
	return true;
}
bool check_col(char b[4][4], int j, char c)
{
	for (int i = 0; i < 4; i++) {
		if (b[i][j] != c && b[i][j] != 'T') {
			return false;
		}
	}
	return true;
}
bool check_dia(char b[4][4], char c)
{
	bool r = true;
	for (int i = 0; i < 4; i++) {
		if (b[i][i] != c && b[i][i] != 'T') {
			r = false;
			break;
		}
	}
	if (r)	return r;
	for (int i = 0; i < 4; i++) {
		if (b[i][3-i] != c && b[i][3-i] != 'T')
			return false;
	}
	return true;
}

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		char board[4][4];
		bool complete = true;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> board[i][j];
				if (board[i][j] == '.')
					complete = false;
			}
		}

		// solve
		char win = 'D';
		char p[2] = {'X', 'O'};
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 4; j++) {
				if (check_row(board, j, p[i]) || check_col(board, j, p[i])) {
					win = p[i];
					break;
				}
			}
			if (check_dia(board, p[i]))
				win = p[i];
			if (win != 'D')
				break;
		}
		cout << "Case #" << t << ": ";
		if (win == 'D') {
			if (complete)
				cout << "Draw" << endl;
			else
				cout << "Game has not completed" << endl;
		}
		else
			cout << win << " won" << endl;

	}

	return 0;
}
