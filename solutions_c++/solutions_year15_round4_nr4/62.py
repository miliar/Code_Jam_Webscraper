#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const int MAXN = 10;

const int dx[] = { 1, 0,-1, 0};
const int dy[] = { 0, 1, 0,-1};

int r, c;

bool inside(int x, int y) {
	return x >= 0 && x < r;
}

vector<int> b[MAXN][MAXN];

int a[MAXN][MAXN];
int cnt[MAXN][MAXN];
int fr[MAXN][MAXN];

int ans;

void gen(int x, int y) {
	if (x == r) {

		forn(k, ans)
			forn(z, c) {
				bool good = true;

				forn(i, r)
					forn(j, c)
						if (a[i][(j + z) % c] != b[i][j][k]) {
							good = false;
							break;
						}

				if (good)
					return;
			}

		forn(i, r)
			forn(j, c)
				b[i][j].push_back(a[i][j]);
		ans++;
		return;
	}

	forab(i, 1, 4) {
		a[x][y] = i;

		bool good = true;

		forn(q, 4) {
			int nx = x + dx[q], ny = (y + dy[q] + c) % c;
			if (!inside(nx, ny))
				continue;
			if (a[nx][ny] == a[x][y]) {
				cnt[x][y]++;
				cnt[nx][ny]++;
			}

			fr[nx][ny]--;
			if (cnt[nx][ny] > a[nx][ny] || fr[nx][ny] < a[nx][ny] - cnt[nx][ny])
				good = false;
		}

		if (cnt[x][y] > a[x][y] || fr[x][y] < a[x][y] - cnt[x][y])
			good = false;

		if (good) {
			if (y < c - 1)
				gen(x, y + 1);
			else
				gen(x + 1, 0);
		}

		forn(q, 4) {
			int nx = x + dx[q], ny = (y + dy[q] + c) % c;
			if (!inside(nx, ny))
				continue;
			if (a[nx][ny] == a[x][y]) {
				cnt[x][y]--;
				cnt[nx][ny]--;
			}

			fr[nx][ny]++;
		}
	}

	a[x][y] = 0;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d ", &T);
	forn(test, T) {
		printf("Case #%d: ", test + 1);

		scanf("%d%d", &r, &c);

		forn(i, r)
			forn(j, c) {
				a[i][j] = 0;
				cnt[i][j] = 0;
				fr[i][j] = ((i == 0 || i == r - 1) ? 3 : 4);
			}

		forn(i, r)
			forn(j, c)
				b[i][j].clear();
		ans = 0;
		gen(0, 0);

		printf("%d\n", ans);

	}
	return 0;
}
