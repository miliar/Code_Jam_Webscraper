#include <iostream>
using namespace std;

int main() {
	int testCases;
	cin >> testCases;

	int firstCards[16];
	int secondCards[16];

	for (int i = 1; i <= testCases; ++i) {
		int firstAns, secondAns;
		cin >> firstAns;

		for (int j = 0; j < 16; ++j) {
			cin >> firstCards[j];
		}

		cin >> secondAns;

		for (int j = 0; j < 16; ++j) {
			cin >> secondCards[j];
		}

		cout << "Case #" << i << ": ";

		int result = false;
		int bad = false;
		int match;
		for (int m=0; m<4; ++m) {
			for (int n=0; n<4; ++n) {
				if (firstCards[(firstAns - 1)*4 + m] == secondCards[(secondAns - 1)*4 + n]) {
					if (result) {
						bad = true;
					} else {
						result = true;
						match = firstCards[(firstAns - 1)*4 + m];
					}
				}
			}
		}

		if (bad) {
			cout << "Bad magician!" << endl;
		} else if (result) {
			cout << match << endl;
		}
		else {
			cout << "Volunteer cheated!" << endl;
		}
	}

	return 0;
}
