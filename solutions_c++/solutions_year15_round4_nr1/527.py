#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int R, C;
char a[105][105];

bool off(int r, int c) {
    return r <= 0 || c <= 0 || r > R || c > C;
}

bool fall(int r, int c) {
    int dr = 0;
    int dc = 0;
    if(a[r][c] == '.') {
        return false;
    } else if(a[r][c] == '^') {
        dr = -1;
    } else if(a[r][c] == 'v') {
        dr = 1;
    } else if(a[r][c] == '>') {
        dc = 1;
    } else if(a[r][c] == '<') {
        dc = -1;
    } else {
        cerr << "Error\n";
    }
    
    r += dr;
    c += dc;
    while(!off(r, c)) {
        if(a[r][c] != '.') {
            return false;
        }
        r += dr;
        c += dc;
    }
    return true;
}

bool fix(int r, int c) {
    int dr[4] = {1,-1,0,0};
    int dc[4] = {0,0,1,-1};
    for(int d = 0; d < 4; d++) {
        int curR = r;
        int curC = c;
        curR += dr[d];
        curC += dc[d];
        while(!off(curR, curC)) {
            if(a[curR][curC] != '.') {
                return true;
            }
            curR += dr[d];
            curC += dc[d];
        }
    }
    return false;
}

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> R  >> C;
        int ans = 0;
        bool can = true;
        for(int r = 1; r <= R; r++) {
            for(int c = 1; c <= C; c++) {
                cin >> a[r][c];
            }
        }
        for(int r = 1; r <= R; r++) {
            for(int c = 1; c <= C; c++) {
                if(fall(r,c)) {
                    ans++;
                    if(!fix(r, c)) {
                        can = false;
                    }
                } else {
                    
                }
            }
        }
        
        cout << "Case #" << t << ": ";
        if(can) {
            cout << ans << "\n";
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }

    return 0;
}
