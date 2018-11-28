#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <cassert>
using namespace std;

#ifdef LOCAL
    #define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
    #define eprintf(...) 0
#endif

typedef long long ll;

bool all(bool used[])
{
    for (int i = 0; i < 10; i++)
        if (!used[i])
            return false;
    return true;
}

ll solve(ll n)
{
    bool used[10] = {};
    int k;
    for (k = 1; !all(used); k++)
    {
        ll x = n * k;
        while (x > 0)
        {
            used[x % 10] = true;
            x /= 10;
        }
    }
    return n * (k - 1);
}

void solve()
{
    int n;
    scanf("%d", &n);
    if (n == 0)
        puts("INSOMNIA");
    else
        printf("%lld\n", solve(n));
}

int main()
{
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d: ", i + 1);
        solve();
    }

    eprintf("time = %.3lf\n", (double)clock() / CLOCKS_PER_SEC);

    return 0;
}
