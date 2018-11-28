// minesweeper.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#define SIZE 10

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ofstream fout("C-small-attempt1.out");
	ifstream fin("C-small-attempt1.in");

	int cases;
	fin >> cases;

	for (int i = 1; i <= cases; i++) {
		bool possible = false;
		int rows, columns, mines;
		fin >> rows >> columns >> mines;

		int spaces = rows * columns - mines;

		if (rows == 1 || columns == 1) {
			possible = true;
		}

		else if (spaces == 1) {
			possible = true;
		}

		// Can't have odd with 2 rows/columns
		else if ((rows == 2 || columns == 2) && spaces % 2 == 1) {
			possible = false;
		}

		else if (spaces >= 4) {
			if (spaces == 5 || spaces == 7)
				possible = false;
			else
				possible = true;
		}

		fout << "Case #" << i << ":\n";

		if (!possible) {
			fout << "Impossible\n";
		}

		else {
			char sweep[10][10];
			for (int j = 0; j < SIZE; j++) {
				for (int k = 0; k < SIZE; k++) {
					sweep[j][k] = '\0';
				}
			}
			int side = ceil(sqrt(spaces));
			int count = 0;
			int lineCount = 0;
			bool reverse = false; // We build the board vertically. If the board is horizontally long, we need to flip it.
			if (rows < columns)
				reverse = true;

			// If we can fit a square, make a square.
			// If not, add rows until we can fit a square.
			if (rows < side || columns < side) {
				side = fmin(rows, columns);

				while (ceil(sqrt(spaces)) > side) {
					for (int j = 0; j < side; j++) {
						if (j == 0 && lineCount == 0) sweep[lineCount][j] = 'c';
						else sweep[lineCount][j] = '.';
						spaces--;
					}
					lineCount++;
				}

				for (int j = 0; j < side; j++) { // First row of square
					sweep[lineCount][j] = '.';
					spaces--;
				}
				lineCount++;

				for (int j = 0; j < side; j++) {
					for (int k = 0; k < side - 1; k++) {
						if (spaces > 0) {
							sweep[lineCount + k][j] = '.';
							spaces--;
						}

						else
							sweep[lineCount + k][j] = '*';
					}
				}
				lineCount += side - 1;
			}

			else {
				for (int k = 0; k < side; k++) {
					if (k == 0 && lineCount == 0) sweep[lineCount][k] = 'c';
					else sweep[lineCount][k] = '.';
					spaces--;
				}
				lineCount++;

				for (int j = 0; j < side - 1; j++) {
					for (int k = 0; k < side - j; k++) {
						if (spaces > 0) {
							sweep[lineCount][k] = '.';
							spaces--;
							
							if (spaces == 1 && k == side - j - 1) {
								sweep[lineCount][k + 1] = '.';
								spaces--;
							}
						}

						else
							sweep[lineCount][k] = '*';
					}
					lineCount++;
				}
			}

			for (int j = 0; j < fmax(rows, columns); j++) {
				for (int k = 0; k < fmin(rows, columns); k++) {
					if (sweep[j][k] != '.' && sweep[j][k] != '*' && sweep[j][k] != 'c') {
						if (spaces > 0) {
							sweep[j][k] = '.';
							spaces--;
						}

						else
							sweep[j][k] = '*';
					}
				}
			}

			if (reverse) {
				for (int j = 0; j < fmin(rows, columns); j++) {
					for (int k = 0; k < fmax(rows, columns); k++) {
						fout << sweep[k][j];
					}
					fout << '\n';
				}
			}

			else {
				for (int j = 0; j < fmax(rows, columns); j++) {
					for (int k = 0; k < fmin(rows, columns); k++) {
						fout << sweep[j][k];
					}
					fout << '\n';
				}
			}
		}
	}
}
