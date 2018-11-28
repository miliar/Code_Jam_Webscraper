#include <iostream>
#include <set>
#include <map>
#include <sstream>
#include <cmath>

using namespace std;

set<unsigned long long> known_prime;
map<unsigned long long, unsigned long long> divisor;

void make_prime_table(void)
{
    set<unsigned long long>::const_iterator it;
    for(int n = 3; n < 100000; ++n) {
        const unsigned long long limit = sqrt(n);
        bool is_prime = true;
        it = known_prime.begin();
        for(; it != known_prime.end() && *it <= limit; ++it) {
            if(n % *it == 0) {
                is_prime = false;
                break;
            }
        }
        if(is_prime)
            known_prime.insert(n);
    }
}

bool is_prime(unsigned long long n)
{
    cerr << "prime(" << n << ") ";
    set<unsigned long long>::const_iterator it;

    if(n == 1 || known_prime.find(n) != known_prime.end())
        return true;

    it = known_prime.begin();
    for(; it != known_prime.end(); ++it) {
        if(n % *it == 0) {
            divisor[n] = *it;
            return false;
        }
    }

    unsigned long long limit = sqrt(n);
    for(unsigned long long m = *known_prime.rbegin() + 1; m <= limit; ++m) {
        bool is_prime = true;
        set<unsigned long long>::const_iterator it = known_prime.begin();
        for(; it != known_prime.end(); ++it) {
            if(m % *it == 0) {
                divisor[m] = *it;
                is_prime = false;
                break;
            }
        }

        if(is_prime) {
            known_prime.insert(m);
            if(n % m == 0) {
                divisor[n] = m;
                return false;
            }
        }
    }
    return known_prime.find(n) != known_prime.end();
}

unsigned long long check(unsigned long long n)
{
    const unsigned long long limit = sqrt(n);
    set<unsigned long long>::const_iterator it;
    for(it = known_prime.begin(); it != known_prime.end() && *it <= limit; ++it) {
        if(n % *it == 0) {
            return *it;
        }
    }
    return 0;
}

void solve(int N, int J)
{
    int i, j;

    j = 0;
    for(i = 0; i < 1 << (N - 2); ++i) {
        stringstream result;

        unsigned n = (1 << (N - 1)) | (i << 1) | 1;
        for(j = N - 1; j >= 0; j--) {
            result << ((n & (1 << j)) != 0);
        }

        bool is_jamcoin = true;
        for(int base = 2; base <= 10; ++base) {
            unsigned long long factor = 1;
            unsigned long long m = 0;
            for(int k = 0; k < N; ++k) {
                m += ((n & (1 << k)) != 0) * factor;
                factor *= base;
            }
#if 1
            unsigned long long divisor = check(m);
            if(divisor) {
                result << " " << divisor;
            } else {
                is_jamcoin = false;
                break;
            }
#else
            if(is_prime(m)) {
                is_jamcoin = false;
                break;
            }
            result << " " << divisor[m];
            // result << "(" << m << ")";
#endif
        }
        if(is_jamcoin) {
            cout << result.str() << endl;
            --J;
            if(J == 0)
                return;
        }
    }
}

int main(void)
{
    known_prime.insert(2);
    make_prime_table();

    cout << "Case #1:" << endl;
    // solve(6, 3);  // sample
    solve(16, 50);  // small
    // solve(32, 500); // large
    return 0;
}

