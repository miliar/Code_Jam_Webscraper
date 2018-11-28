#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll n, ans;
set<int> s;

void add(ll a) {
    while (a) {
        s.insert(a % 10);
        a /= 10;
    }
}

int main(void) {
    if (fopen("a-small.in", "r")) {
        freopen("a-small.in", "r", stdin);
        freopen("a-small.out", "w", stdout);
    }
    if (fopen("a-large.in", "r")) {
        freopen("a-large.in", "r", stdin);
        freopen("a-large.out", "w", stdout);
    }
    int t;
    cin >> t;
    for (int ii = 1; ii <= t; ii++) {
        cin >> n;
        s.clear();
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", ii);
            continue;
        }
        for (ans = n; s.size() < 10; ans += n) add(ans);
        ans -= n;
        printf("Case #%d: %lld\n", ii, ans);
    }
    return 0;
}
