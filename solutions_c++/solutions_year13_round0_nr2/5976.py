#include <iostream>
#include <fstream>

using namespace std;

const int MAX_SIZE = 100;
const int MAX_HEIGHT = 2;

void initPattern(int pattern[][MAX_SIZE], int n, int m);
bool isMowable(int pattern[][MAX_SIZE], int n, int m);

int main(int argc, const char ** argv) {

	// Read the inputs
	ifstream inputFile;
	inputFile.open(argv[1]);

	int testCases;
	inputFile >> testCases;

	for (int i = 0; i < testCases && inputFile.good(); i++) {
		int n, m;
		int pattern[MAX_SIZE][MAX_SIZE];
	
		inputFile >> n >> m;	// Get dimensions

		// Initialize to 100
		initPattern(pattern, n, m);

		// Get Input
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < m; k++) {
				inputFile >> pattern[j][k];
			}
		}						

		if (isMowable(pattern, n, m)) {
			cout << "Case #" << (i+1) << ": YES" << endl;
		} else {
			cout << "Case #" << (i+1) << ": NO" << endl;
		}
	}

	return 0;
}

bool isMowable(int pattern[][MAX_SIZE], int n, int m) {
	if (n == 1 || m == 1) return true;	// Everything is valid in case of 1 col or 1 row.

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			// Find a 2
			if (pattern[i][j] == 2) {
				// Check the columns for 1, if found, check the entire column for 2
				for (int k = 0; k < m; k++) {
					if (pattern[i][k] == 1) {	// found 1, check the entire col
						for (int l = 0; l < n; l++) {
							if (pattern[l][k] == 2) {
								// Cage condition reached!
								return false;
							}
						}
					}
				}
			}
		}
	}

	return true;	// 2 was not found at all!
}

void initPattern(int pattern[][MAX_SIZE], int n, int m) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			pattern[i][j] = MAX_HEIGHT;
		}
	}
}