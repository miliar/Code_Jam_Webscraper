#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

class Case {
public:
	Case(ifstream &input);
	string solve();
	char board[4][4];
};

Case::Case(ifstream &input) {
	int j, k;
	
	for (j = 0; j < 4; j++) {
		for (k = 0; k < 4; k++) {
			input >> board[j][k];
			}
	}
}

string Case::solve() {
	int i, j, x, o, t, empty = 0;
	bool x_has_won = false, o_has_won = false;

	// check rows
	for (i = 0; i < 4 && !(x_has_won || o_has_won); i++) {
		x = 0, o = 0, t = 0;
		for (j = 0; j < 4; j++) {
			switch (board[i][j]) {
			case 'X':
				x++;
				break;
			case 'O':
				o++;
				break;
			case 'T':
				t++;
				break;
			case '.':
				empty++;
				break;
			}
		}

		if (x == 4 || (x == 3 && t == 1)) {
			x_has_won = true;
		}

		if (o == 4 || (o == 3 && t == 1)) {
			o_has_won = true;
		}
	}
	
	// check columns
	for (i = 0; i < 4 && !(x_has_won || o_has_won); i++) {
		x = 0, o = 0, t = 0;
		for (j = 0; j < 4; j++) {
			switch (board[j][i]) {
			case 'X':
				x++;
				break;
			case 'O':
				o++;
				break;
			case 'T':
				t++;
				break;
			case '.':
				empty++;
				break;
			}
		}

		if (x == 4 || (x == 3 && t == 1)) {
			x_has_won = true;
		}

		if (o == 4 || (o == 3 && t == 1)) {
			o_has_won = true;
		}
	}
	
	// check diagonals
	x = 0, o = 0, t = 0;
	for (i = 0; i < 4 && !(x_has_won || o_has_won); i++) {
		switch (board[i][i]) {
		case 'X':
			x++;
			break;
		case 'O':
			o++;
			break;
		case 'T':
			t++;
			break;
		case '.':
			empty++;
			break;
		}
	}

	if (x == 4 || (x == 3 && t == 1)) {
		x_has_won = true;
	}

	if (o == 4 || (o == 3 && t == 1)) {
		o_has_won = true;
	}
	
	x = 0, o = 0, t = 0;
	for (i = 0; i < 4 && !(x_has_won || o_has_won); i++) {
		switch (board[i][3-i]) {
		case 'X':
			x++;
			break;
		case 'O':
			o++;
			break;
		case 'T':
			t++;
			break;
		case '.':
			empty++;
			break;
		}
	}

	if (x == 4 || (x == 3 && t == 1)) {
		x_has_won = true;
	}

	if (o == 4 || (o == 3 && t == 1)) {
		o_has_won = true;
	}

	if (x_has_won) {
		return "X won";
	}

	if (o_has_won) {
		return "O won";
	}

	if (empty == 0) {
		return "Draw";
	}

	return "Game has not completed";
}

int main() {
	int cases, i;
	Case* testcase;

	ifstream input("A-large-0.in");
	ofstream output("A-large-0.out");
	if (input.is_open()) {
		if (input.good()) {
			input >> cases;
			for (i = 1; i <= cases; i++) {
				testcase = new Case(input);
				output << "Case #" << i << ": " << testcase->solve() << "\n";
			}
		}
	}
	output.close();
	input.close();
	return 0;
}
