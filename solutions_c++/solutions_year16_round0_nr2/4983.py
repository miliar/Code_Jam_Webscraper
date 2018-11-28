#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;

int solve() {
	string s;
	cin >> s;
	char prev = '0';
	int ans = 0;
	for (int i = 0; i < (int)s.size(); i++) {
		if (s[i] != prev) {
			ans += 1;
		}
		prev = s[i];
	}
	if (s[(int)s.size()-1] == '-') {
		return ans;
	} else {
		return ans - 1;
	}
}

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cout << "Case #" << i+1 << ": " << solve() << endl;
	}
	return 0;
}