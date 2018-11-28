#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int map[205][205];
int C[4] = {-1, 1, 0, 0};
int D[4] = {0, 0, -1, 1};

int gett(int ch) {
    if (ch == '^') return 0;
    if (ch == 'v') return 1;
    if (ch == '<') return 2;
    if (ch == '>') return 3;
    return 4;
}

int n, m;

int ins(int x, int y) {
    if (x < 1 || x > n) return 0;
    if (y < 1 || y > m) return 0;
    return 1;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; ++i) 
            for (int j = 1; j <= m; ++j) {
                int ch;
                while (ch = getchar(), ch != '^' && ch != 'v' && ch != '<' && ch != '>' && ch != '.');
                map[i][j] = gett(ch);
            }
        int ans = 0;
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= m; ++j)
                if (map[i][j] != 4) {
                    int flag = 2;
                    for (int k = 0; k < 4; ++k) {
                        int x = i + C[k], y = j + D[k];
                        while (ins(x, y) && map[x][y] == 4) {
                            x += C[k], y += D[k];
                        }
                        if (ins(x, y)) {
                            flag = min(flag, (int)(k != map[i][j]));
                        }
                    }
                    if (flag == 2) ans += n * m * 2;
                    else ans += flag;
                }
        static int ca = 0;
        if (ans > n * m) printf("Case #%d: IMPOSSIBLE\n", ++ca); 
        else printf("Case #%d: %d\n", ++ca, ans);
    }
    return 0;
}
