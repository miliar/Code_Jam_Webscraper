#include <map>
#include <set>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long lint;
#define pp(a,b) push_back(make_pair((a),(b)))
#define pb push_back
#define mp make_pair
#define buybuy {printf("-1\n");return 0;}

int next() {int x; cin >> x; return x;}
lint lnext() {lint x; cin >> x; return x;}
//template<typename T> outln(T x) {cout << x; cout << "\n";}
#define prt(a) cout << a << "\n";
#define prtn(a, n) for(int iiiiiiiiiii = 0; iiiiiiiiiii < n; iiiiiiiiiii++) cout << a[iiiiiiiiiii] << " "; cout << "\n;"
#define prtall(a) for (auto iiiiiiiiiii : a) cout << iiiiiiiiiii << " "; cout << "\n";

int grid[100][100];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0, 1};

bool can(int x, int y, int dir) {
	do {
		x += dx[dir];
		y += dy[dir];
		if (x < 0 || x >= 100 || y < 0 || y >= 100) break;
		if (grid[y][x] >= 0) return true;
	} while (1);
	return false;
}

int main() {
	int tests = next();
	for (int test = 1; test <= tests; test++) {
		for (int i = 0; i < 100; i++) for (int j = 0; j < 100; j++) grid[i][j] = -1;
		int r = next(), c = next();
		for (int i = 0; i < r; i++) {
			string s;
			cin >> s;
			for (int j = 0; j < c; j++) {
				if (s[j] == '.') grid[i][j] = -1;
				if (s[j] == '>') grid[i][j] = 0;
				if (s[j] == '^') grid[i][j] = 1;
				if (s[j] == '<') grid[i][j] = 2;
				if (s[j] == 'v') grid[i][j] = 3;
			}
		}

		/*for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) printf("%d ", grid[i][j]);
			printf("\n");
		}*/

		bool poss = true;
		int cnt = 0;
		for (int i = 0; i < r && poss; i++) for (int j = 0; j < c; j++) if (grid[i][j] >= 0) {
			bool p = false;
			for (int dir = 0; dir < 4; dir++) p |= can(j, i, dir);
			if (!p) poss = false;
			if (!can(j, i, grid[i][j])) cnt++;
		}
		
		if (poss) printf("Case #%d: %d\n", test, cnt);
		else printf("Case #%d: IMPOSSIBLE\n", test);
	}

}
