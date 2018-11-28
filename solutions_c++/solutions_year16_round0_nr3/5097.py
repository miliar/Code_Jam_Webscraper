#include <bits/stdc++.h>

using namespace std;

namespace {

    typedef double real;
    typedef long long ll;

    template<class T> ostream& operator<<(ostream& os, const vector<T>& vs) {
        //if (vs.empty()) return os << "[]";
        os << vs[0];
        for (int i = 1; i < vs.size(); i++) os << " " << vs[i];
        return os;
    }
    template<class T> istream& operator>>(istream& is, vector<T>& vs) {
        for (auto it = vs.begin(); it != vs.end(); it++) is >> *it;
        return is;
    }

    //const int LIM = int(1e4 + 5);
    const int LIM = int(1e8 + 1e3);
    bool isPrime[LIM + 50];
    vector<ll> primes;

    void init() {
        memset(isPrime, 1, sizeof(isPrime));
        isPrime[0] = isPrime[1] = false;
        for (int n = 2; n <= LIM; n++) {
            //if (n % 100 == 0) cerr << n << endl;
            if (not isPrime) continue;
            primes.push_back(n);
            for (int i = n + n; i <= LIM; i += n) {
                isPrime[i] = false;
            }
        }
    }

    int N, J;
    void input() {
        cin >> N >> J;
        //assert(N == 16 && J == 50);
    }

    ll div(ll x) {
        for (int i = 0; i < primes.size(); i++) {
            ll p = primes[i];
            if (p * p > x) return 0;
            if (x % p == 0) return p;
        }
        assert(false);
    }

    void construct(int bit) {
        vector<int> k;
        k.push_back(1);
        for (int i = 0; i < N - 2; i++) {
            if (bit & (1 << i)) {
                k.push_back(1);
            } else {
                k.push_back(0);
            }
        }
        k.push_back(1);
        reverse(k.begin(), k.end());

        //cerr << k << endl;

        vector<ll> xs;
        for (int n = 2; n <= 10; n++) {
            ll x = 0;
            ll base = 1;
            for (int i = 0; i < N; i++) {
                int t = N - i - 1;
                x += base * k[t];
                base *= n;
            }
            ll y = div(x);
            if (y == 0) return;
            xs.push_back(y);
        }

        string k_str;
        for (int i = 0; i < N; i++) {
            k_str.push_back(k[i] + '0');
        }
        cout << k_str << " " << xs << endl;
        J--;
    }

    void solve() {
        for (int bit = 0; J > 0 && bit < (1 << (N - 2)); bit++) {
            construct(bit);
        }
    }
}

int main() {
    init();
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        input();
        cout << "Case #" << t << ": ";
        cout << endl;
        solve();
    }
    return 0;
}

