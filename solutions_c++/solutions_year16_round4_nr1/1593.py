#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n, r, p, s, total;
string ss;
string ans;
bool cond;

bool check() {
	string k = ss;
	string x;
	int pa = total;
	while (k.size() > 1) {
		//cout << k << endl;
		for (int i = 0; i < pa; i+=2) {
			if (k[i] == k[i+1]) return false;
			if (k[i] == 'S' && k[i+1] == 'P') x += 'S';
			if (k[i] == 'S' && k[i+1] == 'R') x+= 'R';
			if (k[i] == 'R' && k[i+1] == 'S') x+= 'R';
			if (k[i] == 'R' && k[i+1] == 'P') x+= 'P';
			if (k[i] == 'P' && k[i+1] == 'S') x+= 'S';
			if (k[i] == 'P' && k[i+1] == 'R') x+= 'P';
		}
		pa /= 2;
		k = x;
		x = "";
	}
	return true;
}
				

void solve(int pass) {
	if (pass == total) {
		if (check()) {
			cond = true;
			if (ss < ans) {
				ans = ss;
			}
		}
	} else {
		for (int i = pass; i < total; i++) {
			swap(ss[pass], ss[i]);
			solve(pass + 1);
			swap(ss[pass], ss[i]);
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++) {
		ss = "";
		ans = "";
		cond = false;
		cout << "Case #" << z << ": ";
		cin >> n >> r >> p >> s;
		total = r + s + p;
		for (int i = 0; i < r; i++) ss += 'R';
		for (int i = 0; i < p; i++) ss += 'P';
		for (int i = 0; i < s; i++) ss += 'S';
		for (int i = 0; i < total; i++) ans += 'Z';
		solve(0);
		if (cond) {
			cout << ans << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
