#include <bits/stdc++.h>
using namespace std;

char cmp(char a, char b) {
	if (a == 'P') {
		if (b == 'R') {
			return 'P';
		}
		else if (b == 'S') {
			return 'S';
		}
	}
	else if (a == 'R') {
		if (b == 'P') {
			return 'P';
		}
		else if (b == 'S') {
			return 'R';
		}
	}
	else if (a == 'S') {
		if (b == 'P') {
			return 'S';
		}
		else if (b == 'R') {
			return 'R';
		}
	}
	return 'X';
}

string num[13][128];

void precalc() {
	num[1]['P'] = "PR";
	num[1]['S'] = "PS";
	num[1]['R'] = "RS";

	for (int i = 2; i <= 12; i++) {
		for (char c = 'P'; c <= 'S'; c++) {
			if (c == 'Q') {
				continue;
			}
			for (char d = 'P'; d <= 'S'; d++) {
				if (d == 'Q') {
					continue;
				}
				char r = cmp(c, d);
				if (r != 'X') {
					num[i][r] = min(num[i - 1][c], num[i - 1][d]) + max(num[i - 1][c], num[i - 1][d]);
				}
			}
		}
	}
}

bool is(string str, int r, int p, int s) {
	for (int i = 0; i < str.length(); i++) {
		if (str[i] == 'R') {
			r--;
		}
		if (str[i] == 'P') {
			p--;
		}
		if (str[i] == 'S') {
			s--;
		}
	}
	return (r == 0 && p == 0 && s == 0);
}

void solve(){
	int n, r, p, s;
	cin >> n >> r >> p >> s;

	string best = "";
	for (char c = 'P'; c <= 'S'; c++) {
		if (c == 'Q') {
			continue;
		}
		if (is(num[n][c], r, p, s)) {
			if (best == "" || best > num[n][c]) {
				best = num[n][c];
			}
		}
	}

	if (best == "") {
		cout << "IMPOSSIBLE";
	}
	else {
		cout << best;
	}
}

int main(){
#ifdef HELTHAZAR
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	precalc();

	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		//printf("Case #%d: ", t);
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		// printf("\n");
	}
}
