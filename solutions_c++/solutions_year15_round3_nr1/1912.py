#include <cstdio>

int main ()
{
    int T;
    scanf ("%d", &T);
    for (int j = 1; j <= T; ++ j)
    {
        int R, C, W;
        scanf ("%d %d %d", &R, &C, &W);
        int numH = (C / W);
        if (C - W * numH > 0)
            ++ numH;
        printf ("Case #%d: %d\n", j, numH + W - 1);
    }
    return 0;
}

