//  O_o  =>  -_-
//
//  Created by shikhar thakur
//

#include <bits/stdc++.h>

#define ll long long
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define gcd(a,b) __gcd(a,b)
#define fillm(v,val) memset(v,val,sizeof(v))
#define NL "\n"
#define _iosync ios_base::sync_with_stdio(false);cin.tie(0);
const ll mod = 1000000007ll;
const double pi = acos(-1.0);

using namespace std;

ll go(ll n)
{
    if (n == 0)
        return 0;
    ll mark = 0;
    ll tmp;
    ll i = 1;
    while (1)
    {
        tmp = n * i;
        while (tmp > 0)
        {
            mark |= (1 << (tmp % 10));
            tmp /= 10;
        }
        if (mark == ((1 << 10) - 1))
            break;
        i++;
    }
    return (ll)(n * i);
}

int main()
{
#ifdef LOCAL_SYS
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    _iosync
    ll t;
    cin >> t;
    for (ll i = 1; i <= t; i++)
    {
        ll n;
        cin >> n;
        ll ans = go(n);
        cout << "Case #" << i << ": ";
        if (!ans)
        {
            cout << "INSOMNIA\n";
            continue;
        }
        cout << ans << NL;
    }
    return 0;
}