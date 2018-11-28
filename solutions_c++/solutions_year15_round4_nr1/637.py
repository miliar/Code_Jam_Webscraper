#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
typedef long long LL;

string str[100];
int dir[4][2] = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };

int getD(char ch) {
    if (ch == '^') return 0;
    if (ch == '>') return 1;
    if (ch == 'v') return 2;
    if (ch == '<') return 3;
    return -1;
}

void run() {
    int R, C;
    cin >> R >> C;
    REP(i, R) cin >> str[i];
    int res = 0;
    REP(r, R) {
        REP(c, C) {
            if (str[r][c] == '.') continue;
            int d = getD(str[r][c]);
            bool isok = false;
            int tr = r, tc = c;
            while (true) {
                tr += dir[d][0], tc += dir[d][1];
                if (tr < 0 || tr >= R || tc < 0 || tc >= C) break;
                if (str[tr][tc] != '.') {
                    isok = true;
                    break;
                }
            }
            if (isok) continue;
            REP(q, 4) {
                if (q == d) continue;
                int tr = r, tc = c;
                while (true) {
                    tr += dir[q][0], tc += dir[q][1];
                    if (tr < 0 || tr >= R || tc < 0 || tc >= C) break;
                    if (str[tr][tc] != '.') {
                        isok = true;
                        break;
                    }
                }
                if (isok) break;
            }
            if (isok) ++res;
            else {
                cout << "IMPOSSIBLE" << endl;
                return;
            }
        }
    }
    cout << res << endl;
}

int main() {
    int k;
    cin >> k;
    FOR(c,1,k) {
        cout << "Case #" << c << ": ";
        run();
    }
    return 0;
}
