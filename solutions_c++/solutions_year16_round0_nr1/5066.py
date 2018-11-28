#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define pp pair<ll, int>
#define fi first
#define se second
#define esp 1e-12
#define inf 1000000001
#define N 400000
typedef long long ll;
using namespace std;
int nt;
int n;
ll state, base;

bool Set(ll x) {
    while (x > 0) {
       state = state | (1 << (x % 10));
       x /= 10;
    }
    return (state == base);
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    base = ((ll) 1 << 10) - 1;
    cin >> nt;
    for (int kk = 1; kk <= nt; kk++) {
        cin >> n;
        state = 0;
        int ret = -1;
        bool ok = false;
        for (int i = 1; i <= 999; i++) {
            ok = Set(i * n);
            if (ok) {
                    ret = i;
                    break;
            }
        }
        cout << "Case #" << kk << ": ";
        if (ok == false)
            cout << "INSOMNIA\n";
        else
            cout << (ret * n) << "\n";
    }
    /**/return 0;
}
