/*
 * This solution uses the gmp/gmpxx library.
 * 1. Download and install the gmp and gmpxx library.
 * 2. Link the gmpxx library when compiling.
 *    e.g.
 *      g++ -Wall -O2 -o A A.cpp -lgmpxx
 *                               ^^^^^^^
 */
#include <iostream>
#include <gmpxx.h>
using namespace std;

inline mpz_class required(mpz_class r, mpz_class n) {
    return n*(2*r+1) + 2*n*(n-1);
}

mpz_class solve(mpz_class r, mpz_class t) {
    mpz_class low = 1;
    mpz_class hi = 1000000000;

    while (true) {
        mpz_class mid = (low + hi) / 2;
        if (required(r, mid) > t && required(r, mid-1) <= t) {
            return mid - 1;
        }
        if (required(r, mid) <= t) {
            low = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return 0;
}

int main() {

    int T;

    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        mpz_class t;
        mpz_class r;
        cin >> r >> t;
        cout << "Case #" << tc << ": " << solve(r, t) << endl;
    }

    return 0;
}

