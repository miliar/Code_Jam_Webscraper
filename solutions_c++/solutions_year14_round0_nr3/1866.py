#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <cassert>

using namespace std;

typedef unsigned int ui32;

const int INF = (int)1e+9;
const double EPS = (double)1e-9;
const int RMAX = 51;

char F[RMAX][RMAX];
bool use[RMAX][RMAX];
int Cnt[RMAX][RMAX];
int R, C, M;

const int dr[8] = { 0, -1, -1, -1, 0, 1, 1, 1 };
const int dc[8] = { 1, 1, 0, -1, -1, -1, 0, 1 };

int Neighbours(int row, int col) {
    int ret = 0;
    for (int step = 0; step < 8; ++step) {
        int nrow = row + dr[step];
        int ncol = col + dc[step];
        if (nrow >= 0 && nrow < R && ncol >= 0 && ncol < C) {
            ret += (F[nrow][ncol] == '*') ? 1 : 0;
        }
    }
    return ret;
}

bool HasAdjZero(int row, int col) {
    for (int step = 0; step < 8; ++step) {
        int nrow = row + dr[step];
        int ncol = col + dc[step];
        if (nrow >= 0 && nrow < R && ncol >= 0 && ncol < C) {
            if (Cnt[nrow][ncol] == 0)
                return true;
        }
    }
    return false;
}

void CalcCnt() {
    for (int row = 0; row < R; ++row) {
        for (int col = 0; col < C; ++col) {
            if (F[row][col] != '*') {
                Cnt[row][col] = Neighbours(row, col);
            } else {
                Cnt[row][col] = -1;
            }
        }
    }
}

void PutClick(int& srow, int& scol) {
    for (int row = 0; row < R; ++row)
        for (int col = 0; col < C; ++col)
            if (Cnt[row][col] == 0) {
                F[row][col] = 'c';
                srow = row;
                scol = col;
                return;
            }
    for (int row = 0; row < R; ++row)
        for (int col = 0; col < C; ++col)
            if (F[row][col] != '*') {
                F[row][col] = 'c';
                srow = row;
                scol = col;
                return;
            }
}

void dfs(int row, int col) {
    use[row][col] = true;
    if (Cnt[row][col] != 0)
        return;
    for (int step = 0; step < 8; ++step) {
        int nrow = row + dr[step];
        int ncol = col + dc[step];
        if (nrow >= 0 && nrow < R && ncol >= 0 && ncol < C) {
            if (!use[nrow][ncol])
                dfs(nrow, ncol);
        }
    }
}

bool IsOk() {
    if (M == R*C)
        return false;
    if (M == R*C - 1) {
        int d1, d2;
        PutClick(d1, d2);
        return true;
    }

    int srow = 0;
    int scol = 0;
    PutClick(srow, scol);
    memset(use, false, sizeof(use));
    dfs(srow, scol);
    for (int row = 0; row < R; ++row) {
        for (int col = 0; col < C; ++col) {
            if (F[row][col] != '*' && !use[row][col])
                return false;
        }
    }

    return true;
}

void PrintField() {
    for (int row = 0; row < R; ++row) {
        for (int col = 0; col < C; ++col) {
            printf("%c", F[row][col]);
        }
        printf("\n");
    }
}

int BitCnt(int num) {
    int ret = 0;
    while (num) {
        ret += (num & 1);
        num >>= 1;
    }
    return ret;
}

void FillFromMask(int mask) {
    assert(BitCnt(mask) == M);
    for (int row = 0; row < R; ++row) {
        for (int col = 0; col < C; ++col) {
            F[row][col] = (mask & 1) ? '*' : '.';
            mask >>= 1;
        }
    }
}

void Solve(int testId) {
    cin >> R >> C >> M;

    bool found = false;
    for (int mask = 0; mask < 1 << (R*C); ++mask) {
        if (BitCnt(mask) != M)
            continue;
        FillFromMask(mask);
        CalcCnt();

        if (!IsOk()) {
            continue;
        }
        found = true;
        break;
    }

    printf("Case #%d:\n", testId);
    if (found) {
        PrintField();
    } else {
        printf("Impossible\n");
    }
}

int main() {
    int testCount;
    cin >> testCount;
    for (int testId = 1; testId <= testCount; ++testId) {
        Solve(testId);
    }

    return 0;
}

