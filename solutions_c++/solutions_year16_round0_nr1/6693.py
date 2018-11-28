#include <bits/stdc++.h>
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define ll long long
#define mod 1000000007

using namespace std;

ll n, t;

int main()
{
    //freopen(".in", "r", stdin);
    freopen("A.out", "w", stdout);
    //ios_base::sync_with_stdio(0);
    cin.tie();
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> n;
        ll x = n, c = 0;
        while(x) c |= 1 << (x % 10), x /= 10;
        for (ll j = 2; j <= 1e6; j++) {
            x = j * n;
            while(x) c |= 1 << (x % 10), x /= 10;
            if (c == (1 << 10) - 1) {
                cout << "Case #" << i << ": " << j * n << endl;
                break;
            }
        }
        if (c != (1 << 10) - 1)
            cout << "Case #" << i << ": INSOMNIA" << endl;
    }
    return 0;
}
