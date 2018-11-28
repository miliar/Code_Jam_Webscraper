#include <bits/stdc++.h>

using namespace std;

typedef long long  ll;

ll Solve(ll n)
{
    int cnt = 0;
    vector<bool> digit(10, false);
    ll mul = n;

    while (true) {
        ll tmp = mul;
        while (tmp) {
            if (!digit[tmp % 10]) {
                digit[tmp % 10] = true;
                ++cnt;
            }
            tmp /= 10;
        }

        if (cnt == 10)
            return mul;
        mul += n;
    }
}

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);

    int t;
    ll n;

    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n;
        cout << "Case #" << i << ": ";
        if (n == 0)
            cout << "INSOMNIA\n";
        else
            cout << Solve(n) << '\n';
    }

    return 0;
}
