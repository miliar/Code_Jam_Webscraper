#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int I, T, n, m;
int g[4][4], h[4][4];

int main() {
//    freopen("A-small-attempt0 (1).in", "r", stdin);
//    freopen("out.txt", "w", stdout);
    for (scanf("%d", &T), I=1; I<=T; I ++) {
        scanf("%d", &n);
        n--;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j ++)
                scanf("%d", &g[i][j]);
        scanf("%d", &m);
        m--;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j ++)
                scanf("%d", &h[i][j]);
        int ans = -1, cnt = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j ++) {
                if (g[n][i] == h[m][j]) {
                    cnt ++;
                    ans = g[n][i];
                }
            }
        }

        printf("Case #%d: ",I);
        if (cnt == 1) {
            printf("%d\n",ans);
        } else if (cnt == 0) {
            printf("Volunteer cheated!\n");
        } else if (cnt > 1) {
            printf("Bad magician!\n");
        }
    }
    return 0;
}
