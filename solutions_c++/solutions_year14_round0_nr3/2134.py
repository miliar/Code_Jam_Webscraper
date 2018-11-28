#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>


using namespace std;

const int maxr = 50 + 5;
const int maxc = 50 + 5;

const int dx[8] = {1, 0, -1, 0, 1, 1, -1, -1};
const int dy[8] = {0, 1, 0, -1, 1, -1, 1, -1};

char a[maxr][maxc];
bool used[maxr][maxc];

bool check_zero(int x, int y, int r, int c)
{   
    for (int i = 0; i < 8; ++i) {
        int sx = x + dx[i];
        int sy = y + dy[i];
        if (0 <= sx && sx < r && 0 <= sy && sy < c && a[sx][sy] == '*') {
            return false;
        }
    }
    return true;
}

int dfs(int x, int y, int r, int c)
{
    used[x][y] = true;
    int res = 1;
    if (!check_zero(x, y, r, c)) {
        return res;
    }
    for (int i = 0; i < 8; ++i) {
        int sx = x + dx[i];
        int sy = y + dy[i];
        if (0 <= sx && sx < r && 0 <= sy && sy < c && a[sx][sy] == '.' && !used[sx][sy]) {
            res += dfs(sx, sy, r, c);
        }
    }
    return res;
}

void solve(int testNum)
{
    int r, c, m;
    cin >> r >> c >> m;

    int nmask = 1 << (r * c);
    bool good = false;
    for (int mask = 0; mask < nmask; ++mask) {
        int mm = 0;
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                bool mine = mask & (1 << (i * c + j));
                a[i][j] = mine ? '*' : '.';
                mm += mine;
            }
        }
        if (mm != m) {
            continue;
        }
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                if (a[i][j] == '*') {
                    continue;
                }
                if (check_zero(i, j, r, c) || r * c - m == 1) {
                    for (int i = 0; i < r; ++i) {
                        for (int j = 0; j < c; ++j) {
                            used[i][j] = false;
                        }
                    }
                    if (dfs(i, j, r, c) == r * c - m) {
                        good = true;
                        a[i][j] = 'c';       
                    }
                    goto for_res;
                }
            }
        }
        for_res:
        if (good) {
            break;         
        }
    }   
    cout << "Case #" << testNum << ":\n"; 
    if (good) {
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                cout << a[i][j];
            }
            cout << "\n";
        }
    }
    else {
        cout << "Impossible\n";
    }
}


int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        solve(i + 1);
    }
    return 0;
}
