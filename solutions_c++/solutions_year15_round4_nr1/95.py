#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <cassert>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const int MAXN = 110;

int r, c;
char a[MAXN][MAXN];

bool good[4][MAXN][MAXN];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	map<char, int> to;
	to['<'] = 0;
	to['>'] = 1;
	to['^'] = 2;
	to['v'] = 3;

	int T;
	scanf("%d ", &T);
	forn(testNum, T) {
		printf("Case #%d: ", testNum + 1);

		scanf("%d%d", &r, &c);
		forn(i, r)
			forn(j, c)
				scanf(" %c ", &a[i][j]);

		forn(i, r)
			forn(j, c)
				forn(q, 4)
					good[q][i][j] = true;

		forn(i, r) {
			forn(j, c)
				if (a[i][j] != '.') {
					good[0][i][j] = false;
					break;
				}
			forba(j, c, 0)
				if (a[i][j] != '.') {
					good[1][i][j] = false;
					break;
				}
		}

		forn(j, c) {
			forn(i, r)
				if (a[i][j] != '.') {
					good[2][i][j] = false;
					break;
				}
			forba(i, r, 0)
				if (a[i][j] != '.') {
					good[3][i][j] = false;
					break;
				}
		}

		int ans = 0;

		forn(i, r) {
			if (ans == -1)
				break;
			forn(j, c)
				if (a[i][j] != '.') {
					if (good[to[a[i][j]]][i][j])
						continue;
					bool _any = false;
					forn(q, 4)
						if (good[q][i][j]) {
							_any = true;
							break;
						}
					if (_any) {
						ans++;
					} else {
						ans = -1;
						break;
					}
				}
		}

		if (ans == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);

	}
	return 0;
}
