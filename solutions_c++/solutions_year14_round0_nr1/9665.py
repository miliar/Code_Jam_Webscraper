//============================================================================
// Name        : CodeJam-2014.cpp
// Author      : Maysoun Hindawi
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
#define N 4
#define NUM 16
void getMatrix(int matrix[][N]) {
	for (int row = 0; row < N; row++) {
		for (int col = 0; col < N; col++) {
			cin >> matrix[row][col];
		}
	}
}

void countNumbers(int* results, int matrix[][N], int rowNum) {
	for (int col = 0; col < N; col++) {
		results[matrix[rowNum -1][col] -1 ]++;
	}

}

int checkCounters(int* results) {
	int count = 0;
	for (int col = 0; col < NUM; col++) {
		if (results[col] > 2)
			return -2;
		if (results[col] == 2)
			count++;
	}
	if (count == 0)
		return -1;
	if (count > 1)
		return -2;

	for (int col = 0; col < NUM; col++) {
		if (results[col] == 2)
			return col + 1;
	}
}

int main() {
	int cases;
	cin >> cases;
	int *results = new int[cases];

	for (int counter = 0; counter < cases; counter++) {
		int matrix[N][N];
		int counters[NUM] = { };
		int firstRow;
		int secondRow;

		cin >> firstRow;
		getMatrix(matrix);
		countNumbers(counters, matrix, firstRow);

		cin >> secondRow;
		getMatrix(matrix);
		countNumbers(counters, matrix, secondRow);

		results[counter] = checkCounters(counters);
	}

	for (int counter = 0; counter < cases; counter++) {
		cout << "Case #" << (counter + 1) << ": ";
		switch (results[counter]) {
		case -2: {
			cout << "Bad magician!";
			break;
		}
		case -1: {
			cout << "Volunteer cheated!";
			break;
		}
		default: {
			cout << results[counter];
			break;
		}
		}
		cout << endl;
	}

	return 0;
}
