#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

int solve(string s, int n) {
	int res = 0;
	for(int i = 0;i+1 < n; ++i) {
		res += (s[i] != s[i+1]);
	}
	res += s[n-1] == '-';
	return res;
}

int main() {
	int T;
	cin >> T;
	for(int t = 1;t <= T; ++t) {
		string s;
		cin >> s;
		int n(s.length());
		int res(solve(s,n));
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}