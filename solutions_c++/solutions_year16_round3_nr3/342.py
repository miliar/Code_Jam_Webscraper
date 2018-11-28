#include <iostream>
#include <cstdio>

using namespace std;

int a[5111], b[5111], timeA[5111], timeB[5111];

int main()
{
    int n, m, k;
    scanf("%d%d%d", &n, &m, &k);

    for (int i = 0; i < k; i++)
    {
        int type, x, color;
        scanf("%d%d%d", &type, &x, &color);

        if (type == 1)
        {
            a[x] = color;
            timeA[x] = i + 1;
        }
        else
        {
            b[x] = color;
            timeB[x] = i + 1;
        }
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            int x = 0;
            if (timeA[i] > timeB[j]) x = a[i];
            else x = b[j];

            printf("%d ", x);
        }
        printf("\n");
    }
}
