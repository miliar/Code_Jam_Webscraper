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

int r, c, m;
char matr[8][8];

inline bool good(int x, int y) {
	return x >= 0 && y >= 0 && x < r && y < c;
}

void DFS(int x, int y) {
	char c = matr[x][y];
	matr[x][y] = ':';
	if (c != '.')
		return;
	for (int di = -1; di <= 1; di++)
		for (int dj = -1; dj <= 1; dj++) if (di || dj)
			if (good(x + di, y + dj)) {
				char& c = matr[x+di][y+dj];
				if (c != '*' && c != ';')
					DFS(x+di, y+dj);
			}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d%d", &r, &c, &m);

		bool imposs = true;
		for (int q = 0; q < (1<<(r*c)); q++) {
			memset(matr, 0, sizeof(matr));
			int kk = 0;
			for (int i = 0; i<r; i++)
				for (int j = 0; j<c; j++) {
					matr[i][j] = ((q >> (i*c+j)) & 1) ? '*' : '.';
					kk += (matr[i][j] == '*');
				}
			if (kk != m) continue;

			for (int i = 0; i<r; i++)
				for (int j = 0; j<c; j++) if (matr[i][j] == '.') {
					int kk = 0;
					for (int di = -1; di <= 1; di++)
						for (int dj = -1; dj <= 1; dj++) if (di || dj) {
							if (good(i+di, j+dj))
								kk += matr[i+di][j+dj] == '*';
						}
					if (kk > 0)
						matr[i][j] = '0' + kk;
				}

			int ci = -1, cj = -1;
			bool f = false;
			for (int i = 0; !f && i<r; i++)
				for (int j = 0; !f && j<c; j++) if (matr[i][j] == '.') {
					DFS(i, j);
					ci = i;  cj = j;
					f = true;
				}
			for (int i = 0; !f && i<r; i++)
				for (int j = 0; !f && j<c; j++) if (matr[i][j] != '*') {
					DFS(i, j);
					ci = i;  cj = j;
					f = true;
				}


			bool bad = false;
			for (int i = 0; i<r; i++)
				for (int j = 0; j<c; j++)
					if (matr[i][j] != ':' && matr[i][j] != '*')
						bad = true;
			
			if (!bad) {
				matr[ci][cj] = 'c';
				for (int i = 0; i<r; i++)
					for (int j = 0; j<c; j++)
						if (matr[i][j] >= '0' && matr[i][j] <= '9' || matr[i][j] == ':')
							matr[i][j] = '.';
				imposs = false;
				break;
			}
		}

		printf("Case #%d:\n", tt);
		if (imposs) printf("Impossible\n");
		else {
			for (int i = 0; i<r; i++) {
				matr[i][c] = 0;
				printf("%s\n", matr[i]);
			}
		}
		fflush(stdout);
	}
	return 0;
}
