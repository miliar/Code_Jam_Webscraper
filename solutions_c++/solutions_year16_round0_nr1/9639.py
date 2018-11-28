#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll solve(ll n) {
    if (n == 0) return -1;
    set <int> s;
    for (ll x = n; ; x += n) {
        if (x < 0) return -1;
        ll tmp = x;
        while (tmp > 0) {
            s.insert(tmp % 10);
            tmp /= 10;
        }
        if (s.size() == 10)
            return x;
    }
}

int main() {
    //freopen("input.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int nTests;
    scanf("%d", &nTests);
    for (int t = 1; t <= nTests; ++t) {
        int n;
        scanf("%d", &n);

        ll res = solve(n);
        printf("Case #%d: ", t);
        if (res < 0) puts("INSOMNIA");
        else cout << res << endl;
    }
}
