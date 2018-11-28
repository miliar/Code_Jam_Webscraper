#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n, r, p, s;
	cin >> n >> r >> p >> s;
	vector<vector<string>> best(4, vector<string>(n + 1));
	for(char letter : {'R', 'P', 'S'}) {
		best[letter - 'P'][0] = letter;
	}
	for(int i = 1; i <= n; ++i) {
		for(char letter : {'R', 'P', 'S'}) {
			char lose;
			if(letter == 'R') {
				lose = 'S';
			} else if(letter == 'P') {
				lose = 'R';
			} else {
				lose = 'P';
			}
			if(best[letter - 'P'][i - 1] < best[lose - 'P'][i - 1]) {
				best[letter - 'P'][i] = best[letter - 'P'][i - 1] + best[lose - 'P'][i - 1];
			} else {
				best[letter - 'P'][i] = best[lose - 'P'][i - 1] + best[letter - 'P'][i - 1];
			}
		}
	}
	vector<string> options = {best[0][n], best[2][n], best[3][n]};
	sort(options.begin(), options.end());
	for(string &option : options) {
		int count[4] = {0, 0, 0, 0};
		for(char letter : option) {
			++count[letter - 'P'];
		}
		if(count[0] == p && count[2] == r && count[3] == s) {
			cout << ' ' << option << '\n';
			return;
		}
	}
	cout << " IMPOSSIBLE\n";
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ':';
		solve();
	}
	return 0;
}
