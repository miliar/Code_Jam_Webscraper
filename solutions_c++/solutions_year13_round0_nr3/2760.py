#include <stdio.h>

int p(int x)
{
    int y = x;
    int z = 0;
    while (y) {
        z = z * 10 + y % 10;
        y /= 10;
    }
    if (z == x) return 1;
    return 0;
}

int is[1024];
int main()
{
    int t, a, b;
    scanf("%d", &t);
    for (int i = 1; i*i <= 1000; i++) {
        if (p(i) && p(i*i)) {
            is[i*i] = 1;
        }
    }
    for (int i = 1; i <= t; i++) {
        scanf("%d%d", &a, &b);
        int res = 0;
        for (; a <= b; a++) {
            if (is[a]) res++;
        }
        printf("Case #%d: %d\n", i, res);
    }

    return 0;
}
