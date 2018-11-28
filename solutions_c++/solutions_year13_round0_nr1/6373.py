#include <fstream>
#include <vector>
#include <string>

using namespace std;

const int BOARD_SIZE = 4;

int checkBoard(const vector<string>& board);
int checkRow(const vector<string>& board);
int checkColumn(const vector<string>& board);
int checkDiagonal(const vector<string>& board);
bool isExistEmpty(const vector<string>& board);

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int numberOfCases;
	in >> numberOfCases;
	vector<string> board(BOARD_SIZE + 1);
	for (int i = 1; i <= numberOfCases; ++i) {
		for (int j = 0; j <= BOARD_SIZE; ++j) {
			getline(in, board[j]);
		}
		in.get();

		out << "Case #" << i << ": ";
		int result = checkBoard(board);
		switch (result) {
			case 0:
				out << "X won" << endl;
				break;
			case 1:
				out << "O won" << endl;
				break;
			case 2:
				out << "Draw" << endl;
				break;
			case 3:
				out << "Game has not completed" << endl;
				break;
		}
	}
}

int checkBoard(const vector<string>& board)
{
	int rowResult = checkRow(board);
	if (rowResult != -1) {
		return rowResult;
	}

	int columnResult = checkColumn(board);
	if (columnResult != -1) {
		return columnResult;
	}

	int diagonalResult = checkDiagonal(board);
	if (diagonalResult != -1) {
		return diagonalResult;
	}

	if (isExistEmpty(board)) {
		return 3;
	}
	else {
		return 2;
	}
}

int checkRow(const vector<string>& board)
{
	for (int i = 0; i < BOARD_SIZE; ++i) {
		int XCounter = 0;
		int OCounter = 0;
		int TCounter = 0;
		for (int j = 0; j < BOARD_SIZE; ++j) {
			if (board[i][j] == 'X') {
				++XCounter;
			}
			else if (board[i][j] == 'O') {
				++OCounter;
			}
			else if (board[i][j] == 'T') {
				++TCounter;
			}
		}

		if ((XCounter == 4) || (XCounter == 3 && TCounter == 1)) {
			return 0;
		}
		if ((OCounter == 4) || (OCounter == 3 && TCounter == 1)) {
			return 1;
		}
	}
	return -1;
}

int checkColumn(const vector<string>& board)
{
	for (int j = 0; j < BOARD_SIZE; ++j) {
		int XCounter = 0;
		int OCounter = 0;
		int TCounter = 0;
		for (int i = 0; i < BOARD_SIZE; ++i) {
			if (board[i][j] == 'X') {
				++XCounter;
			}
			else if (board[i][j] == 'O') {
				++OCounter;
			}
			else if (board[i][j] == 'T') {
				++TCounter;
			}
		}

		if ((XCounter == 4) || (XCounter == 3 && TCounter == 1)) {
			return 0;
		}
		if ((OCounter == 4) || (OCounter == 3 && TCounter == 1)) {
			return 1;
		}
	}
	return -1;
}

int checkDiagonal(const vector<string>& board)
{
	int XCounter = 0;
	int OCounter = 0;
	int TCounter = 0;
	for (int i = 0; i < BOARD_SIZE; ++i) {	
		if (board[i][i] == 'X') {
			++XCounter;
		}
		else if (board[i][i] == 'O') {
			++OCounter;
		}
		else if (board[i][i] == 'T') {
			++TCounter;
		}
	}
	if ((XCounter == 4) || (XCounter == 3 && TCounter == 1)) {
		return 0;
	}
	if ((OCounter == 4) || (OCounter == 3 && TCounter == 1)) {
		return 1;
	}

	XCounter = 0;
	OCounter = 0;
	TCounter = 0;
	for (int i = 0; i < BOARD_SIZE; ++i) {
		if (board[i][BOARD_SIZE - i - 1] == 'X') {
			++XCounter;
		}
		else if (board[i][BOARD_SIZE - i - 1] == 'O') {
			++OCounter;
		}
		else if (board[i][BOARD_SIZE - i - 1] == 'T') {
			++TCounter;
		}
	}
	if ((XCounter == 4) || (XCounter == 3 && TCounter == 1)) {
		return 0;
	}
	if ((OCounter == 4) || (OCounter == 3 && TCounter == 1)) {
		return 1;
	}
	
	return -1;
}

bool isExistEmpty(const vector<string>& board)
{
	for (int i = 0; i < BOARD_SIZE; ++i) {
		for (int j = 0; j < BOARD_SIZE; ++j) {
			if (board[i][j] == '.') {
				return true;
			}
		}
	}
	return false;
}
