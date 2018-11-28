/*
ID: tju_hac1
PROG:
LANG: C++
*/
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int a[4][4], b[4][4];
bool f[17];
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T, n, i, m, ca = 1, j;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d", &n);
        for (i = 0;i < 4;i++)
            for (j = 0;j < 4;j++)
                scanf("%d", &a[i][j]);
        scanf("%d", &m);
        for (i = 0;i < 4;i++)
            for (j = 0;j < 4;j++)
                scanf("%d", &b[i][j]);
        int cnt = 0;
        memset(f, 0, sizeof(f));
        for (i = 0;i < 4;i++)
            f[b[m-1][i]] = true;
        int ans;
        for (i = 0;i < 4;i++)
            if (f[a[n-1][i]]) cnt++, ans = a[n-1][i];
        printf("Case #%d: ", ca++);
        if (cnt == 0) puts("Volunteer cheated!");
        else if (cnt > 1) puts("Bad magician!");
        else printf("%d\n", ans);
    }
    return 0;
}
