#include <iostream>
#include <cstdio>

using namespace std;

int a[200][200];
int n, m;

void Check()
{
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
        {
            bool find = false;
            for (int k = 0; k < n; k++)
                if (a[k][j] > a[i][j])
                {
                    find = true;
                    break;
                }

            if (!find)
                continue;

            find = false;
            for (int k = 0; k < m; k++)
                if (a[i][k] > a[i][j])
                {
                    find = true;
                    break;
                }

            if (!find)
                continue;
            else
            {
                printf("NO\n");
                return;
            }
        }

    printf("YES\n");
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        scanf("%d %d", &n, &m);
        for (int j = 0; j < n; j++)
            for (int k = 0; k < m; k++)
                scanf("%d", &a[j][k]);
        printf("Case #%d: ", i + 1);
        Check();
    }



    return 0;
}
