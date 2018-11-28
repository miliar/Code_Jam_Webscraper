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

ll to_base(ll x, int b)
{
    vector<int> bin;
    while (x > 0)
    {
        bin.push_back(x % 10);
        x /= 10;
    }
    reverse(bin.begin(), bin.end());
    ll res = 0;
    for (int e : bin)
        res = res * b + e;
    return res;
}

ll get_prime(ll x)
{
    for (ll i = 2; i * i <= x; i++)
        if (x % i == 0)
            return i;
    return -1;
}

vector<ll> is_jamcoin(ll x)
{
    vector<ll> cert;
    cert.push_back(x);
    for (int i = 2; i <= 10; i++)
    {
        ll p = get_prime(to_base(x, i));
        if (p == -1)
            return {};
        cert.push_back(p);
    }
    return cert;
}

void solve()
{
    int n, cnt;
    scanf("%d%d", &n, &cnt);

    vector<vector<ll>> res;
    for (int mask = 0; mask < (1 << (n - 2)) && (int)res.size() < cnt; mask++)
    {
        ll x = 1;
        for (int i = 0; i < n - 2; i++)
            x = 10 * x + !!(mask & (1 << i));
        x = 10 * x + 1;
        auto cert = is_jamcoin(x);
        if (!cert.empty())
            res.push_back(cert);
    }

    assert((int)res.size() >= cnt);
    for (int i = 0; i < cnt; i++)
    {
        auto vec = res[i];
        for (ll e : vec)
            printf("%lld ", e);
        printf("\n");
    }
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
        printf("Case #%d:\n", i + 1);
        solve();
    }

    eprintf("time = %.3lf\n", (double)clock() / CLOCKS_PER_SEC);

    return 0;
}
