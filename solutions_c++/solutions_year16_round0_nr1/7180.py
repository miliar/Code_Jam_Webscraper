// Yerzhan Gapurinov

#include <bits/stdc++.h>
#define ull unsigned ll
#define mp make_pair
#define F first
#define S second
#define ll long long
#define yerzhan gapurinov
#define ld long double
#define pb push_back
#define pll pair<ll, ll>
#define pii pair <int, int>
#define all(v) (v.begin(), v.end())


using namespace std;

const int INF = 1e9 + 7;
const int MXN = 1e6 + 7 ;
const double EPS = 1e-9;
const double PI = acos(-1);

ll n, x;;
ll a[MXN], b[MXN];

set <int> S;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
   //freopen("modern-art.in", "r", stdin);
   // freopen("modern-art.out", "w", stdout);
    cin >> n;
    for(int i = 1; i <= n; i++) {
        cin >> x;
        cout << "Case #" << i << ": ";
        if(x == 0) {
            cout << "INSOMNIA\n";
        } else {
            ll j = 1, m = x;
            S.clear();
            while(S.size() != 10){
                while(m != 0) {
                    S.insert(m % 10);
                    m /= 10;
                }
                if(S.size() < 10) {
                 j++;
                 m = x * j;
                }
            }
            cout << x * j << endl;
        }
    }

    return 0;
}
