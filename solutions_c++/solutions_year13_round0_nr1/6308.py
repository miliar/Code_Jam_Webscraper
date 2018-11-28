#include <iostream>
#include <fstream>

using namespace std;

// Returns 1 if X's win
// Returns 2 if O's win
// Returns 3 if board is full
// Returns 0 otherwise
int checkBoard(char *board) {
	// Check horizontally
	for (int x = 0; x < 4; ++x) {
		if(board[4*x] != '.') {
			char t = board[4*x];
			bool goodBoard = true;

			if(t == 'T') {
				if(board[4*x + 1] == '.')
					continue;
				else
					t = board[4*x + 1];
			}



			for(int y = 1; y < 4; ++y) {
				if(board[4*x + y] != t && board[4*x + y] != 'T')
					goodBoard = false;
			}

			if(goodBoard) {
				if(t == 'X')
					return 1;
				else
					return 2;
			}
		}
	}

	// Check horizontally
	for (int y = 0; y < 4; ++y) {
		if(board[y] != '.') {
			char t = board[y];
			bool goodBoard = true;

			if(t == 'T') {
				if(board[y + 4] == '.')
					continue;
				else
					t = board[y + 4];
			}



			for(int x = 1; x < 4; ++x) {
				if(board[4*x + y] != t && board[4*x + y] != 'T')
					goodBoard = false;
			}

			if(goodBoard) {
				if(t == 'X')
					return 1;
				else
					return 2;
			}
		}
	}

	// Check diagonally
	char start = board[0];
	if(start == 'T' && board[5] != '.')
		start = board[5];
	if(start != '.') {
		bool goodBoard = true;

		for(int idx = 5; idx < 16; idx += 5) {
			if(board[idx] != start && board[idx] != 'T')
				goodBoard = false;
		}

		if(goodBoard) {
			if(start == 'X')
				return 1;
			else
				return 2;
		}
	}

	start = board[3];
	if(start == 'T' && board[6] != '.')
		start = board[6];
	if(start != '.') {
		bool goodBoard = true;

		for(int idx = 6; idx < 13; idx += 3) {
			if(board[idx] != start && board[idx] != 'T')
				goodBoard = false;
		}

		if(goodBoard) {
			if(start == 'X')
				return 1;
			else
				return 2;
		}
	}

	// Check for tie game
	for(int i = 0; i < 16; ++i)
		if(board[i] == '.')
			return 0;

	return 3;
}

int main(int argc, char **argv) {
	fstream inFile(argv[1]);
	fstream outFile("ttt.result", fstream::trunc | fstream::out);

	int lines;
	inFile >> lines;

	cout << "Number of boards: " << lines << endl;

	char *board = new char(16);
	char c;
	for(int caseNum = 1; caseNum <= lines; ++caseNum) {
		for(int i = 0; i < 16; ) {
			inFile >> c;
			if(c == 'X' || c == '.' || c == 'O' || c == 'T') {
				board[i] = c;
				++i;
				cout << c;
			}
		}


		outFile << "Case #" << caseNum << ": ";
		int res = checkBoard(board);
		if(res == 1)
			outFile << "X won\n";
		else if(res == 2)
			outFile << "O won\n";
		else if(res == 3)
			outFile << "Draw\n";
		else
			outFile << "Game has not completed\n";
	}

	inFile.close();
	outFile.close();
	return 0;
}