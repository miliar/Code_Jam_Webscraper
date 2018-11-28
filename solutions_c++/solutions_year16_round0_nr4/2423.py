#include<cstdio>

int main()
{
    int Case;
    scanf("%d", &Case);

    for (int t = 1; t <= Case; t++)
    {
        int k, c, s;
        scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d:", t);
        for (int i = 1; i <= k; i++)
            printf(" %d", i);
        putchar('\n');
    }

    return 0;
}