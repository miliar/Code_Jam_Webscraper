#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <cassert>
#include <map>
#include <vector>
#include <queue>
#include <deque>
#include <sstream>
#include <iomanip>
using namespace std;
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef pair <int, int> PII;
const int N = 105;
int Tc, m, n;
char mat[N][N];
bool ban[N][N][4];
char rr[4][2] = {
    {'^', 0},
    {'v', 1},
    {'<', 2},
    {'>', 3}
};

char getRef(char c) {
    rep (i, 4) {
        if (rr[i][0] == c) {
            return rr[i][1];
        }
    }
    assert(0);
}

int main() {
    cin >> Tc;
    rep (ri, Tc) {
        printf("Case #%d: ", ri + 1);
        cin >> m >> n;
        rep (i, m) rep (j, n) {
            cin >> mat[i][j];
        }
        memset(ban, 0, sizeof(ban));
        rep (i, m) rep (j, n) {
            int k;
            if (i == 0) {
                k = i;
                while (k < m && mat[k][j] == '.') k++;
                if (k < m) {
                    ban[k][j][0] = 1;
                }
            }
            if (i + 1 == m) {
                k = i;
                while (k >= 0 && mat[k][j] == '.') k--;
                if (k >= 0) {
                    ban[k][j][1] = 1;
                }
            }
            if (j == 0) {
                k = j;
                while (k < n && mat[i][k] == '.') k++;
                if (k < n) {
                    ban[i][k][2] = 1;
                }
            }
            if (j + 1 == n) {
                k = j;
                while (k >= 0 && mat[i][k] == '.') k--;
                if (k >= 0) {
                    ban[i][k][3] = 1;
                }
            }
        }
        int ans = 0;
        bool bad = false;
        rep (i, m) rep (j, n) {
            if (mat[i][j] != '.') {
                int cnt = 0;
                rep (k, 4) cnt += ban[i][j][k];
                if (cnt == 4) {
                    bad = true;
                }
                if (ban[i][j][getRef(mat[i][j])]) {
                    ans++;
                }
            }
        }
        if (bad) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", ans);
        }
    }
    return 0;
}

