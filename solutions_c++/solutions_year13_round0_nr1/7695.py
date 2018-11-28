#include <iostream>
using namespace std;

enum STATE {
	X, O, Draw, NC
};

void check(char arr[][4]) {
	STATE status = Draw;
	for (int i = 0; i < 4; i++) {
		char start = arr[i][0];
		if (start == '.') {
			status = NC;
			continue;
		}
		int j = 1;
		for (; j < 4; j++) {
			if (arr[i][j] == '.') {
				status = NC;
				break;
			}

			if (arr[i][j] != start && arr[i][j] != 'T')
				break;
		}
		if (j < 4)
			continue;
		else {
			cout << (char) toupper(start) << " won" << endl;
			return;
		}
	}

	for (int j = 0; j < 4; j++) {
		char start = arr[0][j];
		if (start == '.') {
			status = NC;
			continue;
		}
		int i = 1;
		for (; i < 4; i++) {
			if (arr[i][j] == '.') {
				status = NC;
				break;
			}
			if (arr[i][j] != start && arr[i][j] != 'T')
				break;
		}
		if (i < 4)
			continue;
		else {
			cout << (char) toupper(start) << " won" << endl;
			return;
		}
	}

	char start = arr[0][0];
	if (start == '.') {
		status = NC;
	} else {
		int i = 1;
		for (; i < 4; i++) {
			if (arr[i][i] == '.') {
				status = NC;
				break;
			}
			if (arr[i][i] != start && arr[i][i] != 'T')
				break;
		}
		if (i == 4) {
			cout << (char) toupper(start) << " won" << endl;
			return;
		}
	}

	start = arr[0][3];
	if (start == '.') {
		status = NC;
	} else {
		int i = 1;
		for (; i < 4; i++) {
			if (arr[3 - i][i] == '.') {
				status = NC;
				break;
			}
			if (arr[3 - i][i] != start && arr[3 - i][i] != 'T')
				break;
		}
		if (i == 4) {
			cout << (char) toupper(start) << " won" << endl;
			return;
		}
	}

	if (status == Draw) {
		cout << "Draw" << endl;
	} else {
		cout << "Game has not completed" << endl;
	}
}

int main() {
	int T;
	cin >> T;
	for (int k = 0; k < T; k++) {
		char arr[4][4];
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> arr[i][j];
			}
		}

		cout << "Case #" << (k + 1) << ": ";
		check(arr);
		if (k < T - 1) {
			cin.ignore();
			string tmp;
			getline(cin, tmp);
		}
	}
	return 1;
}
