#include <stdio.h>

int main()
{
    int T, r, t, x;
    scanf("%d", &T);
    for (int i = 0; i < T; ++i)
    {
        scanf("%d %d", &r, &t);
        for (x = t/(2*r); 2*x*r + x*(2*x-1) > t; --x);
        printf("Case #%d: %d\n", i+1, x);
    }
    return 0;
}