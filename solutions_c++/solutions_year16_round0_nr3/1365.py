
#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for (int i = 0; i < int(n); i++)
#define rep1(i,n) for (int i = 1; i <= int(n); i++)
#define var(x) #x " = " << x
#define show(x) cout << var(x) << endl;
#define all(c) (c).begin(), (c).end()

typedef long long ll;

ll ex(ll p, int k) {
    ll r = 1;
    rep (i,k) r *= p;
    return r;
}

int main() {
    int T;
    cin >> T;
    cout << "Case #1:" << endl;
    int N, J;
    cin >> N >> J;
    // 32 500
    
    for (int n = 1; n <= J; n++) {
        int _n = 2*n-1, d[16] = {}, i = 0;
        while (_n > 0) {
            d[i] = _n % 2;
            _n /= 2;
            i++;
        }
        d[N/2-1] = 1;

        rep (i,N/2) cout << d[N/2-1-i];
        rep (i,N/2) cout << d[N/2-1-i];
        for (int k = 2; k <= 10; k++) cout << " " << ex(k,N/2)+1;
        cout << endl;
    }
}
