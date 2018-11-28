#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define pb emplace_back

using namespace std;

typedef long long ll;

void fuck(map<char, int> &m, char c, const string &s) {
	int x = m[c];
	for (int i = 0; i < x; ++i) {
		for (char q : s) {
			m[q]--;
		}
	}
}

void solve() {
	string s;
	cin >> s;
	map<char, int> cnt;
	for (auto c : s) {
		cnt[c]++;
	}
	int ans[10];
	memset(ans, 0, sizeof(ans));
	ans[0] = cnt['Z'];
	fuck(cnt, 'Z', "ZERO");
	ans[2] = cnt['W'];
	fuck(cnt, 'W', "TWO");
	ans[4] = cnt['U'];
	fuck(cnt, 'U', "FOUR");
	ans[6] = cnt['X'];
	fuck(cnt, 'X', "SIX");
	ans[8] = cnt['G'];
	fuck(cnt, 'G', "EIGHT");
	ans[1] = cnt['O'];
	fuck(cnt, 'O', "ONE");
	ans[3] = cnt['H'];
	fuck(cnt, 'H', "THREE");
	ans[5] = cnt['F'];
	fuck(cnt, 'F', "FIVE");
	ans[7] = cnt['S'];
	fuck(cnt, 'S', "SEVEN");
	ans[9] = cnt['I'];
	fuck(cnt, 'I', "NINE");
	for (auto p : cnt) {
		assert(p.second == 0);
	}
	for (int i = 0; i < 10; ++i) {
		for (int j = 0; j < ans[i]; ++j) {
			cout << i;
		}
	}
	cout << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
  return 0;
}
