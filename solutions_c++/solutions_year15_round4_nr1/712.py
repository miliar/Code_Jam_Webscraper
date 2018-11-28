#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <ctime>
#include <numeric>

using namespace std;

#define sqr(a) ((a)*(a))
#define two(a) (1 << (a))
#define has(mask, a) ((mask) & two(a) ? 1 : 0)

const int di[] = {0, 1, 0, -1};
const int dj[] = {1, 0, -1, 0};

int n, m, sumi[105], sumj[105];
string a[105];
map<char, int> dirs;

void load() {
	scanf("%d%d", &n, &m);
	for (int i = 0;i < n;i++) {
		cin >> a[i];
	}
}

void solve(int test) {
	memset(sumi, 0, sizeof(sumi));
	memset(sumj, 0, sizeof(sumj));

	dirs['>'] = 0;
	dirs['v'] = 1;
	dirs['<'] = 2;
	dirs['^'] = 3;

	int ans = 0;
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < m;j++) {
			if (a[i][j] == '.') continue;

			sumi[i]++;
			sumj[j]++;

			bool ok = 0;
			int dir = dirs[a[i][j]];
			for (int k = 1;;k++) {
				int ni = i + k * di[dir];
				int nj = j + k * dj[dir];
				if (ni < 0 || ni >= n || nj < 0 || nj >= m) break;
				if (a[ni][nj] != '.') { 
					ok = 1;
					break;
				}
			}

			if (ok) continue;
			ans++;
		}
	}

	for (int i = 0;i < n;i++) {
		for (int j = 0;j < m;j++) {
			if (a[i][j] == '.') continue;

			if (sumi[i] == 1 && sumj[j] == 1) {
				printf ("Case #%d: IMPOSSIBLE\n", test);
				return;
			}
		}
	}

	printf ("Case #%d: %d\n", test, ans);
}

int main() {
 	freopen ("a.in", "r", stdin);

 	int t;
 	scanf ("%d\n", &t);

 	clock_t start = clock();
 	for (int i = 1;i <= t;i++) {
 		clock_t cur_start = clock();

 		fprintf(stderr, "Test %d:\n", i);
 		load();
 		solve(i);
 		fprintf(stderr, "Done in %.3f\n", (clock() - cur_start) / (double)CLOCKS_PER_SEC);
 	}

 	fprintf(stderr, "Total time: %.3f\n", (clock() - start) / (double)CLOCKS_PER_SEC);

 	return 0;
}