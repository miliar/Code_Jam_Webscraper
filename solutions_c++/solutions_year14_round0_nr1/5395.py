#include <bits/stdc++.h>
using namespace std;
void func() {
	int c[17] = {};
	for (int i = 0; i < 2; ++ i) {
		int x;
		cin >> x;
		for (int j = 1; j <= 4; ++ j) for (int k = 1; k <= 4; ++ k) {
			int y;
			cin >> y;
			if (x == j) ++ c[y];
		}
	}
	vector<int> a;
	for (int i = 1; i <= 16; ++ i) if (c[i] == 2) a.push_back(i);
	if (a.size() == 0) {
		cout << "Volunteer cheated!" << endl;
	} else if (a.size() == 1) {
		cout << a[0] << endl;
	} else {
		cout << "Bad magician!" << endl;
	}
}
int main() {
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++ tt) {
		cout << "Case #" << tt << ": ";
		func();
	}
}
