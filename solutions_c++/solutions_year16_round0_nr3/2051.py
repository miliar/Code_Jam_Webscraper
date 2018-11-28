#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

using ll = long long;
#define int ll

int pow(int a, int b, int m) {
    int r = 1;
    while (b) {
        if (b & 1) {
            r = r * a % m;
        }
        a = a * a % m;
        b >>= 1;
    }
    return r;
}

int dec_to_bin(int n) {
    int r = 0;
    int p = 1;
    while (n) {
        int d = n & 1;
        r += p * d;
        p *= 10;
        n >>= 1;
    }
    return r;
}

long long any_to_dec(int n, int b) {
    if (b == 10) {
        return n;
    }
    if (n <= 1) {
        return n;
    }
    int r = 0;
    int p = 1;
    while (n) {
        int d = n % 10;
        r += d * p;
        p *= b;
        n /= 10;
    }
    return r;
}

int find_divisor(int n, int b, int d) {
    constexpr int powers[] = { 1, 10, 100, 1000, 10000 };
    int l = 1000;
    if (d < sizeof(powers) / sizeof(powers[0])) {
        l = std::min(l, powers[d]);
    }
    for (int i = 2; i < l; ++i) {
        int r = (long long) n * b % i;
        r++;
        r = (r + pow(b, d - 1, i)) % i;
        if (r == 0) {
            return i;
        }
    }
    return -1;
}

signed main() {
    std::freopen("in", "r", stdin);
    std::freopen("out", "w", stdout);
    int tn;
    std::cin >> tn;
    for (int ti = 1; ti <= tn; ++ti) {
        int n, k;
        std::cin >> n >> k;
        int counter = 0;
        std::cout << "Case #" << ti << ":" << '\n';
        for (int i = 0; counter < k; ++i) {
            int b = dec_to_bin(i);
            bool ok = true;
            std::vector<int> v;
            for (int j = 2; j <= 10; ++j) {
                auto x = any_to_dec(b, j);
                auto y = find_divisor(x, j, n);
                if (y == -1) {
                    ok = false;
                    break;
                }
                v.push_back(y);
            }
            if (ok) {
                std::cout << '1' << std::setfill('0') << std::setw(n - 2) << b << '1';
                for (auto j : v) {
                    std::cout << ' ' << j;
                }
                std::cout << '\n';
                counter++;
            }
        }
    }
}
