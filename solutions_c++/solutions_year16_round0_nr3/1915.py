
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <vector>
using namespace std;

vector<pair<int, vector<int> > > memo;
vector<int> primes = { 2 };

long long convert(long long n, int base) {
    long long k = n;
    long long bn = 0;
    long long b = 1;
    for ( int i=0 ; k > 0 ; ++i ) {
        bn += (k & 1) ? b : 0;
        b *= base;
        k >>= 1;
    }
    return bn;    
}

long long jamcoin(long long bn) {
    for ( int i=0 ; i<primes.size() && primes[i] * primes[i] <= bn ; ++i ) {
        if ( bn % primes[i] == 0 ) {
            return primes[i];
        }
    }
    return -1;
}

void solve(int N, int J) {
    int k = N - 2;
    for ( int m=0 ; m < (1<<k) && J > 0 ; ++m ) {
        long long n = (1LL << (N - 1)) + (m << 1) + 1;
        vector<long long> tmp;
        for ( int b=2 ; b<=10 ; ++b ) {
            long long bn = convert(n, b);
            long long z = jamcoin(bn);
            //printf("n=%lld b=%d bn=%lld z=%lld\n", n, b, bn, z);
            if ( z == -1 ) {
                break;
            }
            tmp.push_back(z);
        }
        if ( tmp.size() == 9 ) {
            for ( int i=N-1 ; i>=0 ; --i ) {
                printf("%d", n & (1<<i) ? 1 : 0);
            }
            for ( int i=0 ; i<tmp.size() ; ++i ) {
                printf(" %lld", tmp[i]);
            }
            printf("\n");
            --J;
        }
    }
}

void preprocessing() {
    vector<int> sieve(65536, 1); // check prime
    for ( int i=4 ; i<65536 ; i += 2 ) sieve[i] = 0;
    for ( int i=3 ; i<65536 ; i += 2 ) {
        if ( sieve[i] ) {
            primes.push_back(i);
            for ( int j=i*2 ; j<65536 ; j += i ) {
                sieve[j] = 0;
            }
        }
    }
    // printf("-- primes = %ld\n", primes.size());
}

int main()
{
    preprocessing();

    int T;
    scanf("%d", &T);
    for ( int tc=1 ; tc<=T ; ++tc ) {
        printf("Case #%d:\n", tc);
        int N, J;
        scanf("%d %d", &N, &J);
        solve(N, J);
    }
    return 0;
}
