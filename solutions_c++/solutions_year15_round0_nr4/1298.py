#include <cstdio>
#include <cstdlib>
#include <cstring>

int a[1010];

bool can(int x, int r, int c)
{
    if (x == 4 && r == 2 && c == 4)
        return false;
    bool gab_win = true;
    if (r * c % x > 0 || ((x + 1) / 2 > r || x / 2 + 1 > c))
        gab_win = false;
    return gab_win;
}

int main()
{
    int T;
    /*
    for (int x = 1; x <= 4; ++x)
        for (int r = 1; r <= 4; ++r)
            for (int c = r; c <= 4; ++c)
                //if (r * c % x == 0)
                if (can(x, r, c))
                    printf("%d %d %d\n", x, r, c);
                    */
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int x, r, c;
        scanf("%d%d%d", &x, &r, &c);
        if (r > c)
        {
            int tmp = r; r = c; c = tmp;
        }
        printf("Case #%d: %s\n", t, can(x, r, c)?"GABRIEL":"RICHARD");
    }

    return 0;
}
