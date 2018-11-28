#include <iostream>
#include <string>
#include <vector>

using namespace std;

enum class V { ONE, I, J, K };
struct Q {
    int sgn;
    V val;

    Q(): sgn(1), val(V::ONE) {}
    Q(int sgn, V val): sgn(sgn), val(val) {}

    bool operator==(const Q& x) const {
        return sgn == x.sgn && val == x.val;
    }
};

Q mul(Q a, Q b) {
    Q r;
    r.sgn = a.sgn * b.sgn;

    if (a.val == V::ONE) {
        r.val = b.val;
    } else if (b.val == V::ONE) {
        r.val = a.val;
    } else if (a.val == V::I && b.val == V::I) {
        r.sgn *= -1;
    } else if (a.val == V::I && b.val == V::J) {
        r.val = V::K;
    } else if (a.val == V::I && b.val == V::K) {
        r.val = V::J;
        r.sgn *= -1;
    } else if (a.val == V::J && b.val == V::I) {
        r.val = V::K;
        r.sgn *= -1;
    } else if (a.val == V::J && b.val == V::J) {
        r.sgn *= -1;
    } else if (a.val == V::J && b.val == V::K) {
        r.val = V::I;
    } else if (a.val == V::K && b.val == V::I) {
        r.val = V::J;
    } else if (a.val == V::K && b.val == V::J) {
        r.val = V::I;
        r.sgn *= -1;
    } else if (a.val == V::K && b.val == V::K) {
        r.sgn *= -1;
    }
    
    return r;
}

Q pow (Q a, int64_t k) {
    Q r;
    while (k) {
        if (k & 1) r = mul(r, a);
        a = mul(a, a);
        k >>= 1;
    } 
    return r;
}

Q parse(char c) {
    if (c == 'i') return Q{1, V::I};
    if (c == 'j') return Q{1, V::J};
    if (c == 'k') return Q{1, V::K};
    cerr << "ERROR" << endl;
    return Q();
}

int findQ(const string& s_, int pos, Q x) {
    string s = (s_ + s_ + s_ + s_ + s_).substr(pos, 4 * s_.size());
    Q q;
    for (int i = 0; i < (int)s.size(); ++i) {
        q = mul(q, parse(s[i]));
        if (q == x)
            return i+1;
    }
    return -1;
} 

Q fold(const string& s) {
    Q r;
    for (auto c : s)
        r = mul(r, parse(c));
    return r;
}

bool solve(const string& s, int64_t L, int64_t X) {
    Q i{1, V::I};
    Q j{1, V::J};
    Q k{1, V::K};
    
    int64_t N = L*X;

    int p1 = findQ(s, 0, i);
    if (p1 < 0 || p1 >= N) return false;
    N -= p1;

    int p2 = findQ(s, p1 % L, j);
    if (p2 < 0 || p2 >= N) return false;
    N -= p2;

    Q rem = mul(fold(s.substr(L - (N % L), N % L)), pow(fold(s), N / L));
    return rem == k;
}

int main() {
    int T; cin >> T;

    for (int t = 1; t <= T; ++t) {
        int64_t L, X; cin >> L >> X;
        string ijk; cin >> ijk;

        auto ans = solve(ijk, L, X);
        cout << "Case #" << t << ": " << (ans ? "YES" : "NO") << endl;
    }

    return 0;
}
