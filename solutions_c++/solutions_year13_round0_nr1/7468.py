#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <cstdio>

using namespace std;

char board[4][4];

int main() {
	int T;
	char input;
	int counter = 1;
	cin >> T;
	while (T-- > 0) {
		char who = '.';
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> input;
				board[i][j] = input;
			}
		}
		if (board[0][0] != '.') {
			if (board[0][0] == 'T' && board[1][1] == board[2][2] && board[1][1] == board[3][3]) {
				who = board[1][1];
			} else if ((board[0][0] == board[1][1] || board[1][1] == 'T')&&(board[1][1] == board[2][2] || board[2][2] == 'T')&&(board[2][2] == board[3][3]) || board[3][3] == 'T') {
				who = board[0][0];
			}
		}
		if (board[0][3] != '.' && who == '.') {
			if (board[0][3] == 'T' && board[1][2] == board[2][1] && board[1][2] == board[3][0]) {
				who = board[1][2];
			} else if ((board[0][3] == board[1][2] || board[1][2] == 'T')&&(board[0][3] == board[2][1] || board[1][2] == 'T')&&(board[0][3] == board[3][0] || board[3][0] == 'T')) {
				who = board[0][3];
			}
		}
		if (who == '.') {
		for (int i = 0; i < 4; i++) {
			if (board[i][0] != '.') {
				if (board[i][0] == 'T' && board[i][1] == board[i][2] && board[i][2] == board[i][3]){
					who = board[i][1];
					break;
				} else if ((board[i][0] == board[i][1] || board[i][1] == 'T')&&(board[i][0] == board[i][2] || board[i][2] == 'T')&&(board[i][0] == board[i][3] || board[i][3] == 'T')) {
					who = board[i][0];
					break;
				}
			}
			if (board[0][i] != '.') {
				if (board[0][i] == 'T' && board[1][i] == board[2][i] && board[2][i] == board[3][i]){
					who = board[1][i];
					break;
				} else if ((board[0][i] == board[1][i] || board[1][i] == 'T')&&(board[0][i] == board[2][i] || board[2][i] == 'T')&&(board[0][i] == board[3][i] || board[3][i] == 'T')) {
					who = board[0][i];
					break;
				}
			}
		}
		}
		if (who == '.') {
			int temp = 0;
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					if (board[i][j] == '.')
						temp = 1;
				}
			}
			if (temp == 1)
				cout << "Case #" << counter << ": " << "Game has not completed" << endl;
			else if (temp == 0)
				cout << "Case #" << counter << ": " << "Draw" << endl;
		} else
			cout << "Case #" << counter << ": " << who << " won" << endl;
		counter++;
	}	
	return 0;
}