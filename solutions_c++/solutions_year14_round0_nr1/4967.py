//In the name of God
#include <algorithm>
#include <iostream>
using namespace std;

int a[4][4], b[4][4], ans, ls, r1, r2;

int main() {
	int test;
	cin >> test;
	for (int c = 1; c <= test; c++) {
		ans = 0;
		cin >> r1; r1--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> a[i][j];
		cin >> r2; r2--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> b[i][j];
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (a[r1][i] == b[r2][j]) {
					ans++, ls = a[r1][i];
					break;
				}
		cout << "Case #" << c << ": ";
		if (ans > 1)
			cout << "Bad magician!\n";
		else if (ans == 1)
			cout << ls << '\n';
		else
			cout << "Volunteer cheated!\n";
	}
	return 0;
}
