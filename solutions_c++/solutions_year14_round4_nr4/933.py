//In the name of God
#include <algorithm>
#include <iostream>
using namespace std;
const int N = 6, M = 10;

int t[N][M * 10][26], n, m, a[M], ed[M], rep, ans;
string s[M];

void bt(int c) {
	if (c == m) {
//		for (int i = 0; i < m; i++)
//			cerr << a[i] << ' ';
//		cerr << '\n';
		for (int i = 0; i < n; i++)
			if (!count(a, a + m, i))
				return;
		int tmp = n;
		fill(t[0][0], t[N][0], -1);
		fill(ed, ed + n, 1);
		for (int i = 0; i < m; i++) {
			int cur = 0;
			for (int j = 0; j < (int) s[i].size(); j++) {
				if (t[a[i]][cur][s[i][j]] == -1)
					t[a[i]][cur][s[i][j]] = ed[a[i]]++, tmp++;
				cur = t[a[i]][cur][s[i][j]];
			}
		}
		if (tmp > ans)
			ans = tmp, rep = 1;
		else if (tmp == ans)
			rep++;
		return;
	}
	for (int i = 0; i < n; i++) {
		a[c] = i;
		bt(c + 1);
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int test = 1; test <= T; test++) {
		cin >> m >> n;
		for (int i = 0; i < m; i++) {
			cin >> s[i];
			for (int j = 0; j < (int) s[i].size(); j++)
				s[i][j] -= 'A';
		}
		ans = 0;
		bt(0);
		cout << "Case #" << test << ": " << ans << ' ' << rep << '\n';
	}
	return 0;
}
