#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

void solve() {
	int X, R, C; cin >> X >> R >> C;
	if (R > C) swap(R, C);
	
	bool ok = R * C % X == 0;
	ok &= R >= (X + 1) / 2;
	ok &= C >= X;

	if (X == 4) {
		if (R == 2) ok = false;
	}

	if (X == 6) {
		if (R == 3) ok = false;
	}

	if (X >= 7) ok = false;

	string res = ok ? "GABRIEL" : "RICHARD"; 

	static int test;
	cout << "Case #" << ++test << ": " << res << endl;
	cerr << "Case #" << test << ": " << res << endl;
}

int main() {
	int t;
	cin >> t;
	while (t --> 0)
		solve();
	return 0;
}