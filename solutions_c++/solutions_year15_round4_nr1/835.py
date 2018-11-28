#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <deque>
using namespace std;
//-----------------------------------------------------------
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ull inf64 = ((ull) 1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

#define bit(i) ((ull)1 << i)
//-----------------------------------------------------------

#define MAXN 150

int R, C;
int dir[][5] = {{0, 0}, {1, 0}, {0, -1}, {-1, 0}, {0, 1}};


int m[MAXN][MAXN];

int ans;

bool islegal(int x, int y)
{
	if (x < 0 || y < 0 || x >= R || y >= C) {
		return false;
	}
	return true;
}

bool searchDir(int x, int y, int d) {
	//printf("%d %d = %d\n", x, y, d);
	for(int i = 1; i <= 4; i++) {
		int nx = x;
		int ny = y;
		if (i == d) continue;
		do {
			nx += dir[i][0];
			ny += dir[i][1];
			//printf("%d %d\n", nx, ny);
			if (islegal(nx, ny) == false) break;
			if (m[nx][ny] != 0) {
				m[x][y] = i;
				return true;
			}
		} while(true);
	}
	return false;
}

void solve() {
	int ans = 0;
	bool isIm = false;
// {{0, 0}, {1, 0}, {0, -1}, {-1, 0}, {0, 1}};
	for(int i = 0; i < R && !isIm; i++) {

		for(int j = 0; j < C && !isIm; j++) {
			if (m[i][j] == 0) continue;
			if (m[i][j] == 2) {
				if (searchDir(i, j, 2)) {
					ans++;
					//printf("d=2\n");
					break;
				}
				else {
					isIm = true;
					break;
				}
			}
			else {
				break;
			}
		}
		for(int j = C - 1; j >= 0; j--) {
			if (m[i][j] == 0) continue;
			if (m[i][j] == 4) {
				if (searchDir(i, j, 4)) {
					ans++;
					//printf("[%d][%d] = d=4\n", i, j);
					break;
				}
				else {
					isIm = true;
					break;
				}
			}
			else {
				break;
			}
		}
	}

	for (int j = 0; j < C && !isIm; j++) {
		for(int i = 0; i < R && !isIm; i++) {
			if (m[i][j] == 0) continue;
			if (m[i][j] == 3) {
				if (searchDir(i, j, 3)) {
					//printf("d=2\n");
					ans++;
					break;
				}
				else {
					isIm = true;
					break;
				}
			}
			else {
				break;
			}
		}

		for(int i = R - 1; i >= 0 && !isIm; i--) {
			if (m[i][j] == 0) continue;
			if (m[i][j] == 1) {
				if (searchDir(i, j, 1)) {
					//printf("d=4\n");
					ans++;
					break;
				}
				else {
					isIm = true;
					break;
				}
			}
			else {
				break;
			}
		}
	}

	if (isIm) {
		printf("IMPOSSIBLE\n");
	}
	else {
		printf("%d\n", ans);
	}
	fflush(stdout);
}

int main() {
	int cases;
	int caseid = 1;

	char tmp[MAXN];

	freopen("input", "r", stdin);
//freopen("output", "w", stdout);
	scanf("%d", &cases);
	while (cases--) {
		ans = INT_MAX;
		printf("Case #%d: ", caseid++);
		scanf("%d%d", &R, &C);
		for(int i = 0; i < R; i++) {
			scanf("%s", tmp);
			for(int j = 0; j < C; j++) {
				if (tmp[j] == '.')
					m[i][j] = 0;
				else if (tmp[j] == 'v')
					m[i][j] = 1;
				else if (tmp[j] == '<')
					m[i][j] = 2;
				else if (tmp[j] == '^')
					m[i][j] = 3;
				else if (tmp[j] == '>')
					m[i][j] = 4;

			}
		}


		solve();
	}
	return 0;
}

