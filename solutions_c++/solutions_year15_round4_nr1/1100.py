#pragma comment(linker, "/STACK:102400000,102400000")
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cassert>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#define  RD(x)      scanf("%d", &x)
#define  REP(i, n)  for (int i=0; i<int(n); ++i)
#define  FOR(i, n)  for (int i=1; i<=int(n); ++i)
#define  pii        pair<int, int>
#define  piL        pair<int, long long>
#define  mp         make_pair
#define  pb         push_back
#define  whatis(x)  cout << #x << ": " << x << endl;
int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};

using namespace std;
#define  N   123
#define  eps 1e-8
#define  pi  acos(-1.0)
#define  inf 0XFFFFFFFll
#define  mod 1000000007ll
#define  LL  long long
#define  ULL unsigned long long

int m, n;

char s[N][N];

bool cao[N][N];

int Main() {

//	freopen("bc.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
//	freopen("out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);

	int T = 0;
	cin >> T;

	FOR(_T, T) {

		cin >> m >> n;

		FOR(i, m)
			cin >> s[i] + 1;

		bool impossible = false;

		FOR(i, m) FOR(j, n) if (s[i][j] != '.') {
			int cnt = 0;
			FOR(k, m) if (s[k][j] == '.')
				cnt++;
			FOR(k, n) if (s[i][k] == '.')
				cnt++;
			if (cnt == n + m - 2) {
				impossible = true;
				break;
			}
		}

		printf("Case #%d: ", _T);
		if (impossible) {
			puts("IMPOSSIBLE");
			continue;
		}

		int ans = 0;
		memset(cao, false, sizeof cao);

		FOR(j, n) {
			if (s[1][j] == '^')
				cao[1][j] = true;
			if (s[m][j] == 'v')
				cao[m][j] = true;
		}

		FOR(i, m) {
			if (s[i][1] == '<')
				cao[i][1] = true;
			if (s[i][n] == '>')
				cao[i][n] = true;
		}

		FOR(i, m) FOR(j, n) if (s[i][j] != '.') {
			int d;
			if (s[i][j] == '^')
				d = 2;
			else if (s[i][j] == 'v')
				d = 0;
			else if (s[i][j] == '<')
				d = 3;
			else if (s[i][j] == '>')
				d = 1;
			int x = i, y = j;
			int cnt = 0;
			while (x > 0 && x <= m && y > 0 && y <= n) {
				if (s[x][y] != '.')
					cnt++;
				x += dx[d];
				y += dy[d];
			}
			if (cnt == 1)
				cao[i][j] = true;
		}

		FOR(i, m) FOR(j, n) if (cao[i][j])
			ans++;

		printf("%d\n", ans);



	}


	return 0;
}

int main() {
	return Main();
}
