#include <bits/stdc++.h>

#define ll long long
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define ld double

using namespace std;

const int nm = 1026;

string s;
int n;
int f[nm], g[nm];

void solve(int test) {
	cout << "Case #" << test << ": ";
	cin >> s;
	n = s.length();
	for (int i = 1; i <= n; ++i) {
		if (s[i - 1] == '+') {
			f[i] = f[i - 1];
			g[i] = f[i - 1] + 1;
		} else {
			f[i] = g[i - 1] + 1;
			g[i] = g[i - 1];
		}
//		cout << f[i] << " " << g[i] << "\n";
	}
	cout << f[n] << "\n";
}

int main() {
#ifdef LOCAL
//	freopen("input.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("output2.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		solve(i);
}
