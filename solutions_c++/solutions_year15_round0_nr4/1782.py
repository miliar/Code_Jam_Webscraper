#include <cstdio>

void swap(int &x, int &y)
{
    int z = x;
    x = y;
    y = z;
}

int main()
{
    int T, X, R, C;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        scanf("%d%d%d", &X, &R, &C);
        int ok = C * R % X == 0;
        if (ok)
        {
            if (C < R) swap(R, C);
            ok = R * C % X == 0 && R >= X - 1;
        }
        printf("Case #%d: %s\n", t, ok ? "GABRIEL" : "RICHARD");
    }
    return 0;
}
