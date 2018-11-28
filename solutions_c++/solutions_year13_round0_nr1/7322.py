//============================================================================
// Name        : TicTacToeTomek.cpp
// Author      : Steve
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>

using namespace std;

int check(char c1, char c2, char c3, char c4) {
	if(c1==c2 && c1==c3 && c1==c4 && c1!='.') {
		if (c1=='X') {
			return 1;
		} else {
			return 2;
		}
	} else {
		return -1;
	}
}

int checkBoard(string board[]) {
	//printf("\t%s\n\t%s\n\t%s\n\t%s\n\n", board[0].c_str(), board[1].c_str(), board[2].c_str(), board[3].c_str());

	// Check rows
	int value = -1;
	if ((value=check(board[0][0], board[0][1], board[0][2], board[0][3])) > 0) {
		return value;
	}

	if ((value=check(board[1][0], board[1][1], board[1][2], board[1][3])) > 0) {
		return value;
	}

	if ((value=check(board[2][0], board[2][1], board[2][2], board[2][3])) > 0) {
		return value;
	}

	if ((value=check(board[3][0], board[3][1], board[3][2], board[3][3])) > 0) {
		return value;
	}

	//Check columns
	if ((value=check(board[0][0], board[1][0], board[2][0], board[3][0])) > 0) {
		return value;
	}

	if ((value=check(board[0][1], board[1][1], board[2][1], board[3][1])) > 0) {
		return value;
	}

	if ((value=check(board[0][2], board[1][2], board[2][2], board[3][2])) > 0) {
		return value;
	}

	if ((value=check(board[0][3], board[1][3], board[2][3], board[3][3])) > 0) {
		return value;
	}

	//Check diagonals
	if ((value=check(board[0][0], board[1][1], board[2][2], board[3][3])) > 0) {
		return value;
	}

	if ((value=check(board[3][0], board[2][1], board[1][2], board[0][3])) > 0) {
		return value;
	}

	//Check if game over
	if (board[0].find_first_of('.') == string::npos &&
		board[1].find_first_of('.') == string::npos &&
		board[2].find_first_of('.') == string::npos &&
		board[3].find_first_of('.') == string::npos) {
		return 0;  //tie
	} else {
		return -1;
	}
}

int main(int argc, char *argv[]) {
	string line;
	string board[4];
	int cases = 0;

	ifstream stream("tests/A-large.in");

//	if (stream.is_open()) {
//		printf("File is opened\n");
//	} else {
//		printf("Failed to open file\n");
//	}
	//printf("Enter number of cases: ");

	getline(stream, line);

	cases = atoi(line.c_str());

	//printf("Reading in %d cases\n", cases);

	for (int caseNum = 1; caseNum <= cases; caseNum++) {
		int tx = -1;
		unsigned int ty = string::npos;

		getline(stream, board[0]);
		getline(stream, board[1]);
		getline(stream, board[2]);
		getline(stream, board[3]);
		getline(stream, line);

		ty = board[0].find_first_of("T");
		if (ty != string::npos) {
			tx = 0;
		} else {
			ty = board[1].find_first_of("T");
			if (ty != string::npos) {
				tx = 1;
			} else {
				ty = board[2].find_first_of("T");
				if (ty != string::npos) {
					tx = 2;
				} else {
					ty = board[3].find_first_of("T");
					if (ty != string::npos) {
						tx = 3;
					}
				}
			}
		}

		//printf("Case #%d: %d, %d\n", caseNum, tx, ty);

		int value = -1;

		if (tx != -1) {
			board[tx][ty] = 'X';
			value = checkBoard(board);

			if (value <= 0) {
				board[tx][ty] = 'O';
				value = checkBoard(board);
			}
		} else {
			value = checkBoard(board);
		}

		string result = "";

		switch(value) {
			case -1:
				result = "Game has not completed";
				break;
			case 0:
				result = "Draw";
				break;
			case 1:
				result = "X won";
				break;
			case 2:
				result = "O won";
				break;
			default:
				result = "Draw";
				break;
		}

		printf("Case #%d: %s\n", caseNum, result.c_str());
	}

	stream.close();

	return 0;
}
