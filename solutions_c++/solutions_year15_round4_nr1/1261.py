#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>

using namespace std;
FILE* in; FILE* out;

const int MAX = 104;

int n, m;
char board[MAX][MAX];
bool vis[MAX][MAX];
char dc[4] = { '^', '>', 'v', '<' };
int dir[4][2] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };

bool inside(int row, int col) {
    return row >= 0 && row < n && col >= 0 && col < m;
}

void findNext(int& row, int& col, int d) {
    row += dir[d][0], col += dir[d][1];
    while (inside(row, col) && board[row][col] == '.')
        row += dir[d][0], col += dir[d][1];
}

int fix(int row, int col) {
    if (vis[row][col]) {
        return 0;
    }
    vis[row][col] = true;
    int d = 0;
    while (board[row][col] != dc[d])
        d++;
    int nrow = row, ncol = col;
    findNext(nrow, ncol, d);
    // Can continue
    if (inside(nrow, ncol)) {
        return fix(nrow, ncol);
    }
    // Must fix
    for (int d = 0; d < 4; d++) {
        nrow = row, ncol = col;
        findNext(nrow, ncol, d);
        if (inside(nrow, ncol)) {
            board[row][col] = dc[d];
            break;
        }
    }
    return 1;
}

void solveTest() {
    fscanf(in, "%d %d", &n, &m);
    for (int row = 0; row < n; row++) {
        fscanf(in, "%s", board[row]);
    }
    vector <int> cntRow(n, 0);
    vector <int> cntCol(m, 0);
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < m; col++) {
            if (board[row][col] != '.') {
                cntRow[row]++;
                cntCol[col]++;
            }
        }
    }
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < m; col++) {
            if (board[row][col] != '.') {
                if (cntRow[row] == 1 && cntCol[col] == 1) {
                    fprintf(out, "IMPOSSIBLE\n");
                    return;
                }
            }
        }
    }
    
    int ans = 0;
    memset(vis, 0, sizeof(vis));
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < m; col++) {
            if (board[row][col] != '.' && !vis[row][col]) {
                ans += fix(row, col);
            }
        }
    }
    fprintf(out, "%d\n", ans);
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("Pegman.in", "rt");
	out = fopen("Pegman.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++) {
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		solveTest();
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n",
        (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	return 0;
}
