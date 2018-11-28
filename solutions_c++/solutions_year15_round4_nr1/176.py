#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define each(it,n) for(__typeof((n).begin()) it=(n).begin();it!=(n).end();++it)

using namespace std;

int dr[4] = {1, 0, -1, 0}, dc[4] = {0, 1, 0, -1};
// down right up left

void solve() {
    int R, C;
    cin >> R >> C;
    bool dir[4][100][100] = {0};
    vector<string> field(R);
    set<pair<int, int> > s;
    rep(i, R) cin >> field[i];
    
    for (int i = 0; i < R; i++) {
        bool flag = false;
        for (int j = 0; j < C; j++) {
            if (field[i][j] != '.') {
                dir[3][i][j] = flag;
                flag |= true;
            }
        }
        flag = false;
        for (int j = C - 1; j >= 0; j--) {
            if (field[i][j] != '.') {
                dir[1][i][j] = flag;
                flag |= true;
            }
        }
    }

    for (int j = 0; j < C; j++) {
        bool flag = false;
        for (int i = 0; i < R; i++) {
            if (field[i][j] != '.') {
                dir[2][i][j] = flag;
                flag |= true;
            }
        }
        flag = false;
        for (int i = R - 1; i >= 0; i--) {
            if (field[i][j] != '.') {
                dir[0][i][j] = flag;
                flag |= true;
            }
        }
    }

    int ans = 0;
    rep(i, R) {
        rep(j, C) {
            if (field[i][j] == '.') continue;
            if ((dir[0][i][j] ||
                dir[1][i][j] ||
                dir[2][i][j] ||
                dir[3][i][j]) == false) {
                cout << "IMPOSSIBLE" << endl;
                return;
            }
            switch(field[i][j]) {
            case 'v':
                if (dir[0][i][j] == false) ans++;
                break;
            case '>':
                if (dir[1][i][j] == false) ans++;
                break;
            case '^':
                if (dir[2][i][j] == false) ans++;
                break;
            case '<':
                if (dir[3][i][j] == false) ans++;
                break;
            }
        }
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << i + 1 << ": "; 
        solve();
    }
    return 0;
}
