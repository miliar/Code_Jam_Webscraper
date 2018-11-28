#include<stdio.h>

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out_A.txt", "w", stdout);

    int T, r, t, x, y;
    scanf("%d", &T);
    for(x = 1; x <= T; x++) {
        scanf("%d %d", &r, &t);
        for(y = 1; (2*(r+y)-1)*y <= t; y++);
        printf("Case #%d: %d\n", x, y-1);
    }
    return 0;
}
