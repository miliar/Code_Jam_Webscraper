#include <cstdio>
#include <cstring>

using namespace std;

int T, n, m;
int a[222][222];

bool checkvert(int x, int y)
{
    for (int i = 0; i < n; ++i)
        if (a[i][y] > a[x][y])
            return false;
    return true;
}

bool checkhori(int x, int y)
{
    for (int j = 0; j < m; ++j)
        if (a[x][j] > a[x][y])
            return false;
    return true;
}

bool checkpoint(int x, int y)
{
    return checkvert(x, y) || checkhori(x, y);
}

bool check()
{
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (!checkpoint(i, j))
                return false;
    return true;
}

int main()
{
    freopen("b.txt", "r", stdin);
    freopen("b-out.txt", "w", stdout);

    scanf("%d", &T);
    for (int CS = 1; CS <= T; ++CS)
    {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                scanf("%d", &a[i][j]);
        if (check())
            printf("Case #%d: YES\n", CS);
        else
            printf("Case #%d: NO\n", CS);
    }
    return 0;
}
