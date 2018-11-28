#include <cstdio>
#include <cstring>

int a[5][5];
int v[5][5];
int r, c, m;
bool e[5][5];

#define inr(_x_, _y_) ((_x_) >= 0 && (_x_) < r && (_y_) >= 0 && (_y_) < c)

bool can_put(int x, int y) {
    memset(e, false, sizeof(e));
    int q[25], qh = 0, qt = 0;
    q[qt ++] = x * c + y;
    e[x][y] = true;
    while (qh != qt) {
        int u = q[qh ++];
        x = u / c;
        y = u % c;
        if (v[x][y] == 0) {
            for (int i = x - 1; i <= x + 1; ++ i)
                for (int j = y - 1; j <= y + 1; ++ j)
                    if (inr(i, j) && !e[i][j]) {
                        q[qt ++] = i * c + j;
                        e[i][j] = true;
                    }
        }
    }
    return (qt == r * c - m);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int kase = 0; kase < T; ++ kase) {
        scanf("%d%d%d", &r, &c, &m);
        printf("Case #%d:\n", kase + 1);
        for (int msk = 0; msk < 1 << (r * c); ++ msk)
            if (__builtin_popcount(msk) == m) {
                for (int i = 0; i < r; ++ i)
                    for (int j = 0; j < c; ++ j)
                        a[i][j] = msk >> (i * c + j) & 1;
                int rest = ((1 << (r * c)) - 1) ^ msk;
                for (int i = 0; i < r; ++ i)
                    for (int j = 0; j < c; ++ j) {
                        v[i][j] = 0;
                        for (int x = i - 1; x <= i + 1; ++ x)
                            for (int y = j - 1; y <= j + 1; ++ y)
                                if (inr(x, y)) v[i][j] += a[x][y];
                    }
                while (rest) {
                    int p = rest & -rest;
                    rest ^= p;
                    p = __builtin_ctz(p);
                    int x = p / c;
                    int y = p % c;
                    if (can_put(x, y)) {
                        for (int i = 0; i < r; ++ i) {
                            for (int j = 0; j < c; ++ j)
                                if (i == x && j == y) putchar('c');
                                else if (a[i][j]) putchar('*');
                                else putchar('.');
                            puts("");
                        }
                        goto END;
                    }
                }
            }
        printf("Impossible\n");
        END:
        ;
    }
    return 0;
}
