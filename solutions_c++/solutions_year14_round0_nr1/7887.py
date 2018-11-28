#include <iostream>

using namespace std;

void Read(int& guess, int a[4][4]) {
	cin >> guess;
	guess--;
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			cin >> a[i][j];
}

void Solve() {
	int guess1;
	int a[4][4];
	Read(guess1, a);

	int guess2;
	int b[4][4];
	Read(guess2, b);

	int vals[16];
	memset(vals, 0, sizeof(vals));

	for (int j = 0; j < 4; ++j) {
		++vals[a[guess1][j] - 1];
		++vals[b[guess2][j] - 1];
	}
	
	int cnt = 0;
	int ind = 0;
	for (int i = 0; i < 16; ++i)
		if (vals[i] == 2) {
			++cnt;
			ind = i;
		}
	
	if (cnt == 0) {
		cout << "Volunteer cheated!" << endl;
		return;
	}
	if (cnt > 1) {
		cout << "Bad magician!" << endl;
		return;
	}
	cout << ind + 1 << endl;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		Solve();
	}
}