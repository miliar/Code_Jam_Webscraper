#include <bits/stdc++.h>
using namespace std;

#define pb push_back

typedef long long ll;

int n, J;
map<string, vector<int>> ans;
mt19937 rnd;

vector<int> jamcoin(string s) {
	reverse(s.begin(), s.end());
	vector<int> res;
	for (int d = 2; d <= 10; ++d) {
		__int128 pw = 1;
		__int128 val = 0;
		for (int i = 0; i < (int)s.size(); ++i) {
			if (s[i] == '1') {
				val += pw;
			}
			pw *= d;
		}
		bool found = false;
		for (int i = 0; i < 100000; ++i) {
			int x = rnd() % 1000000 + 2;
			if (val % x == 0 && x < val) {
				found = true;
				res.pb(x);
				break;
			}
		}
		if (!found) return vector<int>();
	}
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	rnd = mt19937(0xdeadbeef);
	int T;
	cin >> T;
	assert(T == 1);
	cin >> n >> J;
	while ((int)ans.size() < J) {
		string s(n, '0');
		s[0] = s[n - 1] = '1';
		for (int i = 1; i < n - 1; ++i) {
			s[i] = rnd() % 2 + '0';
		}
		vector<int> tmp = jamcoin(s);
		if ((int)tmp.size() == 9) {
			ans[s] = tmp;
			clog << ans.size() << endl;
		}
	}
	cout << "Case #1:\n";
	for (auto a : ans) {
		cout << a.first;
		for (auto b : a.second) {
			cout << ' ' << b;
		}
		cout << endl;
	}
	return 0;
}