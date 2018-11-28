#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define N 1005
char a[N];
int n;

bool check()
{
    int tot = a[0];
    for (int i = 1; i < n; ++i)
        if (tot >= i)
            tot +=a[i];
        else
            return 0;
    return 1;
}

int solve()
{
    scanf("%d%s", &n, a);
    ++n;
    for (int i = 0; i < n; ++i)
    {
        a[i] -= '0';
    }
    if (check())
        return 0;
    for (int ans = 1; ans <= n; ++ans)
    {
        for (int i = 0; i < 1; ++i)
        {
            a[i] += ans;
            if (check())
                return ans;
            a[i] -= ans;
        }
    }
}

int main()
{
    int t;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt)
    {
        printf("Case #%d: ", tt);
        printf("%d\n", solve());
    }
    return 0;
}