#include <iostream>
#include <cmath>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

namespace mp = boost::multiprecision;

using namespace std;

//std::map<int, int> primes;

mp::cpp_int findDivisor(mp::cpp_int num) {
//    if (primes.find(num) != primes.end())
//        return primes[num];

    for (mp::cpp_int i = 2; i <= static_cast<mp::cpp_int>(sqrt(num) + 1); i++) {
        if (num % i == 0) { //divisible par i
//            primes[num] = i;
            return i;
        }
    }

//    primes[num] = 0;
    return 0;
}

string showbits(int x, unsigned int len) {
    string out;

    for (int i = len - 1; i >= 0; i--) {
        if (x & (1u << i))
            out.append("1");
        else
            out.append("0");
    }

    return out;
}

mp::cpp_int changeBase(string base2, unsigned int base) {
    mp::cpp_int out = 0;
    mp::cpp_int power = 1;

    for (int i = 0; i < base2.size(); i++) {
        out += base2[base2.size() - 1 - i] == '1' ? power : 0;
        power *= base;
    }

    return out;
}

int main(int argc, char **argv) {
    unsigned int T;
    cin >> T;

    bool debug = false;

    for (unsigned int k = 0; k < T; k++) {
        cout << "Case #" << k + 1 << ":" << endl;
        int N, J;
        cin >> N >> J;

        int foundCoins = 0;

        for (int base10Num = (1 << (N - 1)) + 1; base10Num < (1 << N) && foundCoins < J; base10Num += 2) {
            if (debug) cout << "======" << endl;
            string numStr = showbits(base10Num, N);
            if (debug) cout << numStr << endl;

            int divisors[10] = {};

            for (unsigned int base = 2; base <= 10; base++) {
                mp::cpp_int bNum = changeBase(numStr, base);

                if (debug) cout << bNum << " (base " << base << ")" << endl;

                int divisor = static_cast<int>(findDivisor(bNum));

                if (divisor == 0) // prime, just stop
                    break;

                divisors[base] = divisor;

                if (base == 10) { // not prime in any base
                    cout << numStr;

                    for (unsigned int j = 2; j <= 10; j++) {
                        cout << " " << divisors[j];
                    }

                    cout << endl;
                    foundCoins++;

                }
            }
        }
    }

    return 0;
}

