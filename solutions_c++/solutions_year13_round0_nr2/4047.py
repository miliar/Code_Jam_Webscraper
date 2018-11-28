#include <iostream>

using namespace std;

int lawn[100][100];

bool solve(int rows, int cols) {
	for(int r = 0; r < rows; r++) {
		for(int c = 0; c < cols; c++) {
			bool rOK, cOK;
			rOK = cOK = true;
			for(int r2 = 0; r2 < rows; r2++) {
				if ( lawn[r][c] < lawn[r2][c] ) {
					rOK = false;
				}
			}
			for(int c2 = 0; c2 < cols; c2++) {
				if ( lawn[r][c] < lawn[r][c2] ) {
					cOK = false;
				}
			}
			if ( !(rOK || cOK ) ) return false;
		}
	}
	return true;
}

int main() {
	int numCases;
	cin >> numCases;

	for (int c = 1; c <= numCases; c++) {
		int rows, cols;
		cin >> rows >> cols;

		for (int r = 0; r < rows; r++) {
			for( int c = 0; c < cols; c++) {
				cin >> lawn[r][c];
			}
		}

		cout << "Case #" << c << ": " << (solve(rows, cols) ? "YES" : "NO") << endl;
	}

	return 1;
}