#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ll;
const ll N = 32;
ll rem[11][11][35];
int32_t main() {
    ll n = N, cnt = 500;
    cout << "Case #1:\n";
    for (ll i = 2; i <= 10; i++) {
        for (auto k : {2, 3, 5, 7}) {
            rem[i][k][0] = 1;
            for (ll j = 1; j < 34; j++)
                rem[i][k][j] = (rem[i][k][j-1] * i) % k;
        }
    }
    
    for (ll i = 0; cnt; i++) {
        ll x = i*2 + 1 + (1ll<<(n-1));
        ll r[20][20] = {};
        for (ll k = 0; k < N; k++) if(x >> k & 1ll) {
            for(ll u = 2; u <= 10; u++)
                for (auto l : {2, 3, 5, 7})
                    r[u][l] += (rem[u][l][k]);
        }
        ll bl[20] = {}, kol = 0;
        for (ll j = 2; j <= 10; j++) {
            for (auto l : {2, 3, 5, 7})
                if (r[j][l] % l == 0) {
                    kol++;
                    bl[j] = l;
                    break;
                }
        }
        if (kol == 9) {
            cnt--;
            cout << bitset<N>(x) << ' ';
            for (ll p = 2; p <= 10; p++)
                cout << bl[p] <<' ';
            cout << endl;
        }
    }
}
/*for (ll j = 2; j <= 10; j++) {
 ll ans = 0;
 for (ll k = 0; k < n; k++) if(x >> k & 1){
 ans += (pow(j, k));
 }
 if (ans % 2 != 0 && ans % 3 != 0 && ans % 7 != 0 && ans % 5 != 0) {
 bul = 0;
 //break;
 }
 cerr << j << ' ' << ans << ' '<< ans % 3 << ' ' << ans % 2 << ' ' << ans % 7<< endl;
 }
 if(bul) {
 an ++;
 }
 }
 cerr << an << endl;
 }*/