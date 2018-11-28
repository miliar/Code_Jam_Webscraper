#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

pair<string, int> f(string T) {
	string cur = "";
	int sign = 1;

	for (int i = 0; i < T.length(); ++i) {
		if (T[i] == 'i') {
			if (cur == "") cur = 'i';
			else if (cur == "i") { cur = ""; sign *= -1; }
			else if (cur == "j") { cur = "k"; sign *= -1; }
			else { cur = "j"; };
		}

		if (T[i] == 'j') {
			if (cur == "") cur = 'j';
			else if (cur == "i") { cur = "k"; sign *= +1; }
			else if (cur == "j") { cur = ""; sign *= -1; }
			else { cur = "i"; sign *= -1; };
		}

		if (T[i] == 'k') {
			if (cur == "") cur = 'k';
			else if (cur == "i") { cur = "j"; sign *= -1; }
			else if (cur == "j") { cur = "i"; sign *= +1; }
			else { cur = ""; sign *= -1; };
		}
	}

	return make_pair(cur, sign);
}

void solve() {
	long long L, X; cin >> L >> X;
	string s; cin >> s;
	string T; for (int i = 0; i < X && i < 100; ++i) T += s;
	T += "X";

	string need = "ijkX";
	string cur = "";
	int sign = 1;

	for (int i = 0; i < T.length(); ++i) {
		if (sign == 1 && cur == need.substr(0, 1)) {
			need = need.substr(1);
			cur = "";
		}

		if (T[i] == 'i') {
			if (cur == "") cur = 'i';
			else if (cur == "i") { cur = ""; sign *= -1; }
			else if (cur == "j") { cur = "k"; sign *= -1; }
			else { cur = "j"; };
		}

		if (T[i] == 'j') {
			if (cur == "") cur = 'j';
			else if (cur == "i") { cur = "k"; sign *= +1; }
			else if (cur == "j") { cur = ""; sign *= -1; }
			else { cur = "i"; sign *= -1; };
		}

		if (T[i] == 'k') {
			if (cur == "") cur = 'k';
			else if (cur == "i") { cur = "j"; sign *= -1; }
			else if (cur == "j") { cur = "i"; sign *= +1; }
			else { cur = ""; sign *= -1; };
		}
	}

	pair<string, int> r = f(s);

	bool ok = true;
	if (r.first == "") {
		if (r.second == 1) ok = false;
		if (X % 2 == 0) ok = false;
	} else {
		if (X % 4 != 2) ok = false;
	}

	string res = ok && need == "X" ? "YES" : "NO"; 

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