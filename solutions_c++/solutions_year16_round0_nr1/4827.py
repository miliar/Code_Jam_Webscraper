#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll getMsk(ll x) {
    ll ans = 0;

    while (x != 0) {
        ll digit = x % 10;
        x /= 10;

        ans |= 1 << digit;
    }

    return ans;
}

ll getAns(ll x) {
    if (x == 0) {
        return 0;
    }


    ll msk = 0;

    ll k = 0;
    while (msk != 1023) {
        ++k;
        msk |= getMsk(x * k);
    }

    return k * x;
}

int main()
{
    ios::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ll t;
    cin >> t;

    for (ll i = 1; i <= t; ++i) {
        ll x;
        cin >> x;

        ll ans = getAns(x);
        if (ans != 0)
            cout << "Case #" << i << ": " << ans << "\n";
        else
            cout << "Case #" << i << ": " << "INSOMNIA" << "\n";
    }

    return 0;
}
