#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

int check(ll x) {
    int k = 0;
    while (x > 0) {
        k |= (1 << (x%10));
        x /= 10;
    }
    return k;
}

int main() {
    int t;
    cin >> t;
    int cas = 1;
    while (t--) {
        cout << "Case #" << cas << ": ";
        ++cas;
        ll n;
        cin >> n;
        if (n == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        int k = check(n);
        ll tt = n;
        while (k < ((1<<(10)) - 1)) {
            tt += n;
            k |= check(tt);
        }
        cout << tt << endl;
    }
}