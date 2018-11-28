#include <iostream>

using namespace std;

bool okay(char * str, int n) {
	if (n == 1) return true;
	char nextStr[n/2];
	for (int i = 0; i < n; i += 2) {
		char a = str[i];
		char b = str[i+1];
		if (a == b) return false;

		char next = a;
		if (a == 'P') {
			if (b == 'R') next = 'P';
			else next = 'S';
		} else if (a == 'R') { 
			if (b == 'P') next = 'P';
			else next = 'R';
		} else {
			if (b == 'P') next = 'S';
			else next = 'R';
		}
		nextStr[i/2] = next;
	}
	return okay(nextStr, n/2);
}

string rec(int p, int r, int s, char * curr, int i, int n) {
	if (i == n) {
		if (okay(curr, n)) return string(curr);
		return "";
	}

	string res;
	if (p > 0) {
		curr[i] = 'P';
		res = rec(p-1, r, s, curr, i+1, n);
		if (res != "") return res;
	}

	if (r > 0) {
		curr[i] = 'R';
		res = rec(p, r-1, s, curr, i+1, n);
		if (res != "") return res;
	}

	if (s > 0) {
		curr[i] = 'S';
		res = rec(p, r, s-1, curr, i+1, n);
		if (res != "") return res;
	}

	return "";
}

int main() {
	int nc; cin >> nc;
	for (int cs = 1; cs <= nc; cs++) {
		int n, r, p, s; cin >> n >> r >> p >> s;
		int nn = r+p+s;
		char buf[nn+1];
		buf[nn] = '\0';
		string res = rec(p, r, s, buf, 0, nn);
		cout << "Case #" << cs << ": ";
		if (res == "") {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << res << endl;
		}
	}
}
