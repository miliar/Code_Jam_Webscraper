#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
const int size = 4;
const int infty = 9999999;
char table[size][size];

void init() {
	for (int i = 0; i < size; ++i)
		for (int j = 0; j < size; ++j)
			table[i][j] = '.';
}

int check() {
	bool empty = false;

	// Diagonal
	int O = 0, X = 0;
	for (int i = 0; i < size; ++i) {
		if (table[i][i] == 'X' || table[i][i] == 'T')
			++X;
		if (table[i][i] == 'O' || table[i][i] == 'T')
			++O;
		if (!empty && table[i][i] == '.')
			empty = true;
	}
	if (O == size) return 0;
	if (X == size) return 1;

	O = 0, X = 0;
	for (int i = 0; i < size; ++i) {
		if (table[size-i-1][i] == 'X' || table[size-i-1][i] == 'T')
			++X;
		if (table[size-i-1][i] == 'O' || table[size-i-1][i] == 'T')
			++O;
		if (!empty && table[size-i-1][i] == '.')
			empty = true;
	}
	if (O == size) return 0;
	if (X == size) return 1;

	// Row
	for (int i = 0; i < size; ++i) {
		int numO = 0, numX = 0;
		for (int j = 0; j < size; ++j) {
			if (table[i][j] == 'X' || table[i][j] == 'T')
				++numX;
			if (table[i][j] == 'O' || table[i][j] == 'T')
				++numO;
			if (!empty && table[i][j] == '.')
				empty = true;
		}
		if (numO == size)
			return 0;
		if (numX == size)
			return 1;
	}

	// Column
	for (int i = 0; i < size; ++i) {
		int numO = 0, numX = 0;
		for (int j = 0; j < size; ++j) {
			if (table[j][i] == 'X' || table[j][i] == 'T')
				++numX;
			if (table[j][i] == 'O' || table[j][i] == 'T')
				++numO;
			if (!empty && table[j][i] == '.')
				empty = true;
		}
		if (numO == size)
			return 0;
		if (numX == size)
			return 1;
	}

	if (empty) return 2;
	else return 3;
}


int main() {
	ofstream fout("tictac_output.txt");
	int N;
	cin >> N;
	string str;
	for (int i = 0; i < N; ++i) {
		init();
		int cnt = 0;
		while (cnt < size) {
			cin >> str;
			if (str.length() != size) continue;
			else {
				for (int k = 0; k < str.length(); ++k)
					table[cnt][k] = str[k];
				cnt = cnt + 1;
			}
		}
		int ans = check();
		fout << "Case #" << i+1 << ": ";
		if (ans == 0) 
			fout << "O won" << endl;
		else if (ans == 1)
			fout << "X won" << endl;
		else if (ans == 2)
			fout << "Game has not completed" << endl;
		else if (ans == 3)
			fout << "Draw" << endl;

	}
	fout.close();

	return 0;
}
