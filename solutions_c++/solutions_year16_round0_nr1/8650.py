#include <bits/stdc++.h>
using namespace std;

int t, n;

string solve(int N) {
	if (N == 0) {
		return "INSOMNIA";
	}
	set<char> ss;
	for (long long i = 1; ; ++i) {
		long long f = (long long) N * i;
		stringstream SS;
		SS << f;
		string s = SS.str();
		for (int j = 0; j < s.length(); ++j) {
			ss.insert(s[j]);
		}
		if (ss.size() == 10) {
			return s;
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	freopen("out.txt", "w", stdout);
	cin >> t;
	for (int tc = 1; tc <= t; ++tc) {
		int e;
		cin >> e;
		printf("Case #%d: %s\n", tc, solve(e).c_str());
	}
	return 0;
}
