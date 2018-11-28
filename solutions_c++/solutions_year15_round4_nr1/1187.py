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
#define taskname "task_a"
const ldb pi = acos(-1.0);
const int N = 1111;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};
const char* dirs = "^v<>";
int n, m, t;
char a[N][N];

bool on_board(int x, int y) {
	return ((x >= 0) && (x < n) && (y >= 0) && (y < m));
}

int main() {
//	assert(freopen(taskname".in", "r", stdin));
//	assert(freopen(taskname".out", "w", stdout));
	scanf("%d", &t);
	for (int it = 0; it < t; ++it) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				scanf(" %c", &a[i][j]);
		int res = 0;
		bool bad = false;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j) {
				if (a[i][j] == '.') continue;
				bool ok[4], any_ok = false;
				for (int dir = 0; dir < 4; ++dir) {
					int x = i + dx[dir], y = j + dy[dir];
					while (on_board(x, y) && (a[x][y] == '.'))
						x += dx[dir], y += dy[dir];
					ok[dir] = on_board(x, y);
					any_ok |= ok[dir];
				}
				if (!any_ok)
					bad = true;
				else if (!ok[strchr(dirs, a[i][j]) - dirs])
					++res;
			}
		printf("Case #%d: ", it + 1);
		if (bad)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", res);
	}	
	return 0;
}
