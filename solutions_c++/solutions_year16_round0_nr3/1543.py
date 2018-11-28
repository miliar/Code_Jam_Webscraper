#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

set<string> s;

ll ret(ll v, int b) {
    ll ret = 0, p = 1;
    while (v) {
        ret += (v % 10) * p;
        p *= b;
        v /= 10;
    }
    return ret;
}

int main(void) {
    //if (fopen("c-small.in", "r")) {
     //   freopen("c-small.in", "r", stdin);
      //  freopen("c-small.out", "w", stdout);
    //}
    if (fopen("c-large.in", "r")) {
        freopen("c-large.in", "r", stdin);
        freopen("c-large.out", "w", stdout);
    }
    int n, num;
    cin >> n;
    cin >> n >> num;
    int k = n / 2;
    cout << "Case #1:\n";
    for (ll ii = 0; s.size() < num; ii++) {
        ll ex = 0, p = 1;
        string c = "";
        for (int i = 0; i < k; i++) {
            if (ii & (1 << i)) ex += p;
            p *= 10;
        }
        for (int i = k - 1; i >= 0; i--) {
            if (ii & (1 << i)) c += "1";
            else c += "0";
        }
        if ((ii & 1) > 0 && (ii & (1 << (k - 1))) > 0) {
            c += c;
            if (s.insert(c).second) {
                cout << c;
                for (int j = 2; j <= 10; j++) cout << " " << ret(ex, j);
                cout << "\n";
            }
        }
    }
    return 0;
}
