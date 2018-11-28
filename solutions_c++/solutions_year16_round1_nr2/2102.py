// rank.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
using namespace std;

int square[50][50];
int input[100][50];
int unmatchedInputIndex;

void clearSquare();
int computeDiagonal(int row);
void mapUnmatchedInput(int row, int unmatchedInputIndex, int missingRow);

int main()
{
	int t;
	int row;
	int missingRow;

	cin >> t;


	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ":";

		cin >> row;

		clearSquare();

		for (int x = 0; x < 2 * row - 1; x++) {
			for (int y = 0; y < row; y++) {
				cin >> input[x][y];
			}
		}

		unmatchedInputIndex = -1;
		missingRow = computeDiagonal(row);

		/*
		cout << "\n";
		for (int x = 0; x < 2 * row - 1; x++) {
			for (int y = 0; y < row; y++) {
				cout << " " << input[x][y];
			}
			cout << "\n";
		}
		*/

		//cout << "Index of missing row? " << missingRow << "\n";
		//cout << "unmatchedInputIndex? " << unmatchedInputIndex << "\n";
		/*
		for (int j = 0; j < row; j++) {
			cout << " " << input[unmatchedInputIndex][j];
		}
		*/

		mapUnmatchedInput(row, unmatchedInputIndex, missingRow);

		cout << "\n";
	}

	return 0;
}

void mapUnmatchedInput(int row, int unmatchedInputIndex, int missingRow)
{
	int value1, value2;
	for (int j = 0; j < row; j++) {
		int diagonal = square[j][j];
		value1 = -1;
		value2 = -1;
		for (int k = 0; k < 2 * row - 1; k++) {
			if (input[k][j] == diagonal) {
				if (value1 == -1) {
					value1 = input[k][missingRow];
				}
				else {
					value2 = input[k][missingRow];
				}
			}
		}
		//cout << value1 << " " << value2 << "\n";
		//cout << "Row " << j << ":";
		cout << " ";
		if (value1 == value2) {
			cout << value1;
		}
		else if (value2 == -1) {
			cout << value1;
		}
		else if (value2 == input[unmatchedInputIndex][j]) {
			cout << value1;
		}
		else {
			cout << value2;
		}
	}
}


int computeDiagonal(int row)
{
	int missingRow = -1;
	int min;
	int count;

	bool skipRow[100] = { false };

	//cout << "\n" << "Diagonal:";

	for (int i = 0; i < row; i++) {
		min = 3000; // max height 2500
		for (int j = 0; j < 2*row - 1; j++) {
			if (!skipRow[j] && input[j][i] < min)
			{
				min = input[j][i];
			}
		}
		square[i][i] = min;

		//cout << " " << square[i][i];

		count = 0;
		int minIndex = -1;
		for (int j = 0; j < 2 * row - 1; j++) {
			if (!skipRow[j] && input[j][i] == min)
			{
				skipRow[j] = true;
				count++;
				minIndex = j; // will not be overwritten if only once
			}
		}
		if (count != 2) {
			missingRow = i;
			unmatchedInputIndex = minIndex;
		}

	}

	return missingRow;
}

void clearSquare()
{
	for (int x = 0; x < 50; x++) {
		for (int y = 0; y < 50; y++) {
			square[x][y] = 0;
		}
	}
}



