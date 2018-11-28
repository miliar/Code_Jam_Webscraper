#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <array>

using namespace std;

int n, j;

vector<vector<uint64_t>> pows;

uint64_t getPow(int base, int deg)
{
    return pows[base][deg];
}

uint64_t prime(uint64_t x)
{
    for (uint64_t i = 2; i * i <= x; i++) {
        if (x % i == 0) {
            return i;
        }
    }
    return 0;
}

void printVal(uint64_t val)
{
    for (int i = n - 3; i >= 0; i--) {
        cout << ((val & (1 << i)) ? 1 : 0);
    }
}

void solve()
{
    // int ff = static_cast<uint64_t>(1) << (n - 2);
    for (uint64_t i = 0; i < static_cast<uint64_t>(1) << (n - 2) && j > 0; i++) {
        vector<uint64_t> guess;
        uint64_t val;
        for (int base = 2; base <= 10; base++) {
            val = getPow(base, n - 1) + 1;
            for (int r = 0; r < n - 2; r++) {
                if (i & (1 << r)) {
                    val += getPow(base, r + 1);
                }
            }
            auto res = prime(val);
            if (res > 0) {
                guess.push_back(res);
            } else {
                break;
            }
        }
        if (guess.size() == 9) {
            cout << 1;
            printVal(i);
            cout << 1;
            cout << " ";
            for (auto &x: guess) {
                cout << x << " ";
            }
            cout << endl;
            j--;
        }
    }
}

int main()
{
    int t;
    scanf("%d", &t);

    pows.resize(11);
    for (int base = 2; base <= 10; base++) {
        pows[base].resize(17);
        pows[base][0] = 1;
        pows[base][1] = base;
        for (int q = 2; q <= 16; q++) {
            pows[base][q] = pows[base][q - 1] * base;
        }
    }

    for (int i = 0; i < t; i++) {
        scanf("%d%d", &n, &j);
        printf("Case #%d:\n", i + 1);
        solve();
    }
    return 0;
}