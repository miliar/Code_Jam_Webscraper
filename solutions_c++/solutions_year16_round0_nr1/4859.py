#include <iostream>
#include <bitset>

using namespace std;
using ll = long long;
#define FOR(i,a,b) for(ll i=(a); i<(b); ++i)

int main() {
    ll T; cin >> T;
    FOR(t,0,T) {
        cout << "Case #" << t+1 << ": ";
        ll N; cin >> N;
        ll cur = 0;
        if(N) {
            bitset<10> seen;
            while(!seen.all()) {
                cur += N;
                for(char c : to_string(cur))
                    seen[c-'0'] = true;
            }
        }
        if(cur)
            cout << cur << endl;
        else
            cout << "INSOMNIA" << endl;
    }
}
