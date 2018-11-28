/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

string c = "PRS", INF = "a";

string check( string &s, vector <int> &cnt ) {
	vector<int> a(3);
	for (char x : s)
		forn(j, 3)
			if (c[j] == x)
				a[j]++;
	return cnt == a ? s : INF;
}

void solve() {
	int n;
	vector<int> cnt(3);
	cin >> n >> cnt[1] >> cnt[0] >> cnt[2];
	string f[n + 1][3];
	forn(i, 3) f[0][i] = c[i];
	forn(i, n) forn(j, 3) {
		int j1 = (j + 1) % 3;
		f[i + 1][j] = min(f[i][j] + f[i][j1], f[i][j1] + f[i][j]);
	}
	string res = INF;
	forn(i, 3) res = min(res, check(f[n][i], cnt));
	cout << (res == INF ? "IMPOSSIBLE" : res) << "\n";
}

int main() {
  int n;
  scanf("%d ", &n);
  for (int i = 1; i <= n; i++) {
    printf("Case #%d: ", i);
    solve();
  }
}
