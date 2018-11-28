#include <iostream>
#include <fstream>
using namespace std;

const int N = 4;

int main()
{
	int cases;
	int A1[N][N];
	int A2[N][N];
	int row1, row2;

	cin >> cases;

	for (int i = 1; i < cases + 1; i++) {
		cin >> row1;
		row1--;
		for (int row = 0; row < N; row++)
			for (int col = 0; col < N; col++)
				cin >> A1[row][col];
		cin >> row2;
		row2--;
		for (int row = 0; row < N; row++)
		for (int col = 0; col < N; col++)
			cin >> A2[row][col];

		/* Find collisions */
		int curCompare;
		int foundVal = 0, foundTotal = 0;
		for (int col1 = 0; col1 < N; col1++) {
			curCompare = A1[row1][col1];
			for (int col2 = 0; col2 < N; col2++) {
				if (curCompare == A2[row2][col2]) {
					foundVal = curCompare;
					foundTotal++;
				}
			}
		}

		cout << "Case #" << i << ": ";
		switch (foundTotal)
		{
		case 0:
			cout << "Volunteer cheated!" << endl;
			break;
		case 1:
			cout << foundVal << endl;
			break;
		default:
			cout << "Bad magician!" << endl;
			break;
		}
	}
}