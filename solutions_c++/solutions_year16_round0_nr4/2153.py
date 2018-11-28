#pragma warning(disable:4996)

#include <stdio.h>

int main()
{
    freopen("D-small.in", "r", stdin);
    freopen("D-small.out", "w", stdout);

    int t,tt=0;
    scanf("%d", &t);
    while(t--)
    {
        int k, c, s;
        scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d:", ++tt);
        for (int i=0; i<s; i++)
            printf(" %d", i+1);
        printf("\n");
    }

    return 0;
}
