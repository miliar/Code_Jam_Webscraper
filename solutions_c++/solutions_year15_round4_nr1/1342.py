#include <cstdio>

const int MAXN = 110;

int r, c;
char  s[MAXN][MAXN];
char dir[] = "^>v<";

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

bool go_out(int x, int y, int d)
{
    do {
        x += dx[d];
        y += dy[d];
    } while (x >= 0 && x < r && y >= 0 && y < c && s[x][y] == '.');

    if (x < 0 || x >= r || y < 0 || y >= c)
        return true;

    return false;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int tt = 1; tt <= T; ++tt) {
        scanf("%d%d", &r, &c);
        for (int i = 0; i < r; ++i)
            scanf("%s", s[i]);
        //printf("%d%d\n", r, c);
        bool imp = false;
        int ans = 0;
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < c; ++j)
                if (s[i][j] != '.') {
                    //puts("aa");
                    int cnt = 0;
                    for (int d = 0; d < 4; ++d)
                        if (!go_out(i, j, d)) {
                            ++cnt;
                            if (dir[d] == s[i][j])
                                --ans;
                        }
                    if (cnt == 0)
                        imp = true;
                    else {
                        ++ans;
                    }
                }
        printf("Case #%d: ", tt);
        if (imp)
            printf("IMPOSSIBLE\n");
        else {
            printf("%d\n", ans);
        }
    }
    return 0;
}
