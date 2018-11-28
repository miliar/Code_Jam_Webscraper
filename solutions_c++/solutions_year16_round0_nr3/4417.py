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
ll n, cnt;

ll prime(ll num)
{
    for (ll i = 2; i <= sqrt(num); i++)
        if (num % i == 0)
            return i;
    return 0;
}

ll to_base(ll msk, ll j)
{
    ll val = 0;
    ll power = 1;
    for (ll i = 0; i < n; i++)
    {
        if (msk & 1 << i)
        {
            val += power;
        }
        power *= j;
    }
    return val;
}

void solve(ll msk, ll j)
{
    vector<ll> v;
    for (ll bas = 2; bas <= j; bas++)
    {
        ll num = to_base(msk, bas);
        if (!prime(num))
        {
            return;
        }
        v.pb(prime(num));
    }
    cnt++;
    bitset<16>b(msk);
    string ans = b.to_string();
    ans.erase(0, ans.find_first_not_of('0'));
    cout << ans << " ";
    for (ll i = 0; i < v.size(); i++)
        cout << v[i] << " ";
    cout << NL;
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
    for (ll tc = 1; tc <= t; tc++)
    {
        cout << "Case #" << tc << ":";
        cout << NL;
        ll j;
        cin >> n >> j;
        cnt = 0;
        for (ll i = 0; i < (1 << n); i++)
        {
            if (cnt == j)
                break;
            if (i & 1)
            {
                if (i & 1 << (n - 1))
                {
                    solve(i, 10);
                }
            }
        }
    }
    return 0;
}