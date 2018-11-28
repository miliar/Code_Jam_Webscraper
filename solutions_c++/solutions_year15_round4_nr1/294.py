#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int kMaxN = 200, kMaxM = 200;
int n, m;
char buf[kMaxN][kMaxM + 1];

const int kFx[4] = {-1, 1, 0, 0};
const int kFy[4] = {0, 0, -1, 1};

bool inr(int x, int y) {
    return (x >= 0 && x < n && y >= 0 && y < m);
}

void solve() {
    int res = 0;
    for (int i = 0; i < n; ++ i)
        for (int j = 0; j < m; ++ j)
            if (buf[i][j] != '.') {
                bool chk = false;
                for (int jj = 0; jj < m; ++ jj)
                    if (jj != j && buf[i][jj] != '.') chk = true;
                for (int ii = 0; ii < n; ++ ii)
                    if (ii != i && buf[ii][j] != '.') chk = true;
                if (!chk) {
                    puts("IMPOSSIBLE");
                    return;
                }
                int d;
                if (buf[i][j] == '^') d = 0;
                else if (buf[i][j] == 'v') d = 1;
                else if (buf[i][j] == '<') d = 2;
                else d = 3;
                chk = false;
                for (int k = 1; inr(i + kFx[d] * k, j + kFy[d] * k); ++ k)
                    if (buf[i + kFx[d] * k][j + kFy[d] * k] != '.') chk = true;
                if (!chk) ++ res;
            }
    printf("%d\n", res);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; ++ kase) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++ i) scanf("%s", buf[i]);
        printf("Case #%d: ", kase);
        solve();
    }
    return 0;
}
