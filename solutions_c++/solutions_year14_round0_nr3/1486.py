#include <cstdio>
#include <iostream>
#include <queue>
#include <set>
#include <cstring>

using namespace std;

int nTest;
int t, n, m;
char grid[55][55];

int ci[] = {0, 0, -1, 1, -1, -1, 1, 1};
int cj[] = {-1, 1, 0, 0, -1, 1, -1, 1};

deque<pair<int, int> > q;

void Open(int i, int j) {
	for(int k = 0; k < 8; k++) {
		int ii = i+ci[k];
		int jj = j+cj[k];
		if (ii > 0 && jj > 0 && ii <= n && jj <= m && grid[ii][jj] == '*') {
			grid[ii][jj] = '.';
			t--;
		}
	}
}
int Count(int i, int j) {
	int ret = 0;
	for(int k = 0; k < 8; k++) {
		int ii = i+ci[k];
		int jj = j+cj[k];
		if (ii > 0 && jj > 0 && ii <= n && jj <= m && grid[ii][jj] == '*') 
			ret++;
	}
	return ret;
}

void Output() {
	for(int i = 1; i <= n; i++) {
		for(int j = 1; j <= m; j++)
			printf("%c", grid[i][j]);
		printf("\n");
	}
}

int main() {

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	scanf("%d", &nTest);
	for(int test = 1; test <= nTest; test++) {
		scanf("%d%d%d", &n, &m, &t);
		t = n*m-t;

		memset(grid, '*', sizeof grid);
		grid[1][1] = 'c'; t--;
		if (t) Open(1, 1);
		while (t > 0) {
			bool Opened = 0;
			if (t%2 == 0)
				for(int i = 1; i <= n; i++) {
					for(int j = 1; j <= m; j++) {
						if (grid[i][j] != '*' && Count(i, j) == 2 && Count(i, j) <= t) {
							Opened = 1;
							Open(i, j);
							if (t&1) break;
						}
						if (grid[j][i] != '*' && Count(j, i) == 2 && Count(j, i) <= t) {
							Opened = 1;
							Open(j, i);
							if (t&1) break;
						}
					}
					if (t&1) break;
				}
			if (!Opened) {
				for(int i = 1; i <= n; i++) {
					for(int j = 1; j <= m; j++)
						if (grid[i][j] != '*' && Count(i, j)%2 == 1 && Count(i, j) <= t) {
							Opened = 1;
							Open(i, j);
							break;
						}
					if (Opened) break;
				}
			}
			if (!Opened) t = -1;
		}		
		
		printf("Case #%d:\n", test);
		if (t) printf("Impossible\n");
		else Output();
	}

	return 0;
}