#include <iostream>
using ll = long long;
using namespace std;
#define FOR(i,a,b) for(ll i=(a); i<(b); ++i)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll T; cin >> T;
    FOR(t,0,T) {
        ll smax; cin >> smax;
        ll acc = 0, needed = 0;
        FOR(i,0,smax+1) {
            char x; cin >> x;
            x -= '0';
            ll add = max(0ll,i-acc);
            needed += add;
            acc += add;
            acc += x;
        }
        cout << "Case #" << t+1 << ": " << needed << endl;
    }
}

