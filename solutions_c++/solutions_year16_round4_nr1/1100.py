#include <bits/stdc++.h>

using namespace std;

#define all(x) (x).begin(), (x).end()
#define allr(x) (x).rbegin(), (x).rend()

typedef pair<int, int> PII;
typedef pair<int, char> PIC;
typedef long long LL;

string getLineUp(string s, int rounds) {
	while (rounds--) {
		string t = "";
		for (auto c : s) {
			if (c == 'P') t += "PR";
			else if (c == 'R') t += "RS";
			else t += "PS";
		}
		s = t;
	}
	return s;
}

bool check(const string &s, int R, int P, int S) {
	int _R = count(all(s), 'R');
	int _P = count(all(s), 'P');
	int _S = count(all(s), 'S');
	return (P == _P && R == _R && S == _S);
}

string minify(string s, int N) {
	string t = "";
	for (int i = 0; i < N; ++i) {
		int len = (1 << i);
		t = "";
		for (int j = 0; j + len < s.size(); j += 2 * len) {
			string x = s.substr(j, len);
			string y = s.substr(j + len, len);
			if (x > y) swap(x, y);
			t += x; t += y;
		}
		s = t;
	}
	return s;
}

int main() {
	int T, N, R, P, S;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		scanf("%d %d %d %d", &N, &R, &P, &S);
		set<string> valid;
		string cur = getLineUp("R", N);
		if (check(cur, R, P, S)) valid.insert(minify(cur, N));
		cur = getLineUp("P", N);
		if (check(cur, R, P, S)) valid.insert(minify(cur, N));
		cur = getLineUp("S", N);
		if (check(cur, R, P, S)) valid.insert(minify(cur, N));
		if (valid.size() > 0) {
			cout << *valid.begin() << "\n";
		} else {
			cout << "IMPOSSIBLE\n";
		}
	}
	return 0;
}