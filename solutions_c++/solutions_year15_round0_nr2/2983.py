#include <iostream>
#include <queue>
#include <limits>
using ll = long long;
using namespace std;
#define FOR(i,a,b) for(ll i=(a); i<(b); ++i)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll T; cin >> T;
    FOR(t,0,T) {
        ll D; cin >> D;
        vector<ll> ds;
        FOR(i,0,D) {
            ll Pi;
            cin >> Pi;
            ds.push_back(Pi);
        }
        ll opt = numeric_limits<ll>::max();
        FOR(ps,1,1100) {
            ll breaks = 0;
            for(const auto &x : ds) {
                breaks += (x+ps-1)/ps - 1;
            }
            opt = min(opt, breaks + ps);
        }
        cout << "Case #" << t+1 << ": " << opt << endl;
    }
}

