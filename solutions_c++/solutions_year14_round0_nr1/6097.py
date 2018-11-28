#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

const int maxn = 5;
int x, y, ans, cnt;
int a[maxn][maxn], b[maxn][maxn];

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T, cas = 1;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d", &x);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                scanf("%d", &a[i][j]);
        scanf("%d", &y);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                scanf("%d", &b[i][j]);
        cnt = 0;
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                if (a[x][i] == b[y][j])
                {
                    cnt++;
                    ans = a[x][i];
                }
        printf("Case #%d: ", cas++);
        if (cnt == 0) puts("Volunteer cheated!");
        else if (cnt > 1) puts("Bad magician!");
        else printf("%d\n", ans);
    }
    return 0;
}
