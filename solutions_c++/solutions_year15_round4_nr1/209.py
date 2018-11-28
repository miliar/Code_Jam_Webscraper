#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int maxn = 110;
const int ax[] = {0, 1, 0, -1};
const int ay[] = {1, 0, -1, 0};
char s[maxn][maxn];
int n, m;

int way(char c) {
    if (c == '>') return 0;
    if (c == 'v') return 1;
    if (c == '<') return 2;
    if (c == '^') return 3;
    return -1;
}

bool inborder(int x, int y) {
    return 1 <= x && x <= n && 1 <= y && y <= m;
}

int calc() {
    int ans = 0;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j) {
            if (way(s[i][j]) == -1) continue;
            int w = way(s[i][j]);
            int x = i, y = j;
            bool flag = true;
            while (true) {
                x += ax[w]; y += ay[w];
                if (!inborder(x, y)) {
                    flag = false;
                    break;
                }
                if (way(s[x][y]) != -1) break;
            }
            if (flag) continue;
            flag = false;
            ++ans;
            for (int ii = 0; ii < 4; ++ii) {
                if (ii == w) continue;
                x = i; y = j;
                bool ok = true;
                while (true) {
                    x += ax[ii], y += ay[ii];
                    if (!inborder(x, y)) {
                        ok = false;
                        break;
                    }
                    if (way(s[x][y]) != -1) break;
                }
                if (ok) {
                    flag = true;
                    break;
                }
            }
            if (!flag) return -1;
        }
    return ans;
}

int main() {
    int tt, cas = 0;
    cin >> tt;
    while (tt--) {
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; ++i)
            scanf("%s", s[i] + 1);
        printf("Case #%d: ", ++cas);
        int ans = calc();
        if (ans == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
}
