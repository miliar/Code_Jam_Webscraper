#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>

using namespace std;

typedef long long ll;
typedef vector<int> vecint;
typedef pair<int, int> ppi;
typedef vector< pair<int, int> > vecppi;

#define fill(a,x) memset(a, (x), sizeof(a))
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

int read() {   int x;   scanf("%d",&x);   return x;   }
int read(int &x) {  scanf("%d",&x);     return x;   }



const int MAX_N = 11;
const int dx[8] = {-1, -1, -1, 0, +1, +1, +1, 0};
const int dy[8] = {-1, 0, +1, +1, +1, 0, -1, -1};



int m, n, nMine;
int a[MAX_N][MAX_N];
bool visited[MAX_N][MAX_N];



bool onBoard(int x, int y) {
	return (x >= 0) && (x < m) && (y >= 0) && (y < n);
}



int dfs(int i, int j) {
	visited[i][j] = true;
	int c = 1;
	if (a[i][j] == 0)
		for (int k = 0; k < 8; ++k) {
			int x = i+dx[k];
			int y = j+dy[k];
			if (onBoard(x, y) && a[x][y] != -1 && !visited[x][y])
				c += dfs(x, y);
		}
	return c;
}



int calA(int &sx, int &sy) {
	int c = 0;
	for (int i = 0; i < m; ++i)
		for (int j = 0; j < n; ++j) if (a[i][j] != -1) {
			++c;
			for (int k = 0; k < 8; ++k) {
				int x = i+dx[k];
				int y = j+dy[k];
				if (onBoard(x, y) && a[x][y] == -1) ++a[i][j];
			}
			if (a[i][j] == 0) {
				sx = i;
				sy = j;
			}
		}
	if (sx == -1)
		for (int i = 0; i < m; ++i)
			for (int j = 0; j < n; ++j)
				if (a[i][j] != -1) {
					sx = i;
					sy = j;
				}
	return c;
}



void print_result(int sx, int sy) {
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j)
			if (a[i][j] == -1) printf("*");
			else if (i == sx && j == sy) printf("c");
			else printf(".");
		printf("\n");
	}
}



bool check() {
	int sx = -1, sy = -1;
	int c = calA(sx, sy);
	fill(visited, false);
	if (c && sx >= 0 && dfs(sx, sy) == c) {
		print_result(sx, sy);
		return true;
	}
	return false;
}



void solve() {
	int sizeA = m*n;
	int limit = (1<<sizeA);
	//cout << sizeA << " " << limit << endl;

	for (int mask = 0; mask < limit; ++mask) {
		fill(a, 0);
		int cMine = 0;
		for (int i = 0; i < sizeA; ++i)
			if (mask&(1<<i)) {
				int x = i/n;
				int y = i - x*n;
				a[x][y] = -1;
				++cMine;
			}
		if (cMine != nMine) continue;
		if (check()) return;
	}
	printf("Impossible\n");
}



int main() {
#ifdef DEBUG
	freopen("C-small-attempt4.in", "r", stdin);
	freopen("C.out", "w", stdout);
#endif
	int nTest = read();
	for (int test_id = 1; test_id <= nTest; ++test_id) {
		scanf("%d%d%d", &m, &n, &nMine);
		printf("Case #%d:\n", test_id);
		solve();
	}
	return 0;
}