#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ll;

string asBinary(ll x, ll n = 0) {
    string s;
    while (x != 0) {
        s += x % 2 + '0';
        x /= 2;
    }

    while ((ll)s.length() < n)
        s += '0';

    reverse(s.begin(), s.end());
    return s;
}

ll getFirstDel(ll x) {
    for (ll i = 2; i * i <= x; ++i) {
        if (x % i == 0)
            return i;
    }

    return 1;
}

ll reinterpretNumber(ll x, ll base) {
    string b = asBinary(x);
    //reverse(b.begin(), b.end());

    ll ans = 0;
    for (ll i = 0; i < (ll)b.length(); ++i) {
        ans = ans * base + b[i] - '0';
    }

    return ans;
}

bool getDel(ll x, ll * d) {
    for (ll i = 10; i >= 2; --i) {
        ll n = reinterpretNumber(x, i);

        d[i] = getFirstDel(n);
        if (d[i] == 1)
            return false;
    }

    return true;
}

void solve (ll n, ll k) {
    for (ll i = ((ll)1 << (n - 1)) + 1; i < (ll)1 << n && k != 0; i += 2) {
        ll d[11];
        memset(d, 0, sizeof(d));
        bool is_good = getDel(i, d);

        if (is_good) {
            cout << asBinary(i, n) << " ";
            for (ll j = 2; j <= 10; ++j) {
                cout << d[j] << " ";
            }

            cout << "\n";
            --k;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    freopen("C-small-attempt1.in", "r", stdin);
    //freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ll t;
    cin >> t;

    for (ll i = 1; i <= t; ++i) {
        ll n, j;
        cin >> n >> j;

        cout << "Case #1:\n";
        solve(n, j);
    }

    return 0;
}
