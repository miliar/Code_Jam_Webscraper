#include <iostream>
#include <stdint.h>
#include <cmath>

using namespace std;

uint64_t interpret(uint32_t x, int b) {
    uint64_t n = 0;

    for(uint64_t u = 0; u < 32; u++) {
        if((x & (1 << u)) > 0) {
            uint64_t s = 1;

            for(uint64_t v = 0; v < u; v++) {
                s *= b;
            }

            n += s;
        }
    }

    return n;
}

int main(int argc, char **argv) {
    int t, n, j;
    cin >> t >> n >> j;

    cout << "Case #1:" << endl;

    uint64_t divisors[9];

    uint64_t mask = 1 << (n - 1);

    for(uint64_t remaining = 1; remaining < mask; remaining += 2) {
        uint64_t jamcoin = mask + remaining;

        bool complete = true;

        for(int base = 2; base <= 10; base++) {
            uint64_t interpreted = interpret(jamcoin, base);
            divisors[base - 2] = 0;

            for(uint64_t divisor = 2; divisor <= sqrt(interpreted) + 1; divisor++) {
                if(interpreted%divisor == 0) {
                    divisors[base - 2] = divisor;
                    break;
                }
            }

            if(divisors[base - 2] == 0) {
                complete = false;
                break;
            }
        }

        if(complete) {
            cout << interpret(jamcoin, 10);
            for(int base = 2; base <= 10; base++) {
                cout << ' ' << divisors[base - 2];
            }
            cout << endl;
            j--;
        }

        if(j == 0) {
            return 0;
        }
    }

    return 0;
}
