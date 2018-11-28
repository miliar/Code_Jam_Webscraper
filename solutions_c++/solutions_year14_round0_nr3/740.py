#include <iostream>
#include <cmath>

using namespace std;

void answer(int r, int c, int free, int x, int y) {

	char table[50][50];

	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			table[i][j] = '*';
		}
	}

	for (int i = 0; i < x; i++) {
		for (int j = 0; j < y; j++) {
			table[i][j] = '.';
		}
	}

	free -= x * y;

	if (free < 4) {
		for (int i = 0; i < free; i++) {
			table[x][i] = '.';
		}

		free = 0;
	}

	for (int i = 0; i <= max(x, y); i++) {
		if (free > 0 && i < x) {
			table[i][y] = '.';
			free--;
		}

		if (free > 0 && i < y) {
			table[x][i] = '.';
			free--;
		}
	}

	table[0][0] = 'c';

	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cout << table[i][j];
		}

		cout << endl;
	}

}

int main() {
	int t;
	cin >> t;

	for (int test = 1; test <= t; test++) {
		int r, c, m;
		cin >> r >> c >> m;
		int free = r * c - m;

		cout << "Case #" << test << ":" << endl;

		if (free == 1) {
			for (int i = 0; i < r; i++) {
				for (int j = 0; j < c; j++) {
					if (i == 0 && j == 0) {
						cout << "c";
					} else {
						cout << "*";
					}
				}

				cout << endl;
			}
		
		} else if (r == 1) {
			for (int i = 0; i < m; i++) {
				cout << "*";
			}

			for (int i = m; i < c - 1; i++) {
				cout << ".";
			}

			cout << "c" << endl;
		
		} else if (c == 1) {
			for (int i = 0; i < m; i++) {
				cout << "*" << endl;
			}

			for (int i = m; i < r - 1; i++) {
				cout << "." << endl;
			}

			cout << "c" << endl;
		
		} else {
			for (int x = 2; x <= r; x++) {
				int y = ceil((double)free / x);

				if (x == 3 && y == 3 && free == 7) {
					continue;
				}

				if (y > 1 && y <= c && free == x * y) {
					answer(r, c, free, x, y);
					goto next_test;
				}

				if (x > 2 && y > 2 && y <= c && free - (x - 1) * (y - 1) != 1) {
					answer(r, c, free, x - 1, y - 1);
					goto next_test;
				}
			}

			cout << "Impossible" << endl;
		}

		next_test:;
	}
}