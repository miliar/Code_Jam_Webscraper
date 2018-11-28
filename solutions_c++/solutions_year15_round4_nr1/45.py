#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

#define foreach(e,x) for(__typeof((x).begin()) e=(x).begin(); e!=(x).end(); ++e)

const int N = 100 + 10;

const int tx[] = {-1, 0, 1, 0};
const int ty[] = {0, 1, 0, -1};

int n, m;
char a[N][N];

void getIt(int &x, int &y, char c)
{
	if (c == '^') {
		x = -1; y = 0;
	}
	if (c == 'v') {
		x = 1; y = 0;
	}
	if (c == '<') {
		x = 0; y = -1;
	}
	if (c == '>') {
		x = 0; y = 1;
	}
}

int valid(int x, int y)
{
	return x >= 0 && x < n && y >= 0 && y < m;
}

bool danger(int sx, int sy, int dx, int dy)
{
	for(sx += dx, sy += dy; valid(sx, sy); sx += dx, sy += dy) {
		if (a[sx][sy] != '.') return false;
	}
	return true;
}

void solve()
{
	cin >> n >> m;
	for(int i = 0; i < n; ++ i) {
		scanf("%s", a[i]);
	}

	int cnt = 0;
	for(int i = 0; i < n; ++ i) {
		for(int j = 0; j < m; ++ j) {
			if (a[i][j] != '.') {
				int dx, dy;
				getIt(dx, dy, a[i][j]);
				if (danger(i, j, dx, dy)) {
					cnt ++;
					int flag = false;
					for(int d = 0; d < 4; ++ d) {
						if (! danger(i, j, tx[d], ty[d])) {
							flag = true;
						}
					}
					if (! flag) {
						puts("IMPOSSIBLE");
						return;
					}
				}
			}
		}
	}

	cout << cnt << endl;
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	int test_case;
	cin >> test_case;
	for(int i = 0; i < test_case; ++ i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
