#include <iostream>
using namespace std;

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		int i, j;
		int row1, row2;
		int a[4][4], b[4][4];
		int matches, match;
		cin >> row1;
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++)
				cin >> a[i][j];
		cin >> row2;
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++)
				cin >> b[i][j];
		// compare a[row1 - 1] to b[row2 - 1]
		matches = 0;
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++) {
				if (a[row1 - 1][i] == b[row2 - 1][j]) {
					matches++;
					match = a[row1 - 1][i];
				}
			}
		
		cout << "Case #" << icase << ": ";
		if (matches == 0)
			cout << "Volunteer cheated!";
		else if (matches == 1)
			cout << match;
		else
			cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}
