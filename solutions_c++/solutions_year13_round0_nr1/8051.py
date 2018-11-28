#include <iostream>
#include <stdio.h>
#include <vector>
#define rep(i,m)        for(int i=0;i<(int)m;i++)
using namespace std;
char checkWinner(char board[4][4]) {
	// row 1
	if (board[0][0] == board[0][1] && board[0][1] == board[0][2]
			&& board[0][2] == board[0][3])
		return board[0][0];
	// col 1
	if (board[0][0] == board[1][0] && board[1][0] == board[2][0]
			&& board[2][0] == board[3][0])
		return board[0][0];
	// row 2
	if (board[1][0] == board[1][1] && board[1][1] == board[1][2]
			&& board[1][2] == board[1][3])
		return board[1][0];
	// col 2
	if (board[0][1] == board[1][1] && board[1][1] == board[2][1]
			&& board[2][1] == board[3][1])
		return board[1][1];
	// row 3
	if (board[2][0] == board[2][1] && board[2][1] == board[2][2]
			&& board[2][2] == board[2][3])
		return board[2][0];
	// col 3
	if (board[0][2] == board[1][2] && board[1][2] == board[2][2]
			&& board[2][2] == board[3][2])
		return board[2][2];
	// row 4
	if (board[3][0] == board[3][1] && board[3][1] == board[3][2]
			&& board[3][2] == board[3][3])
		return board[3][0];
	// col 4
	if (board[0][3] == board[1][3] && board[1][3] == board[2][3]
			&& board[2][3] == board[3][3])
		return board[2][3];
	// diagonal 1
	if (board[0][0] == board[1][1] && board[2][2] == board[1][1]
			&& board[3][3] == board[1][1])
		return board[0][0];
	// diagonal 2
	if (board[0][3] == board[1][2] && board[1][2] == board[2][1]
			&& board[3][0] == board[2][1])
		return board[0][3];
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			if (board[i][j] == '.')
				return '.';
		}
	}
	return 'D';
}
int main() {
	freopen ("A-small-attempt2.in","r+",stdin);
	freopen ("out.txt","w+",stdout);
	int t;
	cin >> t;
	int z = 0;
	char boardX[4][4];
	char boardY[4][4];
	string s[4];
	string empty;
	while (t--) {
		for (int i = 0; i < 4; ++i) {
			cin >> s[i];
		}
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				boardX[i][j] = s[i][j];
				boardY[i][j] = s[i][j];
				if (boardX[i][j] == 'T') {
					boardX[i][j] = 'X';
					boardY[i][j] = 'O';
				}
			}
		}
		char X = checkWinner(boardX);
		char Y = checkWinner(boardY);
		if (X == 'X')
			cout << "Case #" << (z + 1) << ": " << "X won" << endl;
		else if (Y == 'O')
			cout << "Case #" << (z + 1) << ": " << "O won" << endl;
		else if (X == '.' || Y == '.')
			cout << "Case #" << (z + 1) << ": " << "Game has not completed"
					<< endl;
		else
			cout << "Case #" << (z + 1) << ": " << "Draw" << endl;
		z++;
	}
	return 0;
}
