/*
  Google Code Jam 2013
  Problem B
  Coded by Michael Oliver
*/
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef vector<string> vs;

int main() {
	int num_cases;
	cin >> num_cases;
	for (int i=1; i <= num_cases; i++) {
		bool fail = false;
		int n, m;
		cin >> n >> m;
		int lawn[100][100];
		int row_maxes[100];
		for (int j=0; j < 100; j++) row_maxes[j] = 0;
		int row_mins[100];
		for (int j=0; j < 100; j++) row_mins[j] = 101;
		int col_maxes[100];
		for (int j=0; j < 100; j++) col_maxes[j] = 0;
		int col_mins[100];
		for (int j=0; j < 100; j++) col_mins[j] = 101;
		for (int j=0; j < n; j++) {
			for (int k=0; k < m; k++) {
				cin >> lawn[j][k];
				if (lawn[j][k] < row_mins[j]) row_mins[j] = lawn[j][k];
				if (lawn[j][k] > row_maxes[j]) row_maxes[j] = lawn[j][k];
				if (lawn[j][k] < col_mins[k]) col_mins[k] = lawn[j][k];
				if (lawn[j][k] > col_maxes[k]) col_maxes[k] = lawn[j][k];
			}
		}
		
		// Check rows
		for (int j=0; j < n; j++) { // For each row
			// If there's an element in the row less then ends
			if ((row_mins[j] < lawn[j][0]) || (row_mins[j] < lawn[j][m-1])) {
				// Find these elements
				for (int k=0; k < m; k++) { // For each column
					if (lawn[j][k] == row_mins[j]) { // If pass, this is an element
						// Check its column ends to see it's valid
						if ((lawn[j][k] < col_maxes[k]) || (lawn[j][k] < lawn[n-1][k])) {
							// Found invalid
							fail = true;
							break;
						}
					}
				}
				if (fail) break;
			} else if ((row_maxes[j] > lawn[j][0]) || (row_maxes[j] > lawn[j][m-1])) {
				for (int k=0; k < m; k++) { // For each column
					if (lawn[j][k] == row_mins[j]) { // If pass, this is an element
						// Check its column ends to see it's valid
						if ((lawn[j][k] > col_mins[k]) || (lawn[j][k] > lawn[n-1][k])) {
							// Found invalid
							fail = true;
							break;
						}
					}
				}
				if (fail) break;
			}
		}
		if (fail) {
			cout << "Case #" << i << ": NO" << endl;
		/*for (int j=0; j < n; j++) {
			for (int k=0; k < m; k++) {
				cout << lawn[j][k] << " ";
			}
			cout << endl;
		}*/
			continue;
		}
		
		// Check cols
		for (int j=0; j < m; j++) { // For each col
			// If there's an element in the col less then ends
			if ((col_mins[j] < lawn[0][j]) || (col_mins[j] < lawn[n-1][j])) {
				// Find these elements
				for (int k=0; k < n; k++) { // For each row
					if (lawn[k][j] == col_mins[j]) { // If pass, this is an element
						// Check its row ends to see it's valid
						if ((lawn[k][j] < row_maxes[k]) || (lawn[k][j] < lawn[k][m-1])) {
							// Found invalid
							fail = true;
							break;
						}
					}
				}
				if (fail) break;
			} else if ((col_maxes[j] > lawn[0][j]) || (col_maxes[j] > lawn[n-1][j])) {
				for (int k=0; k < n; k++) { // For each row
					if (lawn[k][j] == col_mins[j]) { // If pass, this is an element
						// Check its row ends to see it's valid
						if ((lawn[k][j] > row_mins[k]) || (lawn[k][j] > lawn[k][m-1])) {
							// Found invalid
							fail = true;
							break;
						}
					}
				}
				if (fail) break;
			}
		}
		if (fail) {
			cout << "Case #" << i << ": NO" << endl;
		} else {
			cout << "Case #" << i << ": YES" << endl;
		}
		/*for (int j=0; j < n; j++) {
			for (int k=0; k < m; k++) {
				cout << lawn[j][k] << " ";
			}
			cout << endl;
		}*/
	}
	return 0;
}
