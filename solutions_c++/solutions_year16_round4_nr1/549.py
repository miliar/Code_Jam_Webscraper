#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

string dfs(string c, int d) {
	if (d == 0) {
		return c;
	}
	string l, r;
	if (c == "P") {
		l = dfs("P", d - 1);
		r = dfs("R", d - 1);
	}
	else if (c == "R") {
		l = dfs("R", d - 1);
		r = dfs("S", d - 1);
	}
	else if (c == "S") {
		l = dfs("S", d - 1);
		r = dfs("P", d - 1);
	}
	if (l < r) {
		return l + r;
	}
	else {
		return r + l;
	}
}

bool cnt(string t, int r, int p, int s) {
	bool z1 = count(t.begin(), t.end(), 'R') == r;
	bool z2 = count(t.begin(), t.end(), 'P') == p;
	bool z3 = count(t.begin(), t.end(), 'S') == s;
	return z1 && z2 && z3;
}

int main() {
#ifdef _DEBUG
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		cout << "Case #" << t << ": ";
		
		string tp = dfs("P", n);
		string tr = dfs("R", n);
		string ts = dfs("S", n);

		if (!cnt(tp, r, p, s)) {
			tp = "^";
		}
		if (!cnt(tr, r, p, s)) {
			tr = "^";
		}
		if (!cnt(ts, r, p, s)) {
			ts = "^";
		}

		string res = min(tp, min(tr, ts));

		if (res == "^") {
			cout << "IMPOSSIBLE";
		}
		else {
			cout << res;
		}

		cout << endl;
	}
	return 0;
}