#pragma comment(linker, "/STACK:100000000")
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;
#define int64 long long
#define ldb long double
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define taskname "task_c"
const ldb pi = acos(-1.0);
const int N = 10;
bool data[N][N], used[N][N];
int marked, r, c, m, t;

bool bad(int x, int y) {
	return (x < 0) || (x >= r) || (y < 0) || (y >= c);
}

bool is_mine(int x, int y) {
	return !bad(x, y) && data[x][y];
}

int neigh(int x, int y) {
	int cnt = 0;
	for (int dx = -1; dx <= 1; ++dx)
		for (int dy = -1; dy <= 1; ++dy)
			cnt += (int) is_mine(x + dx, y + dy);
	return cnt;
}

void mark(int x, int y) {
	if (bad(x, y) || used[x][y]) return;
	used[x][y] = true, marked++;
	if (neigh(x, y) == 0)
		for (int dx = -1; dx <= 1; ++dx)
			for (int dy = -1; dy <= 1; ++dy)
				mark(x + dx, y + dy);
}

int main() {
	assert(freopen(taskname".in", "r", stdin));
	assert(freopen(taskname".out", "w", stdout));
	scanf("%d", &t);
	for (int it = 0; it < t; ++it) {
		scanf("%d%d%d", &r, &c, &m);
		bool done = false;
		printf("Case #%d:\n", it + 1);
		for (int mask = 0; !done && (mask < (1 << (r * c))); ++mask) {
			int tmask = mask, cnt = 0, si = 0, sj = 0;
			for (int i = 0; i < r; ++i)
				for (int j = 0; j < c; ++j) {
					data[i][j] = ((tmask & 1) == 1), tmask >>= 1, cnt += (int) (data[i][j]);
					if (!data[i][j]) si = i, sj = j;
				}
			if (cnt != m) continue;
			for (int i = 0; i < r; ++i)
				for (int j = 0; j < c; ++j)
					if (!data[i][j] && (neigh(i, j) == 0))
						si = i, sj = j;
			marked = 0, memset(used, 0, sizeof(used));
			mark(si, sj);
			if (marked + m == r * c) {
				done = true;
				for (int i = 0; i < r; ++i, printf("\n"))
					for (int j = 0; j < c; ++j)
						printf("%c", ((i == si) && (j == sj)) ? 'c' : (data[i][j] ? '*' : '.'));
			}
		}
		if (!done) printf("Impossible\n");
		eprintf("%d\n", it + 1);
	}
	return 0;
}