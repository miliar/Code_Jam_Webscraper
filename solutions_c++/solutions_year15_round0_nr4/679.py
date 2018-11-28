#include <bits/stdc++.h> 
using namespace std;
int main() {
		freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);
	int t;
	cin >> t ;
	for (int tst = 1; tst <= t; ++tst) {
		int x, r, c;
		cin >> x >> r >> c;
		bool b = x >= 7 or (r * c) % x or min(r, c) < x - 1;
		cout << "Case #" << tst << ": " << (b ? "RICHARD\n" : "GABRIEL\n");
	}
}
