#include <cstdio>

int T, a[4][4], b[4][4], c1, c2;

void solve() {
    int cnt = 0, ans;
    for(int i = 0; i < 4; ++i) {
        for(int j = 0; j < 4; ++j) {
            if(a[c1 - 1][i] == b[c2 - 1][j]) {
                cnt++, ans = a[c1 - 1][i];
            }
        }
    }
    if(cnt == 0) {
        puts("Volunteer cheated!");
        return;
    }
    if(cnt == 1) {
        printf("%d\n", ans);
        return;
    }
    puts("Bad magician!");
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    for(int test = 1; test <= T; ++test) {
        scanf("%d", &c1);
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                scanf("%d", &a[i][j]);
            }
        }
        scanf("%d", &c2);
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                scanf("%d", &b[i][j]);
            }
        }
        printf("Case #%d: ", test);
        solve();
    }
    return 0;
}
