#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>

using namespace std;

string A[4];

void solve()
{
	for (int i = 0; i < 4; ++i) {
		A[i] = "";
		while (A[i] == "") {
			getline(cin, A[i]);
		}
		// cout << A[i] << endl;
	}
	// cout << endl;

	bool empty = false;
	bool win_0 = false, win_1 = false;
	for (int i = 0; i < 4; ++i) {
		bool is_good = true;
		for (int j = 0; j < 4; ++j) {
			if (A[i][j] == '.') {
				empty = true;
			}
			if (A[i][j] == 'O' || A[i][j] == '.') {
				is_good = false;
			}
		}
		win_0 |= is_good;
		is_good = true;
		for (int j = 0; j < 4; ++j) {
			if (A[j][i] == 'O' || A[j][i] == '.') {
				is_good = false;
			}
		}
		win_0 |= is_good;
		is_good = true;
		for (int j = 0; j < 4; ++j) {
			if (A[i][j] == 'X' || A[i][j] == '.') {
				is_good = false;
			}
		}
		win_1 |= is_good;
		is_good = true;
		for (int j = 0; j < 4; ++j) {
			if (A[j][i] == 'X' || A[j][i] == '.') {
				is_good = false;
			}
		}
		win_1 |= is_good;
	}

	bool is_good = true;
	for (int i = 0; i < 4; ++i) {
		if (A[i][i] == 'O' || A[i][i] == '.') {
			is_good = false;
		}
	}
	win_0 |= is_good;
	is_good = true;
	for (int i = 0; i < 4; ++i) {
		if (A[i][4 - i - 1] == 'O' || A[i][4 - i - 1] == '.') {
			is_good = false;
		}
	}
	win_0 |= is_good;

	is_good = true;
	for (int i = 0; i < 4; ++i) {
		if (A[i][i] == 'X' || A[i][i] == '.') {
			is_good = false;
		}
	}
	win_1 |= is_good;
	is_good = true;
	for (int i = 0; i < 4; ++i) {
		if (A[i][4 - i - 1] == 'X' || A[i][4 - i - 1] == '.') {
			is_good = false;
		}
	}
	win_1 |= is_good;

	if (win_0 == win_1) {
		if (!win_0 && empty) {
			cout << "Game has not completed\n";
		}
		else {
			cout << "Draw\n";
		}
	}
	else {
		if (win_0) {
			cout << "X won\n";
		}
		else {
			cout << "O won\n";
		}
	}
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	string st;
	getline(cin, st);
	int t = atoi(st.c_str());
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

	return 0;
}