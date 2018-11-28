#include <stdio.h>

const int MAXRC = 16;
int r, c;
int p[MAXRC * 4];
int f[MAXRC * 4];

int find(int i)
{
    return f[i] == i ? i : f[i] = find(f[i]);
}

void merge(int x, int y)
{
    x = find(x), y = find(y);
    f[x] = y;
}

int tr(int i)
{
    if (i < c) return i * 4;
    i -= c;
    if (i < r) return (i * c + c - 1) * 4 + 1;
    i -= r;
    if (i < c) return ((r - 1) * c + (c - i - 1)) * 4 + 2;
    i -= c;
    return ((r - i - 1) * c + 0) * 4 + 3;
}

bool check(int mask)
{
    for (int i = 0; i < r * c * 4; ++i) f[i] = i;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            int t = (i * c + j) * 4;
            if ((mask&1) == 0) { // '/'
                merge(t + 0, t + 3);
                merge(t + 1, t + 2);
            } else { // '\'
                merge(t + 0, t + 1);
                merge(t + 2, t + 3);
            }
            mask >>= 1;

            if (i) merge(t + 0, t - 4 * c + 2);
            if (j) merge(t + 3, t - 4 + 1);
        }
    }
    for (int i = 0; i < 2 * (r + c); i += 2) {
        if (find(tr(p[i])) != find(tr(p[i + 1]))) return false;
    }
    return true;
}

void init()
{
    scanf("%d%d", &r, &c);
    for (int i = 0; i < 2 * (r + c); ++i) {
        scanf("%d", &p[i]);
        --p[i];
    }
}

void solve()
{
    for (int mask = 0; mask < (1<<(r*c)); ++mask) {
        if (check(mask)) {
            for (int i = 0; i < r; ++i) {
                for (int j = 0; j < c; ++j) {
                    putchar("/\\"[mask&1]);
                    mask >>= 1;
                }
                puts("");
            }
            return;
        }
    }
    puts("IMPOSSIBLE");
}

int main()
{
    int dat;
    scanf("%d", &dat);
    for (int cas = 1; cas <= dat; ++cas) {
        printf("Case #%d:\n", cas);
        init();
        solve();
    }
}
