#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

const int maxn = 10;
int can[maxn][maxn];
int n;
int a[maxn][maxn];
int visr[maxn], vism[maxn];

int check(int pos) {
    if(pos == n) {
        return 1;
    }
    int cnt = 0;
    int all = 0;
    for(int i = 0; i < n; i++) {
        if(visr[i] == 0) {
            int flag = 0;
            for(int j = 0; j < n; j++) {
                if(vism[j] == 0 && a[i][j] == 1) {
                    flag = 1;
                    visr[i] = 1;
                    vism[j] = 1;
                    if(check(pos + 1) == 0) {
                        return 0;
                    }
                    visr[i] = 0;
                    vism[j] = 0;
                }
            }
            if(flag == 0) {
                return 0;
            }
        }
    }
    return 1;
}

void solve() {
    int ans = 10000;
    int key = (1 << (n * n));
    for(int sta = 0; sta < key; sta++) {
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                a[i][j] = can[i][j];
            }
        }
        int cnt = 0;
        int flag = 1;
        for(int i = 0; i < n * n; i++) {
            if((1 << i) & sta) {
                cnt++;
                int x = i / n;
                int y = i % n;
                if(can[x][y] == 1) {
                    flag = 0;
                    break;
                } else {
                    a[x][y] = 1;
                }
            }
        }
        memset(visr, 0, sizeof(visr));
        memset(vism, 0, sizeof(vism));
        if(flag && check(0)) {
            ans = min(ans, cnt);
        }
    }
    printf("%d\n", ans);
}

char str[maxn];

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("Dout.txt", "w", stdout);
    int ncase;
    scanf("%d", &ncase);
    for(int i = 1; i <= ncase; i++) {
        printf("Case #%d: ", i);
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            scanf("%s", str);
            for(int j = 0; j < n; j++) {
                can[i][j] = str[j] - '0';
            }
        }
        solve();
    }
    return 0;
}
