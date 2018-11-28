//Author: Václav Volhejn (IAmWave)
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <queue>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define DIST 1
typedef long long ll;

void solve() {
    int r, c;
    cin >> r >> c;
    int state[110][110];
    rep(i, 0, r) {
        string s;
        cin >> s;
        rep(j, 0, c) {
            switch(s[j]) {
            case '^':
                state[i][j] = 1;
                break;
            case '>':
                state[i][j] = 2;
                break;
            case 'v':
                state[i][j] = 3;
                break;
            case '<':
                state[i][j] = 4;
                break;
            default:
                state[i][j] = 0;
                break;
            }
        }
    }
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {-1, 0, 1, 0};
    int res = 0;
    bool ok = true;
    rep(i, 0, r) rep(j, 0, c) {
        if(!state[i][j]) continue;
        //cout << i << "/" << j << "/" << state[i][j]<<endl;
        bool pts[4];
        rep(dir, 0, 4) {
            pts[dir] = false;
            int ci = i + dy[dir];
            int cj = j + dx[dir];
            while((ci >= 0) && (cj >= 0) && (ci < r) && (cj < c)) {
                if(state[ci][cj]) {
                    pts[dir] = true;
                    break;
                }
                ci += dy[dir];
                cj += dx[dir];
            }
        }
        //rep(g,0,4) cout << pts[g] << " "; cout << endl;
        //cout << "s" << state[i][j] << endl;
        if(!pts[state[i][j] - 1]) {
            bool k = false;
            rep(g,0,4) if(pts[g]) k = true;
            if(!k) ok = false;
            res++;
        }

    }
    if(ok) cout << res << endl;
    else cout << "IMPOSSIBLE" << endl;
}

int main() {
    if(DIST) {
        freopen("/home/vaclav/Downloads/A-large.in", "r", stdin);
        freopen("out.txt", "w", stdout);
    } else freopen("in.txt", "r", stdin);
    int cases;
    cin >> cases;
    rep(caseI, 0, cases) {
        cout << "Case #" << (caseI + 1) << ": ";
        solve();
    }
    return 0;
}
