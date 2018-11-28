#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <set>
#include <map>
#include <functional>
#include <cmath>

using namespace std;

bool solve_bf(int x, int r, int c) {
    if (r > c) {
        r ^= c;
        c ^= r;
        r ^= c;
    }
    if ((r * c) % x) {
        return true;
    }
    if (x > c) {
        return true;
    }
    if (x == 1) {
        return false;
    }
    if (x == 2) {
        return false;
    }
    if (x == 3) {
        if (r == 1) {
            return true;
        }
        return false;
    }
    if (x == 4) {
        if (r == 1) {
            return true;
        }
        if (r == 2 && c == 2) {
            return true;
        }
        if (r == 2 && c == 4) {
            return true;
        }
        return false;
    }
}

bool solve(int x, int r, int c) {
    if ((r * c) % x) {
        return true;
    }
    if (r > c) {
        r ^= c;
        c ^= r;
        r ^= c;
    }
    if (x >= 8 && r >= 3 && c >= 3) {
        return true;
    }
    if (x > c) {
        return true;
    }
    if (r == 1) {
        if (x > 2) {
            return true;
        }
        return false;
    }
    if (r == 2) {
        if (x >= 4) {
            return true;
        }
        if ((x == 3) && (c < 3)) {
            return true;
        }
        return false;
    }
    return false;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        int x, r, c;
        cin >> x >> r >> c;
        bool r1 = solve(x, r, c);
        bool r2 = solve_bf(x, r, c);
        if (r1 != r2) {
            cerr << x << " " << r << " " << c << endl;
            cerr << r1 << " " << r2 << endl;
        }
        cout << "Case #" << i + 1 << ": " << (r1 ? "RICHARD" : "GABRIEL") << endl;
    }
    return 0;
}
