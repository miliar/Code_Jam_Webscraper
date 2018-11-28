#include <iostream>
#include <fstream>
#define  INPUTFILE "Alarge.in"
#define  OUTPUTFILE "Alarge.out"

using namespace std;

int main () {
	ifstream inf (INPUTFILE, ios::in);
	ofstream outf (OUTPUTFILE, ios::out);

	int X, O;
	char board[4][4];
	int T;
	char n;
	bool isEmpty;
	while (inf >> T) {
		int i=0;
		while (++i) {
			isEmpty = false;
			for (int row=0; row<4; ++row) {
				for (int col=0; col<4; ++col) {
					inf >> board[row][col];
					if (board[row][col]=='.') isEmpty = true;
				}
			}

			X=0; O=0;
			// check diagonal
			for (int col=0; col<4; ++col) {
				switch (board[col][col]) {
					case 'X':
						++X;
						break;
					case 'O':
						++O;
						break;
					case 'T':
						++X; ++O;
						break;
				}
				if (X==4) {
					outf << "Case #" << i << ": X won" << endl;
					goto loop;
				}
				if (O==4) {
					outf << "Case #" << i << ": O won" << endl;
					goto loop;
				}
			}
			X=0; O=0;
			// check diagonal
			for (int col=0; col<4; ++col) {
				switch (board[col][3-col]) {
					case 'X':
						++X;
						break;
					case 'O':
						++O;
						break;
					case 'T':
						++X; ++O;
						break;
				}
				if (X==4) {
					outf << "Case #" << i << ": X won" << endl;
					goto loop;
				}
				if (O==4) {
					outf << "Case #" << i << ": O won" << endl;
					goto loop;
				}
			}
			//check row
			for (int row=0; row<4; ++row) {
				X=0; O=0;
				for (int col=0; col<4; ++col) {
					switch (board[row][col]) {
						case 'X':
							++X;
							break;
						case 'O':
							++O;
							break;
						case 'T':
							++X; ++O;
							break;
					}
					if (X==4) {
						outf << "Case #" << i << ": X won" << endl;
						goto loop;
					}
					if (O==4) {
						outf << "Case #" << i << ": O won" << endl;
						goto loop;
					}
				}
			}
			//check col
			for (int col = 0; col < 4; ++col) {
				X=0; O=0;
				for (int row = 0; row < 4; ++row) {
					switch (board[row][col]) {
						case 'X':
							++X;
							break;
						case 'O':
							++O;
							break;
						case 'T':
							++X; ++O;
							break;
					}
					if (X==4) {
						outf << "Case #" << i << ": X won" << endl;
						goto loop;
					}
					if (O==4) {
						outf << "Case #" << i << ": O won" << endl;
						goto loop;
					}
				}
			}
			if (isEmpty)
				outf << "Case #" << i << ": Game has not completed" << endl;
			else 
				outf << "Case #" << i << ": Draw" << endl;
			loop: 
				if (i<T) continue;
				else break;
		}
	}
	return 0;
}
