#include <bits/stdc++.h>
#define ll long long
#define ld long double
#define mp make_pair
#define pb push_back
#define ull unsigned ll
#define F first
#define S second
#define y1 sflgdfg

using namespace std;

const ll MIN = 1e3 + 2;
const ll MXN = 1e6 + 3;
const ll INF = 1e9 + 7;
const ll LINF = 1e18 + 15;
const ld EPS = 1e-9;

ll n, x, used[10];

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n;
    for (ll i = 1; i <= n; i++){
        cin >> x;
        cout << "Case #" << i << ": ";
        if (x == 0){
            cout << "INSOMNIA\n";
            continue;
        }
        ll ans = 1;
        memset (used, 0, sizeof(used));
        used[0] = 0;
        ll p = 0;
        ll y = 10;
        while (x * ans <= LINF){
            ll z = x * ans;
            while (z){
                if (!used[z % 10])
                y--;
                used[z % 10] = 1;
                z /= 10;
            }
            if (y <= 0){
                cout << x * ans << "\n";
                p = 1;
                break;
            }
            ans++;
            if (ans == MXN / 100){
                break;
            }
        }
        if (p == 1){
            continue;
        }
        cout << "INSOMNIA\n";
    }
    return 0;
}
