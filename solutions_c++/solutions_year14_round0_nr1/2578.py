#include <iostream>
#include <cstring>

using namespace std;

int mark[17];

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		cout << "Case #" << test << ": ";
		memset(mark, 0, sizeof(mark));
		for (int q = 1; q <= 2; ++q) {
			int row; cin >> row;
			for (int i = 1; i <= 4; ++i)
				for (int j = 1; j <= 4; ++j) {
					int x; cin >> x;
					if (row == i) mark[x]++;
				}
		}
		int cnt = 0;
		for (int i = 1; i <= 16; ++i)
			if (mark[i] == 2)
				++cnt;
		if (cnt == 1) {
			for (int i = 1; i <= 16; ++i)
				if (mark[i] == 2)
					cout << i << endl;
		} else if (cnt > 1) {
			cout << "Bad magician!" << endl;
		} else {
			cout << "Volunteer cheated!" << endl;
		}
	}
	return 0;
}