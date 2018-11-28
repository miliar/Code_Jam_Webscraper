#include <bits/stdc++.h>

using namespace std;

#define MAXN 13

string Pans[MAXN][MAXN][MAXN];
int N, R, P, S;
int P3[MAXN];

void precalc() {
	P3[0] = 1;
	for (int i = 1; i < MAXN; i++) {
		P3[i] = P3[i - 1] * 3;
	}
}

char transfCh(int bit) {
	if (bit == 0) {
		return 'R';
	} else if (bit == 1) {
		return 'P';
	} else {
		return 'S';
	}
}

string transf(int mask) {
	string ret = "";
	for (int i = 0; i < N; i++) {
		int bit = mask % 3;
		mask /= 3;
		char ch = transfCh(bit);
		ret += ch;
	}
	return ret;
}

char winner(char a, char b) {
	if (a > b) {
		swap(a, b);
	}
	if (a == 'P' && b == 'R') {
		return 'P';
	}
	if (a == 'P' && b == 'S') {
		return 'S';
	}
	if (a == 'R' && b == 'S') {
		return 'R';
	}
	assert(false);
}

bool isCountOk(string &s) {
	map<char, int> f;
	for (int i = 0; i < (int) s.size(); i++) {
		f[s[i]]++;
	}
	return f['P'] == P && f['R'] == R && f['S'] == S;
}

bool isOk(string s) {
	if (!isCountOk(s)) {
		return false;
	}
	while (s.size() > 1) {
		string next = "";
		for (int i = 0; i < (int) s.size(); i += 2) {
			char a = s[i];
			char b = s[i + 1];
			if (a == b) {
				return false;
			}
			char w = winner(a, b);
			next += w;
		}
		s = next;
	}
	return true;
}

string solve() {
	string ans = "";
	for (int mask = 0; mask < P3[N]; mask++) {
		string smask = transf(mask);
		if (isOk(smask)) {
			if (ans.size() == 0 || smask < ans) {
				ans = smask;
			}
		}
	}
	return ans;
}

int main() {
	assert(freopen("A.in", "r", stdin));
	assert(freopen("A.out", "w", stdout));
	cin.sync_with_stdio(false);

	precalc();

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		cin >> N >> R >> P >> S;
		N = 1 << N;
		string ans = solve();

		if (ans.size() == 0) {
			cout << "IMPOSSIBLE\n";
		} else {
			cout << ans << '\n';
		}
		
		cerr << t << endl;
	}

	return 0;
}
