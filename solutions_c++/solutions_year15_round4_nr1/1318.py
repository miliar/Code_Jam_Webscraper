#include <bits/stdc++.h>

using namespace std;

const int N = 110;

char s[N][N];
int n, m, ans;
int dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1};
// D R U L

int get(char cc) {
    if(cc == 'v') return 0;
    if(cc == '>') return 1;
    if(cc == '^') return 2;
    if(cc == '<') return 3;
}

void solve() {
    scanf("%d%d", &n, &m);
    ans = 0;
    for(int i = 0; i < n; i++) {
        scanf("%s", s[i]);
    }
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(s[i][j] == '.') continue;
            int k = get(s[i][j]);
            int x = i + dx[k], y = j + dy[k], cc = 0;
            while(x >= 0 && x < n && y >= 0 && y < m) {
                if(s[x][y] != '.') {
                    cc ++; break;
                }
                x += dx[k]; y += dy[k];
            }
            if(cc == 0) ans ++;
            int o = k;
            for(k = 0; k < 4; k++) {
                if(o == k) continue;
                int x = i + dx[k], y = j + dy[k];
                while(x >= 0 && x < n && y >= 0 && y < m) {
                    if(s[x][y] != '.') {
                        cc ++; break;
                    }
                    x += dx[k]; y += dy[k];
                }
            }
            if(cc == 0) {
                puts("IMPOSSIBLE");
                return;
            }
        }
    }
    printf("%d\n", ans);
}

int main() {
    freopen("A1.in", "r", stdin);
    freopen("A1.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        printf("Case #%d: ", ++ cas);
        solve();
    }
    return 0;
}