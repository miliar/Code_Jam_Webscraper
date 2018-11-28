#include <algorithm>
#include <iostream>
#include <map>
#include <utility>

using namespace std;

vector<string> s = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX",
		"SEVEN", "EIGHT", "NINE" };

long long gcd(long long x, long long y) {
	return x ? gcd(y % x, x) : y;
}

void solve() {
	vector<vector<long long> > m('Z' - 'A' + 1,
			vector<long long>(s.size() + 1));
	string S;
	cin >> S;
	for (int i = 0; i < S.length(); ++i) {
		m[S[i] - 'A'][s.size()]++;
	}
	for (int i = 0; i < s.size(); ++i) {
		for (char c : s[i]) {
			m[c - 'A'][i]++;
		}
	}
	for (int i = 0; i < s.size(); ++i) {
		for (int j = i + 1; j < m.size(); ++j) {
			if (m[j][i]) {
				m[i].swap(m[j]);
			}
		}
		for (int j = i + 1; j < m.size(); ++j) {
			long long x = m[i][i], y = m[j][i], g = gcd(x, y);
			x /= g;
			y /= g;
			g = 0;
			for (int k = i; k < m[j].size(); ++k) {
				m[j][k] = m[j][k] * x - m[i][k] * y;
				g = gcd(g, m[j][k]);
			}
			if (g) {
				for (int k = i; k < m[j].size(); ++k) {
					m[j][k] /= g;
				}
			}
		}
	}
	vector<long long> ans(10);
	for (int i = m.size() - 1; i >= 0; --i) {
		for (int j = 0; j < s.size(); ++j) {
			if (m[i][j]) {
				ans[j] = m[i].back();
				for (int k = j + 1; k < s.size(); ++k) {
					ans[j] -= ans[k] * m[i][k];
				}
				ans[j] /= m[i][j];
				break;
			}
		}
	}
	cout << " ";
	for (int i = 0; i < ans.size(); ++i) {
		for (int j = 0; j < ans[i]; j++) {
			cout << i;
		}
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ":";
		solve();
		cout << endl;
	}
}
