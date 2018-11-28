#include <iostream>
using namespace std;

int grass[100][100];

inline bool checkSquare(int r, int c, int n, int m) {
	bool isValid = true;
	int h = grass[r][c];

	for(int i = 0; i < n; i++) {
		if (grass[i][c] > h) {
			isValid = false;
			break;
		}
	}
	
	if (!isValid) {
		isValid = true;
		for(int j = 0; j < m; j++) {
			if (grass[r][j] > h) {
				isValid = false;
				break;
			}
		}
	}
	
	return isValid;
}

int main(void) {
	int numCases, n, m;
	
	cin >> numCases;
	for (int numCase = 1; numCase <= numCases; numCase++) {
		cin >> n >> m;
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> grass[i][j];
			}
		}
		
		bool isPossible = true;
		for (int i = 0; i < n && isPossible; i++) {
			for (int j = 0; j < m && isPossible; j++) {
				isPossible = checkSquare(i, j, n, m);
			}
		}
		
		cout << "Case #" << numCase << ": " << (isPossible ? "YES" : "NO") << endl;
	}
}
