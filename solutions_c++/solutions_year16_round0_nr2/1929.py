#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>

using namespace std;

int solve(string &s) {
	int n_flip = 0;
	for (int i = 1; i < s.size(); i++) {
		if (s[i] != s[i - 1]) {
			n_flip++;
		}
	}

	if (s.back() == '-') {
		n_flip++;
	}

	return n_flip;
}

int main() {
	int t;
	string s;

	cin >> t;
	vector<int> ans(t, 0);

	for (int i = 0; i < t; i++) {
		cin >> s;
		ans[i] = solve(s);
	}

	for (int i = 0; i < t; i++) {
		printf("Case #%d: %d\n", i + 1, ans[i]);
	}
	return 0;
}
