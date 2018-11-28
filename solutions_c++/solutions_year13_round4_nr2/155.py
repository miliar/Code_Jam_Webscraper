#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long llong;

void solve(int cs)
{
    int n;
    llong p;
    scanf("%d %lld", &n, &p);
    llong ans1, ans2;
    if (p == (1LL << n))
        ans1 = ans2 = (1LL << n) - 1;
    else
    {
        //mxw
        p = (1LL << n) - p;
        int mxw = 0;
        for (int i = 0; i < 60; i++)
            if ((p >> i) & 1)
                mxw = i;
        ans1 = (1LL << (n - mxw)) - 2;

        //mn
        p = (1LL << n) - p;
        llong mn = 1e18;
        for (int i = 0; i < 60; i++)
            if ((p >> i) & 1)
                mn = (1LL << (n - i)) - 1;
        ans2 = (1LL << n) - mn - 1;
    }
    printf("Case #%d: %lld %lld\n", cs, ans1, ans2);
}

int main()
{
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
        solve(i + 1);
}
