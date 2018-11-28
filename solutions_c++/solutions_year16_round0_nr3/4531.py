#include <cassert>
#include <cmath>
#include <cstdint>
#include <bitset>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int T, N, J;

#define LEN (16)
#define MAX_PRIME (32000)

vector<uint32_t> prime_list;
map<uint32_t, vector<uint32_t>> prime_map;

void primes() {
    vector<int> prime(MAX_PRIME);
    for (int i = 0; i < MAX_PRIME; i++) {
        prime[i] = i;
    }
    for (int i = 2; i < MAX_PRIME; ++i) {
        if (prime[i] != 0) {
            for (int j = 2 * i; j < MAX_PRIME; j+=i) {
                prime[j] = 0;
            }
        }
    }
    for (int i = 2; i < MAX_PRIME; ++i) {
        if (prime[i] != 0) {
            prime_list.push_back(i);
        }
    }
}

uint32_t my_div(uint32_t base, uint32_t power, uint32_t number) {
    uint32_t z2 = (base * base) % number;
    uint32_t z4 = (z2 * z2) % number;
    uint32_t z8 = (z4 * z4) % number;
    switch (power) {
    case 16:
        return (((((z8 * z4) % number) * z2) % number) * base) % number;
    case 32:
        return ((((((((z8 * z8) % number) % number) * z8) % number * z4) % number) * z2) % number * base) % number;
    }
    assert(false);
    return 0;
}

void precalc(int k) {
    for (uint32_t i = 2; i < 11; ++i) {
        vector<uint32_t> divs(prime_list.size());

        for (uint32_t j = 0; j < prime_list.size(); ++j) {
            divs[j] = my_div(i, k, prime_list[j]);
        }

        prime_map[i] = divs;
    }
}

uint32_t convert(uint32_t i, uint32_t base) {
    uint32_t res = 0, p = 0;
    while (i != 0) {
        if (i % 2 == 1) {
            res += static_cast<uint32_t>(pow(base, p));
        }
        i /= 2;
        ++p;
    }
    return res;
}

vector<uint32_t> check(int i) {
    vector<uint32_t> res;
    for (int base = 2; base < 11; ++base) {
        int w = 0;
        uint32_t base_i = convert(i, base);
        while (w < prime_list.size()) {
            uint32_t value = prime_map[base][w];
            if ((value + base_i) % prime_list[w] == 0) {
                res.push_back(prime_list[w]);
                break;
            }
            ++w;
        }
    }
    return res;
}

void solve() {
    uint32_t i = 1;
    int j = 0;
    while (j < J) {
        vector<uint32_t> divs = check(i);
        if (divs.size() == 9) {
            cout << "1" << bitset<LEN-1>(i) << " ";

            for (uint32_t d : divs) cout << d << " ";
            cout << endl;

            j++;
        }
        i += 2;
    }
    return;
}

int main() {
    primes();
    precalc(LEN);

    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N >> J;
        cout << "Case #" << t << ":" << endl;
        solve();
    }
    return 0;
}