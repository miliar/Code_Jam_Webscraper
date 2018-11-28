#include <bits/stdc++.h>
using namespace std;

char ch[1000000];
map<string, bool> M[2], ans;

void insert(string r, int idx) {
	stringstream ss;
	ss << r;
	while (ss >> r) {
		M[idx][r] = true;
	}
}

void solve(string r) {
	stringstream ss;
	ss << r;
	while (ss >> r) {
		if (M[0].count(r) != 0 && M[1].count(r) != 0) {
			ans[r] = true;
		}
	}
}

int main() {
	int test, n;
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	cin >> test;
	for (int t = 1; t <= test; t++) {
		M[0].clear();
		M[1].clear();
		ans.clear();
		cout << "Case #" << t << ": ";
		string a = "", b = "", s = "";
		cin >> n;
		while(a.size() == 0)
			getline(cin, a);
		while(b.size() == 0)
			getline(cin, b);
		cout << a << "\n" << b << "\n";
		insert(a, 0);
		insert(b, 1);
		solve(b);
		for (int i = 0; i < (n - 2); ++i) {
			s = "";
			while(s.size() == 0)
				getline(cin, s);
			cout << s << '\n';
			solve(s);
		}
		cout << ans.size() << "\n";
	}
	return 0;
}