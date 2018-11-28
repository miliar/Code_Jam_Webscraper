#include <iostream>
#include <string>
using namespace std;
int n;
string mas[4];
int main () {
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);
	cin >> n;
	for (int k = 1; k <= n; k++) {
		for (int i = 0; i < 4; i++) {
			cin >> mas[i];
		}
		bool winner = 0;
		int dot = 0;
		for (int i = 0; i < 4; i++) {
			int t = 0, x = 0, o = 0;
			int t1 = 0, x1 = 0, o1 = 0;
			int t2 = 0, x2 = 0, o2 = 0;
			int t3 = 0, x3 = 0, o3 = 0;
			for (int j = 0; j < 4; j++) {
				if (mas[i][j] == '.') {
					dot++;
				}
				if (mas[i][j] == 'X') {
					x++;
				}
				if (mas[i][j] == 'O'){
					o++;
				}
				if (mas[i][j] == 'T') {
					t++;
				}

				if (mas[j][i] == 'X') {
					x1++;
				}
				if (mas[j][i] == 'O') {
					o1++;
				}
				if (mas[j][i] == 'T') {
					t1++;
				}

				if (mas[j][j] == 'X') {
					x2++;
				}
				if (mas[j][j] == 'O') {
					o2++;
				}
				if (mas[j][j] == 'T') {
					t2++;
				}

				if (mas[j][4 - j - 1] == 'X') {
					x3++;
				}
				if (mas[j][4 - j - 1] == 'O') {
					o3++;
				}
				if (mas[j][4 - j - 1] == 'T') {
					t3++;
				}
			}
			if ((x1 + t1) == 4 || (x + t) == 4) {
				cout << "Case #" << k << ": X won" << endl;
				winner = 1;
				break;
			} else if ((o1 + t1) == 4 || (o + t) == 4) {
				cout << "Case #" << k << ": O won" << endl;
				winner = 1;
				break;
			} else if ((x2 + t2) == 4 || (x3 + t3) == 4) {
				cout << "Case #" << k << ": X won" << endl;
				winner = 1;
				break;
			} else if ((o2 + t2) == 4 || (o3 + t3) == 4) {
				cout << "Case #" << k << ": O won" << endl;
				winner = 1;
				break;
			}
		}
		if (!winner) {
			if (dot) {
				cout << "Case #" << k << ": Game has not completed" << endl;
			} else {
				cout << "Case #" << k << ": Draw" << endl;
			}
		}
	}
	return 0;
}