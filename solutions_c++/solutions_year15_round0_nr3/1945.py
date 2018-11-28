#include <cstdio>

const int mat[5][5] = {{0, 0, 0, 0, 0},
    {
        0, 1, 2, 3, 4
    },
    {
        0, 2, -1, 4, -3
    },
    {
        0, 3, -4, -1, 2
    },
    {
        0, 4, 3, -2, -1
    }
};

char s[10005];

int main() {
    int T, l, x;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d", &l, &x);
        scanf("%s", s);
        int cur = 1;
        int ans = 0;
        for (int i = 0; i < x; i++)
            for (int j = 0; j < l; j++) {
                int ch = s[j] - 'i' + 2;
                //printf("cur = %d, ch = %d\n", cur, ch);
                cur = cur < 0 ? -mat[-cur][ch] : mat[cur][ch];
                if (ans == 0 && cur == 2) ans = 1;
                else if (ans == 1 && cur == 4) ans = 2;
        }
        //printf("cur = %d, ans = %d\n", cur, ans);
        printf("Case #%d: ", cas);
        if (ans == 2 && cur == -1) puts("YES");
        else puts("NO");
    }
    return 0;
}
