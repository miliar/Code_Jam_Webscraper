#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> p(13), r(13), s(13);

string gen(char c, int n) {
	if (n == 0) {
		return string(1, c);
	} else {
		if (c == 'P') {
			string s1 = gen('P', n - 1);
			string s2 = gen('R', n - 1);
			if (s1 < s2) return s1 + s2;
			else return s2 + s1;
		}
		if (c == 'R') {
			string s1 = gen('R', n - 1);
			string s2 = gen('S', n - 1);
			if (s1 < s2) return s1 + s2;
			else return s2 + s1;
		}
		if (c == 'S') {
			string s1 = gen('P', n - 1);
			string s2 = gen('S', n - 1);
			if (s1 < s2) return s1 + s2;
			else return s2 + s1;
		}
	}
}

bool check(int p1, int r1, int s1, string &s) {
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == 'P') p1--;
		if (s[i] == 'R') r1--;
		if (s[i] == 'S') s1--;
		if (p1 < 0 || r1 < 0 || s1 < 0) return false;
	}
	return true;
}

bool check(int n, int p1, int r1, int s1) {
	if (check(p1, r1, s1, p[n])) {
		cout << p[n] << endl;
		return true;
	}
	if (check(p1, r1, s1, r[n])) {
		cout << r[n] << endl;
		return true;
	}
	if (check(p1, r1, s1, s[n])) {
		cout << s[n] << endl;
		return true;
	}
	return false;
}

int main() {
	int kase;
	cin >> kase;
	for (int i = 0; i <= 12; i++) {
		p[i] = gen('P', i);
		r[i] = gen('R', i);
		s[i] = gen('S', i);
	}
	for (int ii = 1; ii <= kase; ii++) {
		int n, p1, r1, s1;
		cin >> n >> r1 >> p1 >> s1;
		cout << "Case #" << ii << ": ";
		if (!check(n, p1, r1, s1)) cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}