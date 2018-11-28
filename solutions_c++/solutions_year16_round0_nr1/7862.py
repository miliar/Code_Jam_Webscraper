#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll f(ll x) {
    unordered_set<int> st;
    for (int i = 1; i <= 100; ++i) {
        ll t = x * i;
        while (t) {
            st.insert(t % 10);
            t /= 10;
        }
        if (st.size() == 10) {
            return x * i;
        }
    }
    return -1;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        ll x;
        cin >> x;
        cout << "Case #" << i << ": ";
        if (x == 0) {
            cout << "INSOMNIA\n";
        } else {
            cout << f(x) << "\n";
        }
    }
    return 0;
}
