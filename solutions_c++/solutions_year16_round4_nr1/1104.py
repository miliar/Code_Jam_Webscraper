//============================================================================
// Name        : A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <map>
#include <cstdio>
#include <queue>
#include <set>
#include <vector>
typedef long long LL;
using namespace std;
#define MAXN 1010

int n, p, r, s;

string dfs(int n, int win) {
	if (n == 0) {
		if (win == 0) {
			return "0";
		} else if (win == 1) {
			return "1";
		}
		return "2";
	} else {
		string a, b;
		int x = win;
		int y = (win + 1) % 3;
		a = dfs(n - 1, x);
		b = dfs(n - 1, y);
		if (a > b) {
			return b + a;
		}
		return a + b;
	}
}

bool ok(string str) {
	int a, b, c;
	a = b = c = 0;
	for (int i = 0; i < str.length(); ++i) {
		if (str[i] == '0') {
			a++;
		} else if (str[i] == '1') {
			b++;
		} else {
			c++;
		}
	}
	return a == p && b == r && c == s;
}

int winner(int x, int y) {
	if (x > y) {
		int t = x;
		x = y;
		y = t;
	}
	if (x == 0 && y == 2) {
		return y;
	}
	return x;
}

void gao() {

	vector<int> arr;
	for (int i = 0; i < p; i++) {
		arr.push_back(0);
	}
	for (int i = 0; i < r; i++) {
		arr.push_back(1);
	}
	for (int i = 0; i < s; i++) {
		arr.push_back(2);
	}
	string ans = "ZZZ";
	do {
		vector<int> tmp = arr;
		bool f = true;
		while (tmp.size() != 1) {
			for (int i = 0; i < tmp.size(); i += 2) {
				if (tmp[i] == tmp[i + 1]) {
					f = false;
					break;
				}

			}
			vector<int> x;
			for (int i = 0; i < tmp.size(); i += 2) {
				x.push_back(winner(tmp[i], tmp[i + 1]));
			}
			tmp = x;
		}
		if (f) {
			string tt = "";
			for (int i = 0; i < arr.size(); i++) {
				if (arr[i] == 0) {
					tt += "P";
				} else if (arr[i] == 1) {
					tt += "R";
				} else {
					tt += "S";
				}
			}
			if (tt < ans) {
				ans = tt;
			}
		}
	} while (next_permutation(arr.begin(), arr.end()));
	cout << ans << endl;
	;
}

int main() {
	int T;
	string path = "/Users/baidu/Downloads/";

//change file name
	string in = "A-small-attempt1.in";
	string out = "0.txt";

	freopen((path + in).c_str(), "r", stdin);
	freopen((path + out).c_str(), "w", stdout);
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cin >> n >> r >> p >> s;
//		gao();
		string res = "";
		for (int i = 0; i < 3; i++) {
			string tmp = dfs(n, i);
			if (!ok(tmp)) {
				continue;
			}
//			cout << tmp << endl;
			if (res == "") {
				res = tmp;
			} else if (tmp < res) {
				res = tmp;
			}
		}

		if (res == "") {
			res = "IMPOSSIBLE";
		} else {
			string tmp = res;
			for (int i = 0; i < tmp.length(); ++i) {
				if (tmp[i] == '0') {
					res[i] = 'P';
				} else if (tmp[i] == '1') {
					res[i] = 'R';
				} else {
					res[i] = 'S';
				}
			}
		}

		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}
