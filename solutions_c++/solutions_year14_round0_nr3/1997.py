#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <string.h>
#include <sstream>
#include <stdlib.h>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

const int N = 33;
int n, m;
char a[N][N];
bool used[N][N];
bool good;

bool have(int x, int y) {
    if (x < 0 || y < 0 || x >= n || y >= m) return false;
    return a[x][y] == '*';
}

int calc(int x, int y) {
    int cnt = 0;
    for (int dx = -1; dx <= 1; ++dx)
        for (int dy = -1; dy <= 1; ++dy)
            if (dx != 0 || dy != 0)
                if (have(x + dx, y + dy)) ++cnt;
    return cnt;
}

void doit(int x, int y) {
    if (x < 0 || y < 0 || x >= n || y >= m) return;
    if (a[x][y] == '*') return;
    if (used[x][y]) return;
    used[x][y] = true;
    if (calc(x, y) == 0) {
        for (int dx = -1; dx <= 1; ++dx)
            for (int dy = -1; dy <= 1; ++dy) doit(x + dx, y + dy);
    }
}

void rec(int x, int y, int cnt) {
    if (x == n) {
        if (cnt != 0) return; 
        
        for (int x = 0; x < n; ++x)
            for (int y = 0; y < m; ++y)
                if (a[x][y] == '.') {
                    memset(used, 0, sizeof(used));
                    doit(x, y);

                    bool cool = true;
                    for (int i = 0; cool && i < n; ++i)
                        for (int j = 0; j < m; ++j)
                            if (a[i][j] == '.' && !used[i][j]) {
                                cool = false;
                                break;
                            }
                    if (cool) {
                        a[x][y] = 'c';
                        good = true;
                        return;
                    }
                }
        return;
    }
    if (y >= m) {
        rec(x + 1, 0, cnt);
        return;
    }

    if (cnt) {
        a[x][y] = '*';
        rec(x, y + 1, cnt - 1);
        if (good) return;
    }
    a[x][y] = '.';
    rec(x, y + 1, cnt);
}


int main() {
    int _T;
    scanf("%d\n", &_T);

    for (int _ = 1; _ <= _T; _++) {
        printf("Case #%d:\n", _);
        good = false;

        int mines;
        cin >> n >> m >> mines; 
        rec(0, 0, mines);
        if (good) {
            for (int i = 0; i < n; ++i) {
                a[i][m] = 0;
                puts(a[i]);
            }
        } else puts("Impossible");
    }
    
    return 0;
}
