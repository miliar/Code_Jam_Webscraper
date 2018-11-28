#include <stdio.h>
#include <cstdlib>
#include <string.h>

const int n = 4;

using namespace std;

int a[n][n], b[n][n];
int v[20];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int qw = 0; qw < t; ++qw)
    {
        int k1, k2;
        scanf("%d", &k1);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                scanf("%d", &a[i][j]);
        scanf("%d", &k2);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                scanf("%d", &b[i][j]);
        memset(v, 0, sizeof v);
        for (int i = 0; i < n; ++i)
        {
            v[a[k1 - 1][i]]++;
            v[b[k2 - 1][i]]++;
        }
        int ans = -1;
        for (int i = 0; i < 20; ++i)
            if (v[i] == 2)
            {
                if (ans == -1)
                    ans = i;
                else
                    ans = -2;
            }
        if (ans == -2)
            printf("Case #%d: Bad magician!\n", qw + 1);
        else if (ans == -1)
            printf("Case #%d: Volunteer cheated!\n", qw + 1);
        else
            printf("Case #%d: %d\n", qw + 1, ans);
    }
}
