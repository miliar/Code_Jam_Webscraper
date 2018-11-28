#include <cstdio>
#include <math.h>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
	int c, cases;
	cin >> cases;
	
	for(c = 1; c <= cases; c++)	{
		int m, n;

		cin >> n;
		cin >> m;

		int array[n][m];
		int maxOfRow[n];
		int maxOfCol[m];

		for (int i = 0; i < n; i++) {
			maxOfRow[i] = 0;
		}
		for (int j = 0; j < m; j++) {
			maxOfCol[j] = 0;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> array[i][j];
				maxOfRow[i] = (array[i][j] > maxOfRow[i] ? array[i][j] : maxOfRow[i]);
				maxOfCol[j] = (array[i][j] > maxOfCol[j] ? array[i][j] : maxOfCol[j]);
			}
		}

		bool isPossible = true;;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (array[i][j] < maxOfRow[i] && array[i][j] < maxOfCol[j])
					isPossible = false;
			}
		}

		cout << "Case #" << c << ": ";
		cout << (isPossible ? "YES" : "NO") << '\n';
	}
}
