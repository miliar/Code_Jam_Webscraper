#include <iostream>
#include <cmath>
#include <unordered_map>
#include <vector>
#include <stdint.h>

/**
 * There *MUST* be some trick to this where you don't
 * have to ever compute the palindromes. I know we can
 * determine per digit size the number of palindromes
 * that should exist, but I am missing how that correlates
 * with its perfect square.
 *
 * 10^100 more than likely means that we only have to test
 * 50 numbers in total. I would hope.
 */

bool palindrome(uint64_t x, uint64_t &y) {
    if (x < 0) return false;
    if (x == 0) return true;
    if (palindrome(x / 10, y) && (x % 10 == y % 10)) {
        y /= 10;
        return true;
    }
    return false;
}

int main(int argc, char** argv)
{
    std::unordered_map<uint64_t, bool> mem;
    std::vector<uint64_t> fas;
    uint64_t n = 10000000;
    mem.reserve(n);

    for (uint64_t i = 0; i < n; i++) {
        auto got = mem.find(i);
        if (got == mem.end()) {
            uint64_t ii = i;
            if (palindrome(ii, ii)) {
                uint64_t ps = i * i;
                uint64_t nps = ps;
                mem[i] = true;
                if (palindrome(ps, ps)) {
                    mem[nps] = true;
                    fas.push_back(nps);
                } else {
                    mem[nps] = false;
                }
            } else {
                mem[i] = false;
            }
        } else if (got->second) {
            uint64_t k = got->first;
            uint64_t ps = k * k;
            uint64_t nps = ps;
            got = mem.find(ps);
            if (got == mem.end()) {
                if (palindrome(ps, ps)) {
                    mem[nps] = true;
                    fas.push_back(nps);
                } else {
                    mem[nps] = false;
                }
            } else if (got->second) {
                fas.push_back(got->first);
            }
        }
    }

    uint64_t cases;
    std::cin >> cases;
    for (uint64_t i = 1; i <= cases; i++) {
        uint64_t start, end;
        uint64_t found = 0;
        std::cin >> start >> end;
        for (uint64_t t : fas) {
            if (t >= start && t <= end) {
                found++;
            }
        }
        std::cout << "Case #" << i << ": " << found << "\n";
    }
}
