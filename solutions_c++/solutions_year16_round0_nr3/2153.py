#include <iostream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <map>
#include <cmath>
#include <cstdlib>

using namespace std;

//#define SIEVE_SIZE 2147483649
//
//bool sieve[2147483649];
//
////map<int64_t, int64_t> primes;
//
//void fill_sieve(int64_t t) {
////    if (sieve[t]) {
////        primes.insert(pair<int64_t, int64_t>(1,2));
//////        primes.push_back(t);
////    }
//
//    int64_t counter = t * 2;
//    while (counter <= SIEVE_SIZE) {
//        sieve[counter] = false;
//
//        counter += t;
//    }
//}

int64_t is_prime(int64_t n) {
    for (int i = 2; i <= sqrt(n); ++i) {
        if ((n % i) == 0) {return i;}
    }

    return -1;
}

int64_t base2ToBaseX(int64_t n, int base) {
    int64_t res = 0;
    int counter = 0;

    while (n > 0) {
        int low = n % 2;
        n >>= 1;

        res += low * pow(base, counter++);
    }

    return res;
}

int main() {
//    // clear sieve
//    for (int64_t i = 0; i < SIEVE_SIZE; ++i) {
//        sieve[i] = true;
//    }
//
//    for (int64_t j = 2; j < (SIEVE_SIZE / 2); ++j) {
//        if ((j % 1000000) == 0) cout << j << endl;
//        fill_sieve(j);
//    }
//
//    // all possible prime numbers are in 'primes' now
//    // let's interpret them in each base
//    for (int k = 1; k <= 1000; ++k) {
//        if (sieve[k]) cout << k << endl;
//    }

    cout << "Case #1:" << endl;

    int64_t start = 0b1000000000000001;//32769;
    int64_t end =   0b1111111111111111;

//    int64_t start = 0b100001;
//    int64_t end = 0b111111;
    const int results_needed = 50;

    int found_counter = 0;

    vector<int64_t> bag;
    bool found = false;

    for (int64_t i = start; i <= end; i+=2) {
        int64_t tt = is_prime(i);
        if (tt == -1) { continue; }

        bag.push_back(tt);

        for (int j = 3; j <= 10; ++j) {
            int64_t nmb = base2ToBaseX(i, j);

            int64_t tt = is_prime(nmb);
            if (tt == -1) {break;}

            if (j == 10) {found = true;}
            bag.push_back(tt);
        }

        if (found) {
            found = false;

            found_counter++;

            cout << bitset<16>(i);

            for (int j = 0; j < 9; ++j) {
                cout << " " << bag[j];
            }

            cout << endl;

            if (found_counter >= results_needed) {
                return 0;
            }
        }

        bag.clear();
    }

    return 0;
}