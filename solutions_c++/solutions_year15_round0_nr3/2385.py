#include <iostream>
#include <tuple>

using namespace std;

typedef long long num;

#define FOR(i, a, b) for (int i(a), _end(b); i < _end; ++i)
#define REP(i, n) FOR(i, 0, n)

int nxt(int i) { return i % 3 + 1; }

struct H {
    bool neg;
    int i;

    H operator*(const H& o) const {
        bool neg = this->neg ^ o.neg;
        int i;
        if (!this->i || !o.i) {
            i = this->i ^ o.i;
        } else if (this->i == o.i) {
            neg ^= 1;
            i = 0;
        } else if (nxt(this->i) == o.i) {
            i = nxt(o.i);
        } else {
            neg ^= 1;
            i = nxt(this->i);
        }
        return {neg, i};
    }

    bool operator==(const H& o) const {
        return neg == o.neg && i == o.i;
    }

    bool operator!=(const H& o) const {
        return !(*this == o);
    }

    int pos() const {
        return 4*neg + i;
    }

    H inv() const {
        if (!i) return {neg, 0};
        return {!neg, i};
    }

    H pow(int k) const {
        bool neg = this->neg;
        if (neg) {
            neg = k % 2;
        }
        int i = this->i;
        if (!i) {
            return {neg, i};
        }
        neg ^= (k / 2) % 2;
        i = k % 2 ? i : 0;
        return {neg, i};
    }
};

int L; num X;
char s[10005];
H pfx[10005];

H calc(int l, int r) {
    return pfx[l].inv() * pfx[r];
}

bool go() {
    static int mx[8];
    REP(i, 8) mx[i] = -1;
    REP(i, L+1) {
        int pos = pfx[i].pos();
        mx[pos] = max(mx[pos], i);
    }

    for (int l = 0; l < L; ++l) {
        int r = mx[(calc(0, l)*H{false, 2}).pos()];
        if (r >= l) REP(a, 4) REP(b, 4) {
            num diff = X-1-a-b;
            if (diff < 0 || diff % 4) continue;
            if (calc(0, L).pow(a)*calc(0, l) == H{false, 1}
                    && calc(r, L)*calc(0, L).pow(b) == H{false, 3}) return true;
        }
    }

    for (int l = 0; l < L; ++l) REP(a, 4) {
        if (calc(0, L).pow(a)*calc(0, l) != H{false, 1}) continue;
        REP(b, 4) {
            int r = mx[((calc(l, L)*calc(0, L).pow(b)).inv()*H{false, 2}).pos()];
            if (r == -1) continue;
            REP(c, 4) {
                num diff = X-2-a-b-c;
                if (diff < 0 || diff % 4) continue;
                if (calc(r, L)*calc(0, L).pow(c) == H{false, 3}) return true;
            }
        }
    }

    return false;
}

void MAIN(int tc) {
    cin >> L >> X;
    cin >> s;

    for (int i = 0; i < L; ++i) {
        pfx[i+1] = pfx[i] * H{false, s[i]-'h'};

    }

    cout << "Case #" << tc << ": " << (go() ? "YES" : "NO") << "\n";
}

int main() {
    int T; cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        MAIN(tc);
    }
    return 0;
}
