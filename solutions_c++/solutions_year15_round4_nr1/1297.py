#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#define MAXR 105

using namespace std;

int dr[] = {-1,0,1,0};
int dc[] = {0,1,0,-1};

int r,c;
char b[MAXR][MAXR];
int ans;

bool go(int sr, int sc, int d) {
    int rr = sr + dr[d], cc = sc + dc[d];
    while (b[rr][cc]) {
        if (b[rr][cc] != '.') break;
        rr += dr[d];
        cc += dc[d];
    }
    if (b[rr][cc] == 0) return 0;
    return 1;
 }

int main() {
    int T;
    cin >> T;
    for (int TC = 1; TC <= T; TC++) {
        memset(b,0,sizeof(b));
        ans = 0;
        cin >> r >> c;
        for (int i = 1; i <= r; i++) {
            cin >> b[i]+1;
        }
        bool ok = 1;
        for (int i = 1; i <= r && ok; i++) {
            for (int j = 1; j <= c && ok; j++) {
                if (b[i][j] == '.') continue;
                int d = -1;
                if (b[i][j] == '^') d = 0;
                if (b[i][j] == '>') d = 1;
                if (b[i][j] == 'v') d = 2;
                if (b[i][j] == '<') d = 3;
                if (!go(i,j,d)) {
                    ans++;
                    bool flag = 0;
                    for (int k = 0; k < 4 && !flag; k++) {
                        if (go(i,j,k)) flag = 1;
                    }
                    if (!flag) ok = 0;
                }
            }
        }
        cout << "Case #" << TC << ": ";
        if (ok) cout << ans << '\n';
        else cout << "IMPOSSIBLE\n";
    }
}
