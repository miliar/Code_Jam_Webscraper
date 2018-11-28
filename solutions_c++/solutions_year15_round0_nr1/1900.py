
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <utility>
#include <string>
using namespace std;

int solve(int n, const string& s) {
	int ret = 0;
	int amt = s[0] - '0';
	for (int i = 1; i < n; ++i) {
		if (s[i] == '0') continue;
		if (amt < i) {
			ret += i - amt;
			amt = i;			
		}
		amt += s[i] - '0';
	}
	return ret;
}

int main () {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int t;
	cin >> t;
	int n;
	string s;
	int ans;
	for (int test = 1; test <= t; ++test) {
		cin >> n >> ws >> s;
		ans = solve(n + 1, s);
		cout << "Case #" << test << ": ";
		cout << ans;
		cout << "\n";
	}

	return 0;
}