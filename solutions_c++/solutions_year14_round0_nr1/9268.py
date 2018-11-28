#include <cstdio>
#include <cstring>
int s[4][4], t[4][4];
int x, y;
bool f[16], g[16];

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d", &x);
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                scanf("%d", &s[i][j]);
        scanf("%d", &y);
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                scanf("%d", &t[i][j]);
        memset(f, 0, sizeof (f));
        memset(g, 0, sizeof (g));
        for (int i = 0; i < 4; i++)
            f[s[x - 1][i] - 1] = 1;
        for (int i = 0; i < 4; i++)
            g[t[y - 1][i] - 1] = 1;
        int cnt = 0, p;
        for (int i = 0; i < 16; i++)
            if (f[i] & g[i]) {
                cnt++;
                p = i;
            }
        printf("Case #%d: ", cas);
        if (cnt == 0) printf("Volunteer cheated!\n");
        else if (cnt == 1) printf("%d\n", p + 1);
        else printf("Bad magician!\n");
    }
    return 0;
}