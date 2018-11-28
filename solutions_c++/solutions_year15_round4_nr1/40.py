#include <iostream>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;

#define REP(i, n) for(int i(0); (i)<(int)(n); i++)
#define FOR(i, a, b) for (int i(a); i <= int(b); i++)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair

const int N = 105;
int n, m, f[4][N][N];
char s[N][N];

void solve() {
	static int caseCnt = 0;
	printf("Case #%d: ", ++caseCnt);

	cin >> n >> m;
	REP(i, n) scanf("%s", s[i]);
	memset(f, 0, sizeof(f));
	REP(i, n) REP(j, m) {
		if (i && s[i - 1][j] == '.') f[0][i][j] = f[0][i - 1][j] + 1;
		if (j && s[i][j - 1] == '.') f[1][i][j] = f[1][i][j - 1] + 1;
	}
	for (int i = n - 1; i >= 0; i--)
	for (int j = m - 1; j >= 0; j--) {
		if (i < n - 1 && s[i + 1][j] == '.') f[2][i][j] = f[2][i + 1][j] + 1;
		if (j < m - 1 && s[i][j + 1] == '.') f[3][i][j] = f[3][i][j + 1] + 1;
	}
	int ans = 0;
	REP(i, n) REP(j, m) if (s[i][j] != '.') {
		int cnt = 0;
		if (f[0][i][j] == i) cnt++;
		if (f[1][i][j] == j) cnt++;
		if (f[2][i][j] == n - 1 - i) cnt++;
		if (f[3][i][j] == m - 1 - j) cnt++;
		if (cnt == 4) {
			puts("IMPOSSIBLE");
			return ;
		}
		if (s[i][j] == '^' && f[0][i][j] == i) cnt += 9;
		if (s[i][j] == '<' && f[1][i][j] == j) cnt += 9;
		if (s[i][j] == 'v' && f[2][i][j] == n - 1 - i) cnt += 9;
		if (s[i][j] == '>' && f[3][i][j] == m - 1 - j) cnt += 9;
		if (cnt >= 9) ans++;
	}
	cout << ans << endl;
}

int main() {
	int T = 1;
	scanf("%d", &T);
	while (T--) solve();
	return 0;
}

