#include <bits/stdc++.h>

using namespace std;

namespace {

    typedef double real;
    typedef long long ll;

    int __bultin_popcount(int bit) {
        int c = 0;
        for (int i = 0; i < 32; i++) {
            if (bit & (1 << i)) c++;
        }
        return c;
    }

    template<class T> ostream& operator<<(ostream& os, const vector<T>& vs) {
        if (vs.empty()) return os << "[]";
        os << "[" << vs[0];
        for (int i = 1; i < vs.size(); i++) os << " " << vs[i];
        return os << "]";
    }
    template<class T> istream& operator>>(istream& is, vector<T>& vs) {
        for (auto it = vs.begin(); it != vs.end(); it++) is >> *it;
        return is;
    }

    int N, K;
    vector<real> P;
    void input() {
        cin >> N >> K;
        P.clear(); P.resize(N); cin >> P;
    }

    real tie_prob(vector<real>& ps) {
        real ret = 0;
        for (int bit = 0; bit < (1 << K); bit++) {
            if (__bultin_popcount(bit) != K / 2) continue;
            real c = 1.0;
            for (int i = 0; i < K; i++) {
                real p = (bit & (1 << i)) ? ps[i] : 1 - ps[i];
                c *= p;
            }
            ret += c;
        }
        return ret;
    }

    void solve() {
        real ans = 0;
        for (int i = 0; i < (1 << N); i++) {
            int bit = i;
            if (__bultin_popcount(bit) == K) {
                vector<real> p;
                for (int j = 0; j < N; j++) {
                    if (bit & (1 << j)) {
                        p.push_back(P[j]);
                    }
                }
                ans = max(ans, tie_prob(p));
            }
        }
        cout << fixed << setprecision(12) << ans << endl;
    }
}

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        cerr << t << endl;
        input();
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}

