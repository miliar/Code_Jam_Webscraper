#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

double ans = 0, f[200], p[200];
int n, k;

double calc(int x, int t, double now)
{
    if (x > k) {
        return t != 0 ? 0 : now;
    }
    if (t + (k - x + 1) < 0 || t - (k - x + 1) > 0)
        return 0;
    return calc(x + 1, t + 1, now * f[x]) + calc(x + 1, t - 1, now * (1 - f[x]));
}

void dfs(int x, int t)
{
    if (t == k) {
        ans = max(ans, calc(1, 0, 1.0));
        return;
    }
    if (x > n) {
        return;
    }
    dfs(x + 1, t);
    f[t + 1] = p[x];
    dfs(x + 1, t + 1);
}

void work()
{
    scanf("%d%d", &n, &k);
    for (int i = 1; i <= n; i++)  {
        scanf("%lf", &p[i]);
    }
    ans = 0;
    dfs(1, 0);
    printf("%lf\n", ans);
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        work();
    }
}

