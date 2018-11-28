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

vector <int> a;

ll isPrime(ll x) {
    if (x < 2) return -1;
    for (ll i = 2; i <= sqrt(x); i++)
        if (x % i == 0) return i;
    return -1;
}

int n, J, nt;

int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    cin >> nt;
    cout << "Case #1:\n";
    cin >> n >> J;
    int M = (1 << (n - 2));
    int cnt = 0;
    for (int i = 0; i < M; i++) {

        bool ok = true;
        a.clear();
        for (int k = 2; k <= 10; k++) {
            ll sum = 1;
            for (int j = 0; j < n - 2; j++) {
                int d = ((i >> j) & 1);
                sum = sum * k + d;
            }
            sum = sum * k + 1;
            int get = isPrime(sum);
            if (get == -1) {
                ok = false;
                break;
            }
            else {
                a.pb(get);
            }
        }

        if (ok) {
            cout << 1;
            for (int j = 0; j < n - 2; j++)
                cout << ((i >> j) & 1);
            cout << "1 ";
            for (int j = 0; j < a.size(); j++)
                cout << a[j] << " " ;
            cout << "\n";
            cnt++;
            if (cnt == J) break;
        }
    }
    /**/return 0;
}
