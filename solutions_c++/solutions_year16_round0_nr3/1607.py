#include <bits/stdc++.h>
#define fst first
#define scd second
#define N 32
using namespace std;
typedef unsigned long long ull;

bool factor(const ull d, const ull x, const ull b, const ull y) {
    return (y % d) == 0 && (x % d == 0 || b % d == 0);
}

ull isPseudoPrime(pair<ull, ull> p, const ull b) {
    ull x, y;
    tie(x, y) = p;
    if (factor(2, x, b, y))
        return 2;
    for (ull i = 3; i <= y; i += 2)
        if (factor(i, x, b, y))
            return i;
    return 0;
}

pair<ull, ull> inBase(const string &s, const int split, const int b) {
    pair<ull, ull> ret = {0, 0};
    for (int i = 0; i < split; i++) {
        ret.fst *= b;
        ret.fst += s[i] - '0';
    }
    const int len = s.length();
    for (int i = split; i < len; i++) {
        ret.scd *= b;
        ret.scd += s[i] - '0';
    }
    return ret;
}

template <size_t G> void operator++(bitset<G> &in) {
    for (size_t i = 0; i < G; ++i) {
        if (in[i] == 0) {
            in[i] = 1;
            break;
        }
        in[i] = 0;
    }
}

int main() {
    int t;
    cin >> t;
    ull base[10];
    const int split(N/2);
    for (int i = 2; i <= 10; i++) {
        base[i] = 1;
        for (int j = 1; j <= split; j++)
            base[i] *= i;
    }
    int n, j;
    cin >> n >> j;
    bitset<N> b;
    cout << "Case #1:" << endl;
    for (b[0] = b[n - 1] = 1; j > 0; ++b) {
        if (b[0] != b[n - 1] || b[0] != 1)
            continue;
        const string bs = b.to_string();
        ull factor[10];
        bool valid = true;
        for (int i = 2; i <= 10; i++) {
            if ((factor[i] = isPseudoPrime(inBase(bs, split, i), base[i])) == 0) {
                valid = false;
                break;
            }
        }
        if (valid) {
            j--;
            cout << bs;
            for (int i = 2; i <= 10; i++)
                cout << " " << factor[i];
            cout << endl;
        }
    }
}
