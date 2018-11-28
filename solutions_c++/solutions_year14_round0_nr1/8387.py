#include <iostream>
using namespace std;

int main() {
	int line[4];
	int T;
	int i, j, k, l, x;
	int matchCount;
	int magic;
	int a1, a2;
	cin >> T;
	for (i = 0; i < T; i++) {
		// Read 1st answer & 1st card arrangement
		cin >> a1;
		for (j = 0; j < 4; j++) {
			if (j + 1 == a1) {
				// remember this line
				for (k = 0; k < 4; k++) {
					cin >> line[k];
				}
			}
			else {
				// just skip this line
				for (k = 0; k < 4; k++) {
					cin >> x;
				}
			}
		}
		// Read 2nd answer & 2nd card arrangement
		cin >> a2;
		for (j = 0; j < 4; j++) {
			if (j + 1 == a2) {
				// check this line
				matchCount = 0;
				for (k = 0; k < 4; k++) {
					cin >> x;
					for (l = 0; l < 4; l++) {
						if (line[l] == x) {
							matchCount++;
							magic = x;
							break;
						}
					}
				}
				cout << "Case #" << i+1 << ": ";
				if (matchCount == 0)
					cout << "Volunteer cheated!" << endl;
				else if (matchCount == 1)
					cout << magic << endl;
				else
					cout << "Bad magician!" << endl;
			}
			else {
				// skip this line
				for (k = 0; k < 4; k++)
					cin >> x;
			}
		}
	}

	return 0;
}
