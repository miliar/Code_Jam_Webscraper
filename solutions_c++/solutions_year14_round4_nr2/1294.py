#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;

int n, T, a[22], b[22], c[22], ans;
bool h[22];

void dfs(int dep)
{
    if (dep == n)
    {
        int flag = 0;
        for (int i = 0; i + 1 < n; i++)
        {
            if (flag == 1)
            {
                if (b[i] < b[i + 1])
                    return;
            }
            if (flag == 0)
            {
                if (b[i] > b[i + 1])
                    flag = 1;
            }
        }
        int num = 0;
        memcpy(c, a, sizeof c);
        for (int i = 0; i < n; i++)
            for (int j = i; j < n; j++)
                if (c[j] == b[i])
                {
                    for (int k = j; k > i; k--)
                    {
                        swap(c[k], c[k - 1]);
                        //if (b[0]==919) cout << c[k-1] << " "<<c[k]<<"\n";
                        num++;
                    }
                    break;
                }
        if (num < ans) ans = num;
        return;
    }
    for (int i = 0; i < n; i++)
        if (!h[i])
        {
            h[i] = true; b[dep] = a[i]; dfs(dep + 1); h[i] = false;
        }
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("bb.out", "w", stdout);
    scanf("%d", &T);
    for (int tt = 0; tt < T; tt++)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        ans = 1000000;
        dfs(0);
        printf("Case #%d: %d\n", tt + 1, ans);
    }
}
