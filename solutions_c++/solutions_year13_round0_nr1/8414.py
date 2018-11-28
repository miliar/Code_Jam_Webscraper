#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
 
using namespace std;
 
typedef long long LL; 

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int n, Ti = -1, Tj = -1;
	cin >> n;
	char board[4][4];
	for (int k = 0; k < n; ++k) {

		bool full = true, solved = false;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> board[i][j];
				full &= (board[i][j] != '.');
				if (board[i][j] == 'T') {
					Ti = i;
					Tj = j;
				}
			}
		}

		for (int p = 0; p < 2; ++p) {
			if (Ti != -1) {
				if (p == 0) board[Ti][Tj] = 'O';
				else board[Ti][Tj] = 'X';
			} else p = 1;

			for (int i = 0; i < 4; ++i) {
				bool row = true;
				if (board[i][0] == '.') continue;
				for (int j = 0; j < 4; ++j)
					row &= (board[i][j] == board[i][0]);
				if (row) {
					solved = true;
					cout << "Case #" << k + 1 << ": " << board[i][0] << " won" << endl;
					break;
				}
			}
			if (solved) break;

			for (int i = 0; i < 4; ++i) {
				bool col = true;
				if (board[0][i] == '.') continue;
				for (int j = 0; j < 4; ++j)
					col &= (board[j][i] == board[0][i]);
				if (col) {
					solved = true;
					cout << "Case #" << k + 1 << ": " << board[0][i] << " won" << endl;
					break;
				}
			}
			if (solved) break;
			
			if (board[0][0] != '.' && board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[3][3] == board[2][2]) {
				solved = true;
				cout << "Case #" << k + 1 << ": " << board[0][0] << " won" << endl;
				break;
			}
			if (board[0][3] != '.' && board[0][3] == board[1][2] && board[1][2] == board[2][1] && board[2][1] == board[3][0]) {
				solved = true;
				cout << "Case #" << k + 1 << ": " << board[0][3] << " won" << endl;
				break;
			}
			
		}
		if (solved) continue;
		if (!full) cout << "Case #" << k + 1 << ": Game has not completed" << endl;
		else cout << "Case #" << k + 1 << ": Draw" << endl;
	}
	return 0;
}