#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;
const int maxn = 11;
int dat[maxn][maxn], n, m, label[maxn][maxn];
void fuck()
{
    memset(label, 0, sizeof(int)*maxn * maxn);
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            scanf("%d", &dat[i][j]);
    for (int i = 0; i < n; i++)
    {
        bool flag = 1;
        for (int j = 0; j < m; j++)
            if (dat[i][j] == 2)
                flag = 0;
        if (flag)
            for (int j = 0; j < m; j++)
                label[i][j] = 1;
    }
    for (int i = 0; i < m; i++)
    {
        bool flag = 1;
        for (int j = 0; j < n; j++)
            if (dat[j][i] == 2)
                flag = 0;
        if (flag)
            for (int j = 0; j < n; j++)
                label[j][i] = 1;
    }
    bool flag = 1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            if (dat[i][j] == 1 && !label[i][j])
                flag = 0;
    }
    printf("%s\n", flag ? "YES" : "NO");
}
int main(int argc, char const *argv[])
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++)
        printf("Case #%d: ", i), fuck();
    return 0;
}
