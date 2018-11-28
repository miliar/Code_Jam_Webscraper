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

void solve()
{
    ll k, c, s;
    scanf("%lld%lld%lld", &k, &c, &s);
    assert(s == k);

    ll step = 1;
    for (int i = 0; i < c - 1; i++)
        step *= k;
    ll len = step * k;

    for (ll i = 1; i <= len; i += step)
        printf("%lld ", i);
    printf("\n");
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
