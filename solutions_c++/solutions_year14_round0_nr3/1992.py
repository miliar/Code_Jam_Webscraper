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

const int MAX = 16;

int n, m, k;
int a[MAX][MAX];
char board[MAX][MAX];
int dir[8][2] = { {-1, -1}, {-1, 0}, {-1, +1}, {0, -1}, 
                  {0, +1}, {+1, -1}, {+1, 0}, {+1, +1} };

int flood(int row, int col) {
    int ret = 1;
    a[row][col] = 3;
    for (int i = 0; i < 8; i++) {
        int nrow = row + dir[i][0]; if (nrow < 0 || nrow >= n) continue;
        int ncol = col + dir[i][1]; if (ncol < 0 || ncol >= m) continue;
        if (a[nrow][ncol] == 0)
            ret += flood(nrow, ncol);
    }
    return ret;
}

bool check() {
    memset(a, 0, sizeof(a));
    int borders = 0;
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < m; col++) {
            if (board[row][col] == '*')
                a[row][col] = 1;
            else {
                bool border = false;
                for (int i = 0; i < 8; i++) {
                    int nrow = row + dir[i][0]; if (nrow < 0 || nrow >= n) continue;
                    int ncol = col + dir[i][1]; if (ncol < 0 || ncol >= m) continue;
                    if (board[nrow][ncol] == '*') {
                        border = true;
                        break;
                    }
                }
                if (border) {
                    borders++;
                    a[row][col] = 2;
                }
            }
        }
    }
    int rem = n * m - k - borders;
    if (rem == 0 && borders == 1) {
        for (int row = 0; row < n; row++)
            for (int col = 0; col < m; col++)
                if (a[row][col] == 2) board[row][col] = 'c';
        return true;
    }
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < m; col++) {
            if (a[row][col] == 2) {
                bool flag = false;
                for (int i = 0; i < 8; i++) {
                    int nrow = row + dir[i][0]; if (nrow < 0 || nrow >= n) continue;
                    int ncol = col + dir[i][1]; if (ncol < 0 || ncol >= m) continue;
                    if (a[nrow][ncol] == 0) {
                        flag = true;
                        break;
                    }
                }
                if (!flag)
                    return false;
            }
        }
    }
    bool flag = true;
    for (int row = 0; flag && row < n; row++) {
        for (int col = 0; flag && col < m; col++) {
            if (a[row][col] == 0) {
                if (flood(row, col) == rem) {
                    board[row][col] = 'c';
                    return true;
                }
                flag = false;
            }
        }
    }
    return false;
}

bool recurse(int row, int col, int put) {
    if (row >= n) {
        if (put != k)
           return false;
        return check();
    }
    if (col >= m)
        return recurse(row + 1, 0, put);
    
    // Some simple heuristic
    if (put + (n - row - 1) * m + m - col < k)
        return false;
    
    // Not a mine
    if (recurse(row, col + 1, put))
        return true;

    // A mine
    if (put < k) {
        board[row][col] = '*';
        if (recurse(row, col + 1, put + 1))
            return true;
        board[row][col] = '.';
    }
    return false;
}

void solveTest(int test) {
    fscanf(in, "%d %d %d", &n, &m, &k);
    memset(board, '.', sizeof(board));
    for (int row = 0; row < n; row++)
        board[row][m] = 0;

    if (!recurse(0, 0, 0))
        fprintf(out, "Impossible\n");
    else {
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < m; col++)
                fprintf(out, "%c", board[row][col]);
            fprintf(out, "\n");
        }
    }
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("MinesweeperMaster.in", "rt");
	out = fopen("MinesweeperMaster.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++) {
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d:\n", test);
		solveTest(test);
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n", (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	return 0;
}
