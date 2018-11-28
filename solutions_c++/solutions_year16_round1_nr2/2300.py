#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int c[2520];

int main()
{
    int test, temp, max, n;
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    scanf("%d", &test);
    for (int t = 1; t <= test; t++)
    {
        scanf("%d", &n);
        memset(c, 0, 2520);
        max = 0;
        for (int i = 0; i < 2*n-1; i++)
        {
            for (int j = 0; j < n; j++)
            {
                scanf("%d", &temp);
                c[temp]++;
                if (temp > max)
                    max = temp;
            }
        }
        printf("Case #%d: ", t);
        for (int i = 1; i <= max; i++)
        {
            if (c[i]%2 != 0)
                printf("%d ", i);
        }
        printf("\n");
    }
    return 0;
}
