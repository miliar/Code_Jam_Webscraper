//In the name of God
//...
#include <bits/stdc++.h>
using namespace std;

char a[5][5] = { {},
	{0, 1, 2, 3, 4},
	{0, 2, -1, 4, -3},
	{0, 3, -4, -1, 2},
	{0, 4, 3, -2, -1}
};
char sgn(char c) { return c > 0? 1: -1; }
char opr(char c, char d) {
	return sgn(c) * sgn(d) * a[(int) abs(c)][(int) abs(d)];
}
int main() {
	int test; cin >> test;
	for (int num = 1; num <= test; num++) {
		int l, x;
		cin >> l >> x;
		string s, t;
		cin >> t;
		for (int i = 0; i < x; i++)
			s += t;
		int point = 0;
		char cur = 1;
		for (int i = 0; i < s.size(); i++) {
//			cerr << cur + 0 << '\n';
			cur = opr(cur, s[i] - 'i' + 2);
			if (!point && cur == 2)
				point = 1;
			if (point == 1 && cur == opr(2, 3))
				point  = 2;
		}
		cout << "Case #" << num << ": ";
		cout << (point == 2 && cur == opr(opr(2, 3), 4)? "YES\n": "NO\n");
	}
	return 0;
}
