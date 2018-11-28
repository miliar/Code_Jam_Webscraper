#include <vector>
#include <iostream>
#include <fstream>

int cnts[3][11] = {0};

void add(char x, int y) {
	switch (x) {
		case 'X':
			cnts[0][y]++;
			break;
		case 'O':
			cnts[1][y]++;
			break;
		case '.':
			cnts[2][10]++;
			break;
		case 'T':
			cnts[0][y]++;
			cnts[1][y]++;
			break;
	}

	if (cnts[0][y] == 4) { cnts[0][10] = 1; }
	if (cnts[1][y] == 4) { cnts[1][10] = 1; }
}

void checkChar(char x, int y) {
	add(x, y / 4);
	add(x, 4 + (y % 4));

	switch(y) {
		case 0:
		case 5:
		case 10:
		case 15:
			add(x, 8);
			break;
		case 3:
		case 6:
		case 9:
		case 12:
			add(x, 9);
			break;
	}
}

void zeroOut() {
	for (int i = 0; i < 3; ++i) {
		for (int j = 0; j < 11; ++j) {
			cnts[i][j] = 0;
		}
	}
}

int main(void) {
	int cases = 0;
	std::ifstream inFile;
	char x;
	std::string out;

	inFile.open("tttt.txt");

	inFile >> cases;

	for (int i = 0; i < cases; ++i) {
		zeroOut();

		for (int j = 0; j < 16; ++j) {
			inFile >> x;
			checkChar(x, j);
		}

		if (cnts[0][10] > 0) {
			out = "X won";
		} else if (cnts[1][10] > 0) {
			out = "O won";
		} else if (cnts[2][10] == 0) {
			out = "Draw";
		} else {
			out = "Game has not completed";
		}

		std::cout << "Case #" << (i + 1) << ": " << out << std::endl;
	}

	inFile.close();

	return 0;
}
