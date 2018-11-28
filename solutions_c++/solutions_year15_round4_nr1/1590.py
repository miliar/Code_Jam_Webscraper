#include <iostream>
#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <string.h>

using namespace std;

int r, c;

string s[201];
string dir = "^<>v";
int ans;

bool check()
{
    // first line
    for (int j=0; j<c; ++j) {
        if (s[0][j] == 'v') continue;
        if (s[0][j] == '^') return false;
        if (s[0][j] == '.') {
            for (int i=1; i<r; ++i) {
                if (s[i][j] == '.') continue;
                if (s[i][j] == '^') return false;
                break;
            }
        }
    }
    // last line
    for (int j=0; j<c; ++j) {
        if (s[r-1][j] == '^') continue;
        if (s[r-1][j] == 'v') return false;
        if (s[r-1][j] == '.') {
            for (int i=0; i<r-1; ++i) {
                if (s[i][j] == '.') continue;
                if (s[i][j] == 'v') return false;
                break;
            }
        }
    }
    // first col
    for (int i=0; i<r; ++i) {
        if (s[i][0] == '<') return false;
        if (s[i][0] == '>') continue;
        if (s[i][0] == '.') {
            for (int j=1; j<c; ++j) {
                if (s[i][j] == '.') continue;
                if (s[i][j] == '<') return false;
                break;
            }
        }
    }
    // second col
    for (int i=0; i<r; ++i) {
        if (s[i][c-1] == '>') return false;
        if (s[i][c-1] == '<') continue;
        if (s[i][c-1] == '.') {
            for (int j=0; j<c-1; ++j) {
                if (s[i][j] == '.') continue;
                if (s[i][j] == '>') return false;
                break;
            }
        }
    }
    return true;
}

bool dfs(int x, int y, int d)
{
    if (check()) {
        if (d < ans) ans = d;
        return true;
    }
    if (d >= ans) return false;

    bool ok = false;
    while (1) {
        if (y == c) {
            x++;
            y=0;
        }
        if (x == r) {
            return false;
        }
        if (s[x][y] != '.') {
            for (int i=0; i<4; ++i) {
                if (s[x][y] == dir[i]) {
                    ok |= dfs(x, y+1, d);
                } else {
                    char old = s[x][y];
                    s[x][y] = dir[i];
                    ok |= dfs(x, y+1, d+1);
                    s[x][y] = old;
                }
            }
            break;
        }
        y++;
    }
    return ok;
}


bool left(int x, int y)
{
    for (int j=0; j<y; ++j) {
        if (s[x][j] != '.') return true;
    }
    return false;
}
bool right(int x, int y)
{
    for (int j=y+1; j<c; ++j) {
        if (s[x][j] != '.') return true;
    }
    return false;
}

bool up(int x, int y)
{
    for (int i=0; i<x; ++i) {
        if (s[i][y] != '.') return true;
    }
    return false;
}
bool down(int x, int y)
{
    for (int i=x+1; i<r; ++i) {
        if (s[i][y] != '.') return true;
    }
    return false;
}

void solve(int t)
{
    /*
    ans = r * c;
    if (dfs(0, 0, 0)) {
        cout << "Case #" << t << ": " << ans << endl;
    } else {
        cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
    }
    */
    int ans = 0;
    for (int i=0; i<r; ++i) {
        for (int j=0; j<c; ++j) {
            if (s[i][j] == '.') continue;
            if (!left(i,j) &&
                !right(i,j) &&
                !up(i,j) &&
                !down(i,j)) {
                cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
                return;
            }
            if (s[i][j] == '<' && !left(i,j)) ans++;
            if (s[i][j] == '>' && !right(i,j)) ans++;
            if (s[i][j] == '^' && !up(i,j)) ans++;
            if (s[i][j] == 'v' && !down(i,j)) ans++;
        }
    }
    cout << "Case #" << t << ": " << ans << endl;
    return;
}



int main()
{
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        cin >> r >> c;
        for (int i=0; i<r; ++i) {
            cin >> s[i];
        }
        solve(t);
    }
    return 0;
}
