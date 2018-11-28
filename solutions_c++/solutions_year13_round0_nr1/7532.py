#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <math.h>
#include <windows.h>
using namespace std;
typedef long long s64;
typedef unsigned long long u64;
typedef long s32;
typedef unsigned long long u32;



int main(int argc, char* argv[])
{
    HANDLE handle = GetStdHandle(STD_INPUT_HANDLE);
    DWORD mode;
    GetConsoleMode(handle, &mode);
    mode &= ~ENABLE_ECHO_INPUT;
    SetConsoleMode(handle, mode);



	const int mx = 4;
	const int my = 4;



	string line;
	int T;
	cin >> T;
	getline(cin, line);

	for (int t=0; t < T; t++) {

        cout << "Case #" << (t+1) << ": ";

		char board[mx][my];
        string out;

		bool full_board = true;
		for (int y=0; y < my; ++y) {
			getline(cin, line);
			stringstream ss(line);
			for (int x=0; x < mx; ++x) {
				ss >> board[x][y];
				if (board[x][y] == '.') {
					full_board = false;
				}					
			}
		}
		getline(cin, line);

		char result = 'D';

		// Rows
		for (int y=0; y < my; ++y) {
			int X = 0;
			int O = 0;
			for (int x=0; x < mx; ++x) {
				if (board[x][y] == 'X') { X++; }
				if (board[x][y] == 'O') { O++; }
				if (board[x][y] == 'T') { X++; O++; };
			}

			if (X == mx) { result = 'X'; }
			if (O == mx) { result = 'O'; }
		}


		// Columns
		for (int x=0; x < mx; ++x) {
			int X = 0;
			int O = 0;
			for (int y=0; y < my; ++y) {
				if (board[x][y] == 'X') { X++; }
				if (board[x][y] == 'O') { O++; }
				if (board[x][y] == 'T') { X++; O++; };
			}

			if (X == mx) { result = 'X'; }
			if (O == mx) { result = 'O'; }
		}


		// Diagonals
		int X = 0;
		int O = 0;
		for (int x=0, y=0; x < mx; ++x, ++y) {
			if (board[x][y] == 'X') { X++; }
			if (board[x][y] == 'O') { O++; }
			if (board[x][y] == 'T') { X++; O++; };
		}

		if (X == mx) { result = 'X'; }
		if (O == mx) { result = 'O'; }


		X = 0;
		O = 0;
		for (int x=0, y=(my - 1); x < mx; ++x, --y) {
			if (board[x][y] == 'X') { X++; }
			if (board[x][y] == 'O') { O++; }
			if (board[x][y] == 'T') { X++; O++; };
		}

		if (X == mx) { result = 'X'; }
		if (O == mx) { result = 'O'; }



		if (result == 'D') {
			if (full_board) {
				cout << "Draw" << endl;
			} else {
				cout << "Game has not completed" << endl;
			}

		} else {
			cout << result << " won" << endl;
		}
    }

    return 0;
}


