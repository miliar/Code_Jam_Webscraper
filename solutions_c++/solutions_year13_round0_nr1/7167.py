#include <iostream>

using namespace std;

char board[4][4];

bool emptyFields;

char evaldir(int sx, int sy, int dx, int dy) {
	if (board[sy][sx] == 'T') {
		sx += dx;
		sy += dy;
	}
	char prev = board[sy][sx];
	while (0 <= (sy += dy) && sy < 4 &&
				 0 <= (sx += dx) && sx < 4) {
		char cur = board[sy][sx];
		if (cur == 'T') {
			continue;
		} else if (cur != prev || cur == '.') {
				return false;
		} else {
			prev = cur;
		}
	}
	return prev;
}

void evalboard() {
	char ret;
	for (int i = 0; i < 4; i++) {
		if ((ret = evaldir(0, i, 1, 0)) ||
		    (ret = evaldir(i, 0, 0, 1))) {
			cout << ret << " won" << endl;
			return;
		}
	}
	
	if ((ret = evaldir(3, 3, -1, -1)) ||
	    (ret = evaldir(3, 0, -1, 1))) {
		cout << ret << " won" << endl;
		return;
	}
	if (emptyFields) {
		cout << "Game has not completed" << endl;
	} else {
		cout << "Draw" << endl;
	}
	
	return;
}

int main() {
	int tc; cin >> tc; cin.ignore(3, '\n');
	int ctc = 0;
	while (ctc++ < tc) {
		emptyFields = false;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				board[i][j] = cin.get();
				if (board[i][j] == '.') {
					emptyFields = true;
				}
			}
			cin.ignore(3, '\n');
		}
		cin.ignore(3, '\n');
		cout << "Case #" << ctc << ": "; evalboard();
	}
}
