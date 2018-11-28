#include <iostream>

using namespace std;

bool exists(int* arr, int find) {
	for (int i = 0; i < 4; i++) {
		if (arr[i] == find) {
			return true;
		}
	}
	return false;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		int row1;
		int table1[4][4];
		cin >> row1;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> table1[i][j];
			}
		}

		int row2;
		int table2[4][4];
		cin >> row2;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> table2[i][j];
			}
		}
		bool ok = true;
		int answer = 0;
		for (int j = 0; j < 4; j++) {
			if (exists(table1[row1-1], table2[row2-1][j])) {
				if (answer != 0) {
					ok = false;
					break;
				}
				answer = table2[row2-1][j];
			}
		}
		if (!ok) {
			cout << "Bad magician!";
		}
		else if (answer == 0) {
			cout << "Volunteer cheated!";
		}
		else {
			cout << answer;
		}
		cout << endl;
	}
	return 0;
}