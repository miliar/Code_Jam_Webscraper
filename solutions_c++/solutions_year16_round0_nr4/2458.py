#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

typedef long long li;

li binpow(li a, li p) {
    li r = 1;
    while (p > 0) {
        if (p & 1) {
            r *= a;
        }

        a *= a;
        p >>= 1;
    }

    return r;
}

int main() {
    int tests;
    cin >> tests;

    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ":";

        li k, c, s;
        cin >> k >> c >> s;

        if (k != s) {
            cout << " IMPOSSIBLE" << endl;
            continue;
        }

        li step = binpow(k, c - 1);
        li mx = binpow(k, c);
        for (li y = 1; y <= mx; y += step) {
            cout << " " << y;
        }
        cout << endl;

    }
    return 0;
}
