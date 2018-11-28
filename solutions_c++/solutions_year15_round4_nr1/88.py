#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#ifdef HOME
	#define E(c) cerr<<#c
	#define Eo(x) cerr<<#x<<" = "<<(x)<<endl
	#define Ef(...) fprintf(stderr, __VA_ARGS__)
#else
	#define E(c) ((void)0)
	#define Eo(x) ((void)0)
	#define Ef(...) ((void)0)
#endif

const int SIZE = 128;
const char DirChars[] = "v>^<";
const int dir[4][2] = {{1,0}, {0,1}, {-1, 0}, {0, -1}};

int r, c;
char matr[SIZE][SIZE];

bool Move(int& x, int& y, char dch) {
	int d = -1;
	for (int i = 0; i < 4; i++)
		if (dch == DirChars[i])
			d = i;
	assert(d >= 0);
	int dx = dir[d][0];
	int dy = dir[d][1];
	while (1) {
		x += dx;  y += dy;
		if (!(x >= 0 && y >= 0 && x < r && y < c))
			return false;
		if (matr[x][y] != '.')
			return true;
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d", &r, &c);
		for (int i = 0; i<r; i++) scanf("%s", matr[i]);

		int ans = 0;
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				if (matr[i][j] == '.') continue;

				int ni = i, nj = j;
				if (Move(ni, nj, matr[i][j]))
					continue;

				bool ok = false;
				for (int d = 0; !ok && d < 4; d++) {
					int ni = i, nj = j;
					if (Move(ni, nj, DirChars[d]))
						ok = true;
				}

				ans = (ok ? ans+1 : 1000000000);
			}

		printf("Case #%d: ", tt);
		if (ans >= 1000000000) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
		fflush(stdout);
	}
	return 0;
}
