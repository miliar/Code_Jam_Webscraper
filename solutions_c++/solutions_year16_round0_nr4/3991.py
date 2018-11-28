#include <bits/stdc++.h>

using namespace std;

namespace {

    typedef double real;
    typedef unsigned long long ll;

    template<class T> ostream& operator<<(ostream& os, const vector<T>& vs) {
        os << vs[0];
        for (int i = 1; i < vs.size(); i++) os << " " << vs[i];
        return os;
    }
    template<class T> istream& operator>>(istream& is, vector<T>& vs) {
        for (auto it = vs.begin(); it != vs.end(); it++) is >> *it;
        return is;
    }

    ll K, C, S;
    void input() {
        cin >> K >> C >> S;
    }

    void solve() {
        ll X = 1;
        for (int i = 0; i < C - 1; i++) X *= K;
        vector<ll> ans;
        for (ll i = 0; i < K; i++) {
            ans.push_back(i * X + 1);
        }
        cout << ans << endl;
    }
}

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        input();
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}

