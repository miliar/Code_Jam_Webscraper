#include <iostream>
#include <vector>
using namespace std;

int main () {
	int T;
	cin >> T;

	for (int i = 1; i <= T; ++i) {
		vector <int> row (4);

		int r1, r2, count = -1, card;
		cin >> r1;

		for (int j = 1; j < 5; ++j) {
			for (int k = 0; k < 4; ++k) {
				int c;
				cin >> c;
				if (j == r1) {
					row[k] = c;
				}
			}
		}

		cin >> r2;

		for (int j = 1; j < 5; ++j) {
			for (int k = 0; k < 4; ++k) {
				int c;
				cin >> c;
				if (j == r2) {
					for (int l = 0; l < 4; ++l) {
						if (c == row[l]) {
							card = c;
							++count;
						}
					}
				}
			}
		}

		if (count == 0)	cout << "Case #" << i << ": " << card << endl;
		else if (count < 0) cout << "Case #" << i << ": " << "Volunteer cheated!" << endl;
		else cout << "Case #" << i << ": " << "Bad magician!" << endl;
	}
}