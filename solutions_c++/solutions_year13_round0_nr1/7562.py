#include <iostream>
#include <fstream>

using namespace std;

enum GameStatus {
	GameNotCompleted,
	OWon,
	XWon,
	Draw
};

GameStatus getGameStatus(char board[4][4]);

int main(int argc, const char ** argv) {

	// Read the inputs

	ifstream inputFile;
	inputFile.open(argv[1]);

	int testCases;
	inputFile >> testCases;

	for (int i = 0; i < testCases && inputFile.good(); i++) {
		string l1, l2, l3, l4;

		inputFile >> l1 >> l2 >> l3 >> l4;

		// Convert to a matrix
		char board[4][4] = {
			l1[0], l1[1], l1[2], l1[3],
			l2[0], l2[1], l2[2], l2[3],
			l3[0], l3[1], l3[2], l3[3],
			l4[0], l4[1], l4[2], l4[3]
		};

		string output = "";
		GameStatus status = getGameStatus(board);
		switch(status) {
			case GameNotCompleted: {
				output = "Game has not completed";
				break;
			}

			case Draw: {
				output = "Draw";
				break;
			}

			case XWon: {
				output = "X won";
				break;
			}

			case OWon: {
				output = "O won";
				break;
			}
		}

		//cout << "\n Game Status: " << status;
	
		cout << "Case #" << (i+1) << ": " << output << endl;

		inputFile.get();	// The last empty line
	}

	return 0;
}

GameStatus getGameStatus(char board[4][4]) {
	bool xWon, oWon;
	
	// Check Rows
	for (int i = 0; i < 4; i++) {
		xWon = true;
		for (int j = 0; j < 4; j++) {
			if (!(board[i][j] == 'X' || board[i][j] == 'T')) {
				xWon = false;
				break;
			}
		}
		if (xWon) { 
			return XWon;
		}

		oWon = true;
		for (int j = 0; j < 4; j++) {
			if (!(board[i][j] == 'O' || board[i][j] == 'T')) {
				oWon = false;
				break;
			}
		}
		if (oWon) { 
			return OWon;
		}
	}

	// Check Columns
	for (int i = 0; i < 4; i++) {
		xWon = true;
		for (int j = 0; j < 4; j++) {
			if (!(board[j][i] == 'X' || board[i][j] == 'T')) {
				xWon = false;
				break;
			}
		}
		if (xWon) { 
			return XWon;
		}

		oWon = true;
		for (int j = 0; j < 4; j++) {
			if (!(board[j][i] == 'O' || board[i][j] == 'T')) {
				oWon = false;
				break;
			}
		}
		if (oWon) { 
			return OWon;
		}
	}

	// Check the left diagonal
	xWon = true, oWon = true;
	for (int i = 0, j = 0; i < 4 && j < 4; i++, j++) {
		if (!(board[i][j] == 'X' || board[i][j] == 'T')) {
			xWon = false;
		}

		if (!(board[i][j] == 'O' || board[i][j] == 'T')) {
			oWon = false;
		}
	}

	if (xWon) return XWon;
	if (oWon) return OWon;

	// Check the right diagonal
	xWon = true, oWon = true;
	for (int i = 0, j = 3; i < 4 && j >= 0; i++, j--) {
		if (!(board[i][j] == 'X' || board[i][j] == 'T')) {
			xWon = false;
		}

		if (!(board[i][j] == 'O' || board[i][j] == 'T')) {
			oWon = false;
		}
	}

	if (xWon) return XWon;
	if (oWon) return OWon;

	// At this point, the game should be either a draw
	// or not complete.

	for (int i = 0; i < 4; i++) {		// Check for vacant squares
		for (int j = 0; j < 4; j++) {
			if (board[i][j] == '.') return GameNotCompleted;
		}
	}	

	return Draw;
}