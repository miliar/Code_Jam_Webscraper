#include <bits/stdc++.h>

using namespace std;

typedef int i64;

struct Q {
    i64 s;
    i64 i;
    i64 j;
    i64 k;
    Q(i64 _s, i64 _i, i64 _j, i64 _k)
        : s(_s), i(_i), j(_j), k(_k) {}
    Q operator -() const {
        return Q(-s, -i, -j, -k);
    }
};

inline Q operator *(const Q &a, const Q &b) {
    return Q(
        a.s * b.s - a.i * b.i - a.j * b.j - a.k * b.k,
        a.s * b.i + a.i * a.s + a.j * b.k - a.k * b.j,
        a.s * b.j - a.i * b.k + a.j * b.s + a.k * b.i,
        a.s * b.k + a.i * b.j - a.j * b.i + a.k * b.s);
}

inline bool operator == (const Q &a, const Q &b) {
    return a.s == b.s && a.i == b.i && a.j == b.j && a.k == b.k;
}

inline bool operator != (const Q &a, const Q &b) {
    return a.s != b.s || a.i != b.i || a.j != b.j || a.k != b.k;
}

inline Q operator *=(Q &a, const Q&b) {
    return a = a * b;
}

inline i64 abs2(i64 x) {
    return x * x;
}

inline i64 abs2(const Q &a) {
    return abs2(a.i) + abs2(a.j) + abs2(a.k) + abs2(a.s);
}

inline Q conj(const Q &q) {
    return Q(q.s, -q.i, -q.j, -q.k);
}

inline Q operator / (const Q &a, i64 x) {
    assert(a.s % x == 0 && a.i % x == 0 && a.j % x == 0 && a.k % x == 0);
    return Q(a.s / x, a.i / x, a.j / x, a.k / x);
}

inline Q inverse(const Q &q) {
    return conj(q) / abs2(q);
}

const int LX = 10000;

const Q q1 = {1, 0, 0, 0},
    qi = {0, 1, 0, 0},
    qj = {0, 0, 1, 0},
    qk = {0, 0, 0, 1};

Q fromChar(char c) {
    switch (c) {
    case '1':
        return q1;
    case 'i':
        return qi;
    case 'j':
        return qj;
    case 'k':
        return qk;
    default:
        assert(false);
    }
}

bool solve(istream &in) {
    int l, x;
    in >> l >> x;
    string originalS;
    in >> originalS;
    string s;
    s.reserve(l * x);
    
    for (int i = 0; i < x; ++i)
        s += originalS;
    Q total = q1;
    for (int i = 0; i < l * x; ++i)
        total *= fromChar(s[i]);
    
    Q first = q1;
    for (int i = 1; i <= l * x; ++i) {
        first *= fromChar(s[i - 1]);
        if (first != qi)
            continue;
        Q second = q1;
        for (int j = i + 1; j <= l * x; ++j) {
            second *= fromChar(s[j - 1]);
            if (second != qj)
                continue;
            Q third = -qk * total;
            if (third == qk)
                return true;
        }
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    ifstream in("c.txt");
    ofstream out("c_out.txt");
    int t;
    in >> t;
    for (int i = 1; i <= t; ++i) {
        out << "Case #" << i << ": " << (solve(in)? "YES" : "NO") << '\n';
    }
}
    

