#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

void printBoard();
bool fillBoard();
char checkForWinner();

fstream input;
char board[4][4] = {'.'};

int main() {
	input.open("input.txt");
	string intLine;
	getline(input, intLine);
	int count = atoi(intLine.c_str());
	int numberOfCurrentBoard = 1;
	while (numberOfCurrentBoard - 1 < count) {
		cout<<"Case #"<<numberOfCurrentBoard<<": ";
		bool boardIsFull = fillBoard();	
		char result = checkForWinner();
		if (result == 'X') cout<<"X won"<<endl;
		else if (result == 'O') cout<<"O won"<<endl;
		else if (boardIsFull) cout<<"Draw"<<endl;
		else cout<<"Game has not completed"<<endl;
		if (numberOfCurrentBoard != count) getline(input, intLine);
		numberOfCurrentBoard++;
	}

	return 0;
}

bool fillBoard() {
	bool boardIsFull = true;
	for (int i = 0; i < 4; i++) {
		string line;
		getline(input, line);
		for (int j = 0; j < 4; j++) {
			board[i][j] = line.at(j);
			if (line.at(j) == '.')
				boardIsFull = false;
		}
	}
	return boardIsFull;
}

void printBoard() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			cout << "[" <<  board[i][j] <<  "]";
		}
		cout<<endl;
	}
}

char checkForWinner() {
	for (int i = 0; i < 4; i++) {
		char letter = board[i][0];

		bool isValid = true;
		if (letter == 'T') letter = board[i][1];

		if (letter == '.' ) isValid = false;

		for (int j = 0; j < 4 && isValid; j++) {
			if (board[i][j] != 'T' && board[i][j] != letter) {
				isValid = false;
			}
		}
		if (isValid) return letter;
	}

	for (int i = 0; i < 4; i++) {
		char letter = board[0][i];

		bool isValid = true;
		if (letter == 'T') letter = board[1][i];

		if (letter == '.' ) isValid = false;

		for (int j = 0; j < 4 && isValid; j++) {
			if (board[j][i] != 'T' && board[j][i] != letter) {
				isValid = false;
			}
		}
		if (isValid) return letter;
	}

	char letter = board[0][0];
	bool isValid = true;
	if (letter == 'T') letter = board[1][1];
	if (letter == '.' ) isValid = false;
	for (int i = 0; i < 4; i++) {
		if (board[i][i] != 'T' && board[i][i] != letter) {
			isValid = false;
		}
	}
	if (isValid) return letter;

	letter = board[3][0];
	isValid = true;
	if (letter == 'T') letter = board[3][1];
	if (letter == '.' ) isValid = false;
	for (int i = 0; i < 4; i++) {
		if (board[3-i][i] != 'T' && board[3-i][i] != letter) {
			isValid = false;
		}
	}
	if (isValid) return letter;

	
	return '.';
}
