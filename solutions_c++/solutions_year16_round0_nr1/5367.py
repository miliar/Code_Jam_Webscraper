// Copyright 2016 Ricky_Saurav

/*
   Licensed under the "THE BEER-WARE LICENSE" (Revision 42):
   Ricky_Saurav wrote this file. As long as you retain this notice you
   can do whatever you want with this stuff. If we meet some day, and you think
   this stuff is worth it, you can buy me a beer in return.
 */

#include <iostream>
#include <stdio.h>
#include <string>
#include <map>
#include <set>
#include <string.h>
#include <vector>
#include <algorithm>
#include <math.h>
#define NL "\n"
typedef long long ll;
#define fillm(a, val) memset(a, val, sizeof(a))
using namespace std;
const double pi = acos(-1.0);
const ll mod = 1000000007;
const ll maxn = 1000005;
const ll inf = 1ll << 30;
ll maxm = 0;
ll solve(ll n)
{
    ll mark = 0;
    ll cnt = 1;
    while (mark != (1 << 10) - 1)
    {
        ll temp = cnt * n;
        while (temp)
        {
            ll temp1 = (temp % 10);
            temp /= 10;
            mark |= (1 << temp1);
        }
        cnt++;
    }
    cnt--;
    return cnt * n;
}
int main()
{
#ifdef LOCAL_SYS
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        ll n;
        cin >> n;
        if (n == 0)
        {
            cout << "Case #" << i << ": INSOMNIA\n";
            continue;
        }
        ll ans = solve(n);
        cout << "Case #" << i << ": " << ans << NL;
    }
    return 0;
}
