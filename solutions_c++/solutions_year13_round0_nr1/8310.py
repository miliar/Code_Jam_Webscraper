
#include <fstream>
#include <iostream>

using namespace std;

char field[4][4];

inline bool oposite(char symbol) {
	return (symbol == 'X') ? 'O' : 'X';
}

char checkRow(int row) {
	char currentSymbol = (field[row][0] == 'T') ? field[row][1] : field[row][0];
	for (int i=0; i < 4; i++) {
		if (field[row][i] == currentSymbol) continue;
		switch (field[row][i]) {
			case '.': return '.';
			case 'T': continue;
			default: return 'D';
		}
	}
	return currentSymbol;
}

char checkColumn(int col) {
	char currentSymbol = (field[0][col] == 'T') ? field[1][col] : field[0][col];
	for (int i=0; i < 4; i++) {
		if (field[i][col] == currentSymbol) continue;
		switch (field[i][col]) {
			case '.': return '.';
			case 'T': continue;
			default: return 'D';
		}
	}
	return currentSymbol;
}

char checkDiagonal1() {
	char currentSymbol = (field[0][0] == 'T') ? field[1][1] : field[0][0];
	for (int i=0; i < 4; i++) {
		if (field[i][i] == currentSymbol) continue;
		switch (field[i][i]) {
			case '.': return '.';
			case 'T': continue;
			default: return 'D';
		}
	}
	return currentSymbol;
}

char checkDiagonal2() {
	char currentSymbol = (field[3][0] == 'T') ? field[2][1] : field[3][0];
	for (int i=0; i < 4; i++) {
		if (field[3-i][i] == currentSymbol) continue;
		switch (field[3-i][i]) {
			case '.': return '.';
			case 'T': continue;
			default: return 'D';
		}
	}
	return currentSymbol;
}

string checkFields() {
	char result = 'D';
	switch (checkDiagonal1()) {
		case 'X':
			return "X won";
		case 'O':
			return "O won";
		case '.':
			result = '.';
	}
	switch (checkDiagonal2()) {
		case 'X':
			return "X won";
		case 'O':
			return "O won";
		case '.':
			result = '.';
	}
	for (int i=0; i < 4; i++) {
		switch (checkRow(i)) {
			case 'X':
				return "X won";
			case 'O':
				return "O won";
			case '.':
				result = '.';
		}
		switch (checkColumn(i)) {
			case 'X':
				return "X won";
			case 'O':
				return "O won";
			case '.':
				result = '.';
		}
	}
	return (result == 'D') ? "Draw" : "Game has not completed";
}

void solve(const char* filename) {
	ifstream in(filename);
	int N;
	in >> N;
	for (int n=0; n < N; n++) {
		for (int i=0; i < 4; i++) {
			for (int j=0; j < 4; j++) {
				in >> field[i][j];
			}
			in.get();
		}
		cout << "Case #" << n+1 << ": " << checkFields() << endl;
	}
}


int main(int argc, char** argv) {
	solve(argv[1]);
}
