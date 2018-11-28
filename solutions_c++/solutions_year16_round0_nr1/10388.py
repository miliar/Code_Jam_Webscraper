#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int mask = 0;
void process(ll x)
{
    while (x)
    {
        mask |= (1 << (x % 10));
        x /= 10;
    }
}

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int test = 1; test <= t; test++)
    {
        printf("Case #%d: ", test);
        ll n;
        scanf("%lld", &n);
        if (n == 0)
        {
            puts("INSOMNIA");
            continue;
        }
        mask = 0;
        ll cur = n;
        process(cur);
        while (mask != (1 << 10) - 1)
        {
            cur += n;
            process(cur);
        }
        printf("%lld\n", cur);
    }
}
