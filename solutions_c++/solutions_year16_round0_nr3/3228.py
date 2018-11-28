#include <stdio.h>
#include <cmath>
#include <cstdint>
#include <algorithm>
#include <array>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

// using Number = __uint128_t;
using Number = uint64_t;

Number convertBase(Number n, int newBase) {
    bool remainders[256];
    int i = 0;
    while (n) {
        remainders[i++] = n % 2;
        n >>= 1;
    }

    Number ret = 0;
    for (auto j = i - 1; j != -1; --j) {
        ret *= newBase;
        ret += (remainders[j] ? 1 : 0);
    }
    return ret;
}

Number calNontrivialDivider(Number n, const vector<Number> &except) {
    if (n < 2) return 0;
    if (n % 2 == 0) {
        auto found = find(except.begin(), except.end(), 2);
        if (found == except.end()) return 2;
    }

    Number root = sqrt(n);
    for (Number i = 3; i <= root; i += 2) {
        if (n % i != 0) continue;
        auto found = find(except.begin(), except.end(), i);
        if (found != except.end()) continue;
        return i;
    }
    return 0;
}

void write(ostream &os, Number n) {
    char buf[256];
    char *pBuf = buf;
    while (n) {
        *(pBuf++) = '0' + (int)(n % 10);
        n /= 10;
    }

    for (auto i = pBuf - 1; i != buf - 1; --i)
        os << *i;
}

int solve(ostream &os, int lenOfDigit, int numOfJamcoinsToGenerate) {
    auto leftNumOfJamcoinsToGenerate = numOfJamcoinsToGenerate;

    Number base2 = (1 << (lenOfDigit - 1)) + 1;
    do {
        vector<Number> nontrivialDividers;
        nontrivialDividers.reserve(9);

        base2 += 2;
        const auto nontrivialDividerForBase2 = calNontrivialDivider(base2, nontrivialDividers);
        if (nontrivialDividerForBase2 == 0) continue;
        nontrivialDividers.push_back(nontrivialDividerForBase2);

        bool primeExists = false;
        for (int base = 3; base <= 10; ++base) {
            Number convertedN = convertBase(base2, base);
            const auto nontrivialDivider = calNontrivialDivider(convertedN, nontrivialDividers);
            if (nontrivialDivider == 0) {
                primeExists = true;
                break;
            }
            nontrivialDividers.push_back(nontrivialDivider);
        }

        if (primeExists) continue;

        // print jamcoin
        write(os, convertBase(base2, 10));
        os << ' ';

        // print nontrivialDividers
        for (auto i = 0; i < nontrivialDividers.size(); ++i) {
            write(os, nontrivialDividers[i]);
            if (i < nontrivialDividers.size() - 1)
                os << ' ';
        }

        os << endl;

        if (--leftNumOfJamcoinsToGenerate == 0)
            break;
    } while (true);

    return 0;
}

int main() {
    int numOfCases, lenOfDigit, numOfJamcoinsToGenerate;
    cin >> numOfCases;

    for (int i = 1; i <= numOfCases; ++i) {
        // read input
        cin >> lenOfDigit >> numOfJamcoinsToGenerate;
        // write output
        cout << "Case #" << i << ":" << endl;
        solve(cout, lenOfDigit, numOfJamcoinsToGenerate);
    }

    return 0;
}
