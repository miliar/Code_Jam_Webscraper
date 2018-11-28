#include <cstdio>

int main ()
{
    int T;
    scanf ("%d\n", &T);
    for (int j = 1; j <= T; ++ j)
    {
        int X, R, C;
        scanf ("%d %d %d", &X, &R, &C);
        if (X == 1)
            printf ("Case #%d: GABRIEL\n", j);
        else if (X == 2)
        {
            if ((R*C) % 2 == 0)
                printf ("Case #%d: GABRIEL\n", j);
            else
                printf ("Case #%d: RICHARD\n", j);
        }
        else if (X == 3)
        {
            if ((R*C) % 3 == 0 && R*C > 3)
                printf ("Case #%d: GABRIEL\n", j);
            else
                printf ("Case #%d: RICHARD\n", j);
        }
        else if (X == 4)
        {
            if ((R == 4 && C == 4) || (R == 3 && C == 4) || (R == 4 && C == 3))
                printf ("Case #%d: GABRIEL\n", j);
            else
                printf ("Case #%d: RICHARD\n", j);
        }
    }
}

