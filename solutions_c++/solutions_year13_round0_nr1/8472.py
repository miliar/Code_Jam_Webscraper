#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const string XWon = "X won";
const string OWon = "O won";
const string Draw = "Draw";
const string NotFinished = "Game has not completed";

class TTT {
public:
	static string getResult(string& tableString) {
		char table[4][4] = {0};
		bool winning = true;
		bool movesLeft = false;

		for (int i = 0; i < 4; i ++) {
			for (int j = 0; j < 4; j++) {
				table[i][j] = tableString[i*4 + j];
				cout << table[i][j];
			}
			cout << endl;
		}
		

		// Check for a winning line
		for (int i = 0; i < 4; i ++) {
			winning = true;
			char c = table[i][0];
			for (int j = 0; j < 4; j++) {
				if (table[i][j] == 'T')
					continue;

				if (table[i][j] == '.') {
					movesLeft = true;
					winning = false;
					break;
				}

				if (table[i][j] != c) {
					if (c == 'T') {
						c = table[i][j];
						continue;
					} else {
						winning = false;
						break;
					}
				}
			}

			if (winning) {
				switch (c) {
					case 'X':
						return XWon;
						break;
					case 'O':
						return OWon;
						break;
				}
			}
		}

		// Check the columns
		for (int j = 0; j < 4; j++) {
			winning = true;
			char c = table[0][j];
			for (int i = 0; i < 4; i++) {
				if (table[i][j] == 'T')
					continue;

				if (table[i][j] == '.') {
					movesLeft = true;
					winning = false;
					break;
				}

				if (table[i][j] != c) {
					if (c == 'T') {
						c = table[i][j];
						continue;
					} else {
						winning = false;
						break;
					}
				}
			}

			if (winning) {
				switch (c) {
				case 'X':
					return XWon;
					break;
				case 'O':
					return OWon;
					break;
				}
			}
		}

		char c = table[0][0];
		// Check the diagonals
		for (int i = 0, j = 0; i < 4, j < 4; i++, j++) {
			winning = true;
			if (table[i][j] == 'T')
				continue;

			if (table[i][j] == '.') {
				movesLeft = true;
				winning = false;
				break;
			}

			if (table[i][j] != c) {
				if (c == 'T') {
					c = table[i][j];
					continue;
				} else {
					winning = false;
					break;
				}
			}

		}
		
		if (winning) {
			switch (c) {
			case 'X':
				return XWon;
				break;
			case 'O':
				return OWon;
				break;
			}
		}

		// Check the diagonals
		c = table[3][0];
		for (int i = 3, j = 0; i > 0, j < 4; i--, j++) {
			winning = true;
			
			if (table[i][j] == 'T')
				continue;

			if (table[i][j] == '.') {
				movesLeft = true;
				winning = false;
				break;
			}

			if (table[i][j] != c) {
				if (c == 'T') {
					c = table[i][j];
					continue;
				} else {
					winning = false;
					break;
				}
			}

		}

		if (winning) {
			switch (c) {
			case 'X':
				return XWon;
				break;
			case 'O':
				return OWon;
				break;
			}
		}

		if (movesLeft) {
			return NotFinished;
		} else 
			return Draw;
	}
};

int main(int argc, const char *argv[])
{
	if (argc != 3) {
		cout << "Usage: " << argv[0] << " infile outfile" << endl;
		return 1;
	}

	ifstream infile(argv[1]);
	ofstream outfile(argv[2]);
	unsigned numberOfEnttries;
	string table, line;


	if (infile.is_open()) {
		getline(infile, line);
		numberOfEnttries = atol(line.c_str());

		for (int i = 0; i < numberOfEnttries && infile.good(); i++) {
			table = ""; line = "";
			for (int j = 0; j < 4; j++) {
				getline(infile, line);
				table += line;
			}

			cout << table << endl;
			outfile << "Case #" << i + 1 << ": " << TTT::getResult(table) << endl;
			getline(infile, line);
		}
	}

	cin >> numberOfEnttries;
}