#include <iostream>
#include <cmath>
#include <bitset>

using namespace std;

struct Primes {
    void push_back(unsigned int n) { p[n_p++] = n; }
    unsigned int size() { return n_p; }
    unsigned int n_p;
    unsigned int p[5761456];
} primes;

unsigned int divisor(unsigned long long i) 
{
    auto sq = sqrt(i);
    const auto end = primes.size();
    for(auto j = 0u; j < end; j++) {
        auto p = primes.p[j];
        if(p > sq) {
            return 0;
        }

        unsigned long long d = i / p;
        if(i == p * d) {
            return p;
        }
    }
    return 0;
}

void solve()
{
    unsigned long long N[16];
    unsigned long long div[16];
    unsigned long long n, j;
    cin >> n;
    cin >> j;

    for(auto base = 2ull; base <= 10ull; base++) {
        N[base] = (pow(base, n-1ull) + 1ull);
    }
    for(auto i = 1u; i < 15; i++) {
        if((N[2] >> i) % 2) {
            for(auto base = 3ull; base <= 10ull; base++) {
                N[base] += pow(base, i);
            }
        }
    }

    while(j) {        
        bool good = true;
        for(auto base = 2ull; base <= 10ull; base++) {
            div[base] = divisor(N[base]);
            if(div[base] == 0) {
                good = false;
                break;
            }
        }

        if(good) {
            cout << endl;
            cout << bitset<16>(N[2]);
            for(auto base = 2ull; base <= 10ull; base++) {
                cout << " " << div[base];
            }
            j--;
        }

        N[2] += 2;
        for(auto base = 3ull; base <= 10ull; base++) {
            N[base] = (pow(base, n-1ull) + 1ull);
        }
        for(auto i = 1u; i < 15; i++) {
            if((N[2] >> i) % 2) {
                for(auto base = 3ull; base <= 10ull; base++) {
                    N[base] += pow(base, i);
                }
            }
        }
    }
}

int main()
{
    primes.n_p = 0;
    primes.push_back(2);
    primes.push_back(3);
    primes.push_back(5);
    primes.push_back(7);
    primes.push_back(11);
    primes.push_back(13);
    primes.push_back(17);

    unsigned long long limit = pow(10ull, 8ull);

    for(auto i = 19ull; i < limit; i+=2) {
        if(not divisor(i)) {
            primes.push_back(i);
        }
    }

    unsigned int cases;
    cin >> cases;
    for(auto i = 1u; i <= cases; i++) {
        cout << "Case #" << i << ":";
        solve();
        cout << endl;
    }
    return 0;
}
