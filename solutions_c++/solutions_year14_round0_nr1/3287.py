#include <iostream>
using namespace std;

int choice[2][4];

int table[4][4];

int main() {
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++) {
		int first;
		cin >> first;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> table[i][j];
			}
		}
		memcpy(choice[0], table[first - 1], sizeof(choice[0]));
		int second;
		cin >> second;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> table[i][j];
			}
		}
		memcpy(choice[1], table[second - 1], sizeof(choice[1]));
		int ans = 0, match = 0;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++) {
				if (choice[0][i] == choice[1][j]) {
					match++;
					ans = choice[0][i];
				}
			}
		}
		cout << "Case #" << c << ": ";
		if (match > 1) {
			cout << "Bad magician!" << endl;
		} else if (match == 0) {
			cout << "Volunteer cheated!" << endl;
		} else {
			cout << ans << endl;
		}
	}
}