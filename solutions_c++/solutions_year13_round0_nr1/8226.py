// CodeJam2013.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <iostream>

using namespace std;

void finish(int testCaseIndex, char mark, bool gameFinished, ofstream &outputFS) {
	outputFS << "Case #" << testCaseIndex << ": ";
	if (mark == 'X') {
		outputFS << "X won";
	} else if (mark == 'O') {
		outputFS << "O won";
	} else if (gameFinished) {
		outputFS << "Draw";
	} else {
		outputFS << "Game has not completed";
	}
	outputFS << endl;
}

void processTestCase(int testCaseIndex, char **board, ofstream &outputFS) {
			bool gameFinished = true;
			for (int y = 0; y < 4; ++y) {
				char mark = ' ';
				bool win = true;
				for (int x = 0; x < 4; ++x) {
					if (board[y][x] == '.') {
						gameFinished = false;
						win = false;
						break;
					}
					if ((mark != ' ') && (mark != board[y][x]) && (mark != 'T') && (board[y][x] != 'T')) {
						win = false;
						break;
					} else {
						if ((mark == ' ') || ((mark == 'T') && ((board[y][x] == 'X') || (board[y][x] == 'O')))) {
							mark = board[y][x];
						}
					}
				}

				if (win) {
					finish(testCaseIndex, mark, gameFinished, outputFS);
					return;
				}
			}

			for (int x = 0; x < 4; ++x) {
				char mark = ' ';
				bool win = true;
				for (int y = 0; y < 4; ++y) {
					if (board[y][x] == '.') {
						gameFinished = false;
						win = false;
						break;
					}
					if ((mark != ' ') && (mark != board[y][x]) && (mark != 'T') && (board[y][x] != 'T')) {
						win = false;
						break;
					} else {
						if ((mark == ' ') || ((mark == 'T') && ((board[y][x] == 'X') || (board[y][x] == 'O')))) {
							mark = board[y][x];
						}
					}
				}

				if (win) {
					finish(testCaseIndex, mark, gameFinished, outputFS);
					return;
				}
			}

			char mark = ' ';
			bool win = true;
			for (int x = 0; x < 4; ++x) {
				int y = x;
				if (board[y][x] == '.') {
					gameFinished = false;
					win = false;
					break;
				}
				if ((mark != ' ') && (mark != board[y][x]) && (mark != 'T') && (board[y][x] != 'T')) {
						win = false;
						break;
					} else {
						if ((mark == ' ') || ((mark == 'T') && ((board[y][x] == 'X') || (board[y][x] == 'O')))) {
							mark = board[y][x];
						}
					}
			}

			if (win) {
					finish(testCaseIndex, mark, gameFinished, outputFS);
					return;
				}

			mark = ' ';
			win = true;
			for (int x = 0; x < 4; ++x) {
				int y = 3 - x;
				if (board[y][x] == '.') {
					gameFinished = false;
					win = false;
					break;
				}
				if ((mark != ' ') && (mark != board[y][x]) && (mark != 'T') && (board[y][x] != 'T')) {
						win = false;
						break;
					} else {
						if ((mark == ' ') || ((mark == 'T') && ((board[y][x] == 'X') || (board[y][x] == 'O')))) {
							mark = board[y][x];
						}
				}
			}

			if (win) {
					finish(testCaseIndex, mark, gameFinished, outputFS);
					return;
				}

			finish(testCaseIndex, ' ', gameFinished, outputFS);
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inputFS;
	inputFS.open("input.txt");

	ofstream outputFS;
	outputFS.open("output.txt");

	if (inputFS.is_open()) {
		string line;
		getline(inputFS, line);
		int numTestCases = atoi(line.c_str());
		for (int testCase = 0; testCase < numTestCases; ++testCase) {
			char **board = new char *[4];
			for (int y = 0; y < 4; ++y) {
				board[y] = new char[4];
			}
			for (int testCaseLineIndex = 0; testCaseLineIndex < 4; ++testCaseLineIndex) {
				getline(inputFS, line);
				for (int charIndex = 0; charIndex < 4; ++charIndex) {
					board[testCaseLineIndex][charIndex] = line[charIndex];
				}
			}
			getline(inputFS, line);
			processTestCase(testCase + 1, board, outputFS);
		}
		inputFS.close();
		outputFS.close();
	}

	return 0;
}
