#include <cstdlib>
#include <cmath>

#include <iostream>
#include <set>
#include <vector>

using namespace std;

using Number = vector<uint64_t>;

uint64_t getNumber(const Number& number, uint64_t base) {
    uint64_t result = 0;
    for (auto it = number.rbegin(); it != number.rend(); ++it) {
        result = result*base + *it;
    }
    return result;
}

uint64_t getNumberL(const Number& number, uint64_t base, uint64_t l) {
    uint64_t result = 0;
    for (auto it = number.rbegin(); it != number.rend(); ++it) {
        result = result*base + *it;
        if (result > l) {
            return l;
        }
    }
    return result;
}

uint64_t mod(const Number& number, uint64_t base, uint64_t n) {
    uint64_t result = 0;
    for (auto it = number.begin(); it != number.end(); ++it) {
        result = (result*base + *it) % n;
    }
    return result;
}

bool findDiv(const Number& vNumber, uint64_t base, uint64_t& divisor) {
    uint64_t number = getNumberL(vNumber, base, 1000000);
    uint64_t top = sqrt(number) + 0.1;
    uint64_t i = 2;
    while ( (i < top) && mod(vNumber, base, i) ) {
        ++i;
    }
    if ((i < top) && (0 == mod(vNumber, base, i))) {
        divisor = i;
        return true;
    } else {
        return false;
    }
}

void out(const Number& number) {
    for (auto i: number) {
        cout << i;
    }
}

int main() {
    static const int kN = 32;
    static const int kJ = 500;

    cout << "Case #1:" << endl;
    set<uint64_t> output;
    while (kJ != output.size()) {
        vector<uint64_t> number(kN);
        number[0] = 1;
        number[kN - 1] = 1;
        for (int i = 1; i + 1 < kN; ++i) {
            number[i] = rand() & 1;
        }
        Number divisor(11);
        int base = 2;
        while ( (base <= 10) && findDiv(number, base, divisor[base]) ) {
            ++base;
        }
        if (base > 10) {
            uint64_t number2 = getNumber(number, 2);
            if (output.end() == output.find(number2)) {
                output.insert(number2);
                out(number);
                for (int base = 2; base <= 10; ++base) {
                    cout << " " << divisor[base];
                }
                cout << endl;
            }
        }
    }

    return 0;
}
