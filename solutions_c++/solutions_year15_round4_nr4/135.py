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

int n, m, ans;
vector<vector<int> > a;

set <vector<vector<int> > > s;

void load() {
	cin >> n >> m;
}

bool check(int i, int j) {
	int res = 0;
	for (int k = 0;k < 4;k++) {
		int ni = i + di[k];
		int nj = j + dj[k];

		nj = (nj + m) % m;

		if (ni >= 0 && ni < n && a[i][j] == a[ni][nj]) {
			res++;
		}
	}
	return res == a[i][j];
}

void go(int i, int j, bool was1, int f1) {
	if (j == m) {
		if (i == n - 1 && (!check(i, j - 1) || !check(i, 0))) return;
		i++;
		j = 0;
	}

	if (i == n) {
		/*for (int i = 0;i < n;i++) {
			for (int j = 0;j < m;j++) {
				cerr << a[i][j];
			}
			cerr << endl;
		}
		cerr << endl;*/

		if (s.count(a) > 0) return;

		for (int i = 0;i < m;i++) {
			vector<vector<int> > b = a;
			for (int q = 0;q < n;q++) {
				for (int w = 0;w < m;w++) {
					b[q][w] = a[q][(w + i) % m];
				}
			}
			s.insert(b);
		}

		ans++;
		return;
	}

	for (int cur = 1;cur <= 3;cur++) {
		if (!was1 && cur == 1 && j > 0) continue;

		if (f1 == i && j == m - 1 && cur == 1) continue;

		a[i][j] = cur;
		if (i > 0 && !check(i - 1, j)) continue;
		if (j > 1 && i == n - 1 && !check(i, j - 1)) continue;
		go(i, j + 1, was1 || cur == 1, !was1 && cur == 1 ? i : f1);
	}
}

void solve(int test) {
	ans = 0;
	a = vector<vector<int> > (n, vector<int> (m, 0));
	s.clear();
	go(0, 0, 0, -1);
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