//============================================================================
// Name        : lawnmower.cpp
// Author      : swem
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	const int size = 100;
	int grid[size][size] = { { 0 } };
	int gridTranspose[size][size] = { { 0 } };
	int maxAlongRow[size] = { 0 };
	int maxAlongCol[size] = { 0 };

	int t = 0;
	cin >> t;
	for (int caseIdx = 1; caseIdx <= t; ++caseIdx) {
		int row, col;
		cin >> row >> col;
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				cin >> grid[i][j];
				gridTranspose[j][i] = grid[i][j];
			}
		}
		for (int i = 0; i < row; i++) {
			maxAlongRow[i] = *(max_element(grid[i], grid[i] + col));
		}
		for (int i = 0; i < col; i++) {
			maxAlongCol[i] = *(max_element(gridTranspose[i],
					gridTranspose[i] + row));
		}

		bool mowable = true;
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				if (grid[i][j] < maxAlongRow[i]
						&& gridTranspose[j][i] < maxAlongCol[j]) {
					mowable = false;
				}
			}
		}

		cout << "Case #" << caseIdx << ": ";
		if (mowable) {
			cout << "YES";
		} else {
			cout << "NO";
		}
		cout << endl;
	}
	return 0;
}
