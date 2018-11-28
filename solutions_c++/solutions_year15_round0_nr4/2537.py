#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	freopen("input2.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);
	int i, j, n, t, ans, p = 1, x, r, c, h1, h2, h3;
	string s;
	cin >> t;
	while (t--) {
		cin >> x >> r >> c;
		//cout << x << " " << r << " " << c << endl;
		if (r > c)
			swap(r, c);
		if (((r*c) % x) != 0) {
			cout << "Case #" << p << ": " << "RICHARD" << endl;
			p++;
			continue;
		}
		if ((x == 3 && r == 1 && c == 3) || (x == 4 && r == 1 && c == 4) || (x == 4 && r == 2 && c == 4) || (x == 4 && r == 2 && c == 2)) {
			cout << "Case #" << p << ": " << "RICHARD" << endl;
			p++;
			continue;
		}
		cout << "Case #" << p << ": " << "GABRIEL" << endl;
		p++;
	}
	return 0;
}