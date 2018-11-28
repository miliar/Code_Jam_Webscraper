//============================================================================
// Name        : Lawnmower.cpp
// Author      : Jeongseok Son
// Version     :
// Copyright   : GNU LGPL
// Description : Google Code Jam Problem B. Lawnmower
//============================================================================

#include <iostream>

#define SIZE 100

using namespace std;

int main() {
	int cases;
	int lawn[SIZE][SIZE];

	cin >> cases;
	for(int c = 1; c <= cases; c++) {
		int i, j, n, m;
		cin >> n >> m;

		int *rMax = new int[n]();
		int *cMax = new int[m]();

		for(i = 0; i < n; i++) {
			for(j = 0; j < m; j++) {
				cin >> lawn[i][j];
				if(lawn[i][j] > rMax[i])
					rMax[i] = lawn[i][j];
				if(lawn[i][j] > cMax[j])
					cMax[j] = lawn[i][j];
			}
		}

		for(i = 0; i < n; i++) {
			for(j = 0; j < m; j++) {
				if(lawn[i][j] < rMax[i] && lawn[i][j] < cMax[j]) {
					cout << "Case #" << c << ": NO" << endl;
					goto out;
				}
			}
		}
out:
		if (i == n && j == m)
			cout << "Case #" << c << ": YES" << endl;

		delete[] rMax;
		delete[] cMax;
	}
	return 0;
}
