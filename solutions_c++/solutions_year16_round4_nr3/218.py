#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <cstring>

#define div divisor

using namespace std;

int r, c;
int grid[111][111];
int used[111][111][4];
int ans[111][111];
int Pair[1111];
int found;
int bad;

int Who(int x, int y, int side) {
    if (side == 0) {
        if (x == 1) {
            return y;
        }
    }
    if (side == 1) {
        if (y == c) {
            return c + x;
        }
    }
    if (side == 2) {
        if (x == r) {
            return r + c + (c - y + 1);
        }
    }
    if (side == 3) {
        if (y == 1) {
            return r + c + c + (r - x + 1);
        }
    }
    return -1;
}

void dfs(int x, int y, int side, int who) {
    if (x < 1) {
        return;
    }
    if (x > r) {
        return;
    }
    if (y < 1) {
        return;
    }
    if (y > c) {
        return;
    }
    if (used[x][y][side]) {
        return;
    }
    int W = Who(x, y, side);
    //cout << x << " " <<  y << " " << side << " " << W << " " << who << " " << Pair[who] << endl;
    if (W >= 0) {
        if (W != who && W != Pair[who]) {
            bad = 1;
            return;
        }
    }
    used[x][y][side] = 1;
    if (side == 0) {
        dfs(x - 1, y, 2, who);
    }
    if (side == 1) {
        dfs(x, y + 1, 3, who);
    }
    if (side == 2) {
        dfs(x + 1, y, 0, who);
    }
    if (side == 3) {
        dfs(x, y - 1, 1, who);
    }
    
    if (grid[x][y] == 0) {
        if (side == 0) {
            dfs(x, y, 3, who);
        }
        if (side == 1) {
            dfs(x, y , 2, who);
        }
        if (side == 2) {
            dfs(x, y, 1, who);
        }
        if (side == 3) {
            dfs(x, y, 0, who);
        }
    } else {
        if (side == 0) {
            dfs(x, y, 1, who);
        }
        if (side == 1) {
            dfs(x, y , 0, who);
        }
        if (side == 2) {
            dfs(x, y, 3, who);
        }
        if (side == 3) {
            dfs(x, y, 2, who);
        }
    }
}

void check() {
    bad = 0;    
    memset(used, 0, sizeof(used));
    for (int i = 1; i <= c; i++) {
        dfs(1, i, 0, Who(1, i ,0));
    }
    for (int i = 1; i <= r; i++) {
        dfs(i, c, 1, Who(i, c, 1));
    }
    for (int i = 1; i <= c; i++) {
        dfs(r, i, 2, Who(r, i, 2));
    }
    for (int i = 1; i <= r; i++) {
        dfs(i, 1, 3, Who(i, 1, 3));
    }
    if (!bad) {
        found = 1;
        for (int i = 1; i <= r; i++) {
            for (int j = 1; j <= c; j++) {
                ans[i][j] = grid[i][j];
            }
        }
    }
}

void gen(int x, int y) {    
    if (found) {
        return;
    }
    if (y > c) {
        x++;
        y = 1;
    }
    if (x > r) {
        check();
        return;
    }
    grid[x][y] = 0;
    gen(x, y + 1);
    grid[x][y] = 1;
    gen(x, y + 1);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int testCases;
    cin >> testCases;
    //testCases = 1;
    for (int testCase = 1; testCase <= testCases; testCase++) {
        cout << "Case #" << testCase << ": " << endl;
           
        cin >> r >> c;
        for (int i = 1; i <= r+c; i++) {
            int qq, ww;
            cin >> qq >> ww;
            Pair[qq] = ww;
            Pair[ww] = qq;
        }
        found = 0;
        gen(1, 1);
        if (!found) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            for (int i = 1; i <= r; i++) {
                for (int j = 1; j <= c; j++) {
                    cout << (ans[i][j] == 0 ? "/" : "\\");                    
                }
                cout << endl;
            }
        }
    } 
    return 0;
}