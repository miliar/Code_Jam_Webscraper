#include <iostream>

using namespace std;

int main (int argc, char** argv) {

	int testCases;
	cin >> testCases;

	for (int test = 0; test < testCases; ++test) {

		int xOmino;
		cin >> xOmino;

		int rows;
		cin >> rows;

		int cols;
		cin >> cols;

		cout << "Case #" << test + 1 << ": ";

		int minDimension = min (rows, cols);
		int maxDimension = max (rows, cols);

		if ((rows < 1 || cols < 1) ||
			(rows * cols) % xOmino != 0 ||
			(rows < xOmino && cols < xOmino) ||
			(xOmino == 3 && minDimension < 2) ||
			(xOmino == 4 && minDimension < 2) ||
			(xOmino == 4 && minDimension == 2 && maxDimension >= 3)) {

			cout << "RICHARD" << endl;

		} else {

			cout << "GABRIEL" << endl;

		}

	}

	return 0;
}