#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <bits/stdc++.h>

using namespace std;

bool cmp(string less, string more) {
	for (int i = 0; i < (int)less.size(); ++i) {
		if (less[i] < more[i]) {
			return true;
		}
	}
	return false;
}

string check(char winner, int depth) {
	if (depth == 0) {
		return string(1, winner);
	}
	string l, r;
	switch (winner) {
		case 'P':
			l = check('P', depth - 1);
			r = check('R', depth - 1);
			break;

		case 'R':
			l = check('R', depth - 1);
			r = check('S', depth - 1);
			break;

		case 'S':
			l = check('P', depth - 1);
			r = check('S', depth - 1);
			break;
	}
	if (!(cmp(l, r))) {
		swap(l, r);
	}
	return l + r;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	vector<string> v;
	int n, p, r, s;
	for (int i = 0; i < t; ++i) {
		cin >> n >> r >> p >> s;
		v.clear();
		v.push_back(check('P', n));
		v.push_back(check('R', n));
		v.push_back(check('S', n));
		int _p, _r, _s;
		for (auto &ss : v) {
			_p = 0;
			_r = 0;
			_s = 0;
			for (auto c : ss) {
				switch (c) {
				case 'P':
					_p++;
					break;

				case 'R':
					_r++;
					break;

				case 'S':
					_s++;
					break;
				}
			}
			if (p != _p || r != _r || s != _s) {
				ss = "ZZZ";
			}
		}
		sort(v.begin(), v.end());
		cout << "Case #" << (i + 1) << ": " << (v[0] == "ZZZ" ? "IMPOSSIBLE" : v[0]) << "\n";
	}
	return 0;
}
