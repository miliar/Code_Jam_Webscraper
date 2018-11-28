#include <iostream>
#include <string>

using namespace std;

int main() {
//	freopen("input.txt", "r", stdin);
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("D-small-attempt2.out", "w", stdout);
	int t, T, i, j, r, c, x;
	string name;
	cin >> T;

	for (t = 0; t < T; ++t) {
		name = "GABRIEL";
		cin >> x >> r >> c;
		if (r * c % x || (x + 1) / 2 > r || (x + 1) / 2 > c || (x > r && x > c) || (x == 4) && (r < 3 || c < 3)) name = "RICHARD";
		cout << "Case #" << t + 1 << ": " << name << endl;
	}
	return 0;
}