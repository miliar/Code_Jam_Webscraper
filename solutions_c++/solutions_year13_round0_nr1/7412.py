#include <iostream>
#include <string>

using namespace std;

int board[4][4];

void solve()
{
	bool full = true;
	// check horizontal
	for (int i=0; i<4; i++) {
		bool noone = true, nozero = true, rowfull=true;
		for (int j=0; j<4; j++) {
			if (board[i][j] == 0)
				nozero = false;
			if (board[i][j] == 1)
				noone = false;
			if (board[i][j] == 2)
				full = rowfull = false;
		}

		if (noone && rowfull) {
			cout << "O won" << endl;
			return;
		}
		if (nozero && rowfull) {
			cout << "X won" << endl;
			return;
		}
	}

	for (int i=0; i<4; i++) {
		bool noone = true, nozero = true, rowfull=true;
		for (int j=0; j<4; j++) {
			if (board[j][i] == 0)
				nozero = false;
			if (board[j][i] == 1)
				noone = false;
			if (board[j][i] == 2)
				full = rowfull = false;
		}

		if (noone && rowfull) {
			cout << "O won" << endl;
			return;
		}
		if (nozero && rowfull) {
			cout << "X won" << endl;
			return;
		}
	}

	int x= 0, y=0;
	bool noone = true, nozero = true, rowfull=true;
	for (int i=0; i<4; i++) {
		if (board[x][y] == 0)
			nozero = false;
		if (board[x][y] == 1)
			noone = false;
		if (board[x][y] == 2)
			full = rowfull = false;

		x += 1; y+=1;
	}
	if (noone && rowfull) {
		cout << "O won" << endl;
		return;
	}
	if (nozero && rowfull) {
		cout << "X won" << endl;
		return;
	}

	x=0, y=3;
	noone = true, nozero = true, rowfull=true;
	for (int i=0; i<4; i++) {
		if (board[x][y] == 0)
			nozero = false;
		if (board[x][y] == 1)
			noone = false;
		if (board[x][y] == 2)
			full = rowfull = false;

		x += 1; y-=1;
	}
	if (noone && rowfull) {
		cout << "O won" << endl;
		return;
	}
	if (nozero && rowfull) {
		cout << "X won" << endl;
		return;
	}

	if (full)
		cout << "Draw" << endl;
	else
		cout << "Game has not completed" << endl;
}

void input()
{
	string str;
	for (int i=0; i<4; i++) {
		cin >> str;
		for (int j=0; j<4; j++) {
			if (str[j] == 'O')
				board[i][j] = 0;
			else if (str[j] == 'X')
				board[i][j] = 1;
			else if (str[j] == '.')
				board[i][j] = 2;
			else if (str[j] == 'T')
				board[i][j] = 3;
		}
	}
}

int main(int argc, char** argv)
{
	int count;
	cin >> count;

	for (int i=1; i<=count; i++) {
		input();
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}
