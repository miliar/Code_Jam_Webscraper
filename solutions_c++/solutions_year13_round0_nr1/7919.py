//============================================================================
// Name        : gcj-ttt.cpp
// Author      : Yo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <string>
using namespace std;

string check(vector< vector<char> > test, int s) {
	int x, y;
	char check;
	for (x = 0; x < s - 1; x++) {
		check = test[x][0];
		if (check != '.') {
			for (y = 1; y < s; y++) {
				if (check != test[x][y] && test[x][y] != 'T')
					break;
			}
			if (y == s) {
				string res = "  won";
				res[0] = check;
				return res;
			}
		}

		check = test[0][x];
		if (check != '.') {
			for (y = 1; y < s; y++) {
				if (check != test[y][x] && test[y][x] != 'T')
					break;
			}
			if (y == s) {
				string res = "  won";
				res[0] = check;
				return res;
			}
		}
	}

	check = test[0][0];
	if (check != '.') {
		for (x = 1; x < s; x++) {
			if (check != test[x][x] && test[x][x] != 'T')
				break;
		}
		if (x == s) {
			string res = "  won";
			res[0] = check;
			return res;
		}
	}

	check = test[0][3];
	if (check != '.') {
		for (x = 1; x < s; x++) {
			if (check != test[x][3-x] && test[x][3-x] != 'T')
				break;
		}
		if (x == s) {
			string res = "  won";
			res[0] = check;
			return res;
		}
	}

	for (x = 0; x < s; x++) {
		for (y = 0; y < s; y++) {
			if (test[x][y] == '.') {
				return "Game has not completed";
			}
		}
	}

	return "Draw"; // the game is over, and it ended in a draw
	return "X won"; // the game is over, and X won
	return "O won"; // the game is over, and O won
	return "Game has not completed";
}

int main() {

	int n;

	if (!(cin >> n)) {
		return 0;
	}

	char c;
	int size = 4;

	for (int i = 0; i < n; i++) {
		vector< vector<char> > test;

		for (int j = 0; j < size; j++) {
			vector<char> testj;

			for (int k = 0; k < size; k++) {
				cin >> c;
				testj.push_back(c);
			}
			test.push_back(testj);
		}

		cout << "Case #" << (i+1) << ": " << check(test, size) << endl;
	}

	return 0;
}
