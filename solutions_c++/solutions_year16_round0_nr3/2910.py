#include <array>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;


#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)
#define all(x) (x).begin(), (x).end()


//typedef long long LINT;
typedef __int128 LINT;

/* http://stackoverflow.com/questions/25114597/how-to-print-int128-in-g */
std::ostream& operator<<( std::ostream& dest, __int128_t value )
{
    std::ostream::sentry s( dest );
    if ( s ) {
        __uint128_t tmp = value < 0 ? -value : value;
        char buffer[ 128 ];
        char* d = std::end( buffer );
        do {
            -- d; *d = "0123456789"[ tmp % 10 ];
            tmp /= 10;
        } while ( tmp != 0 );
        if ( value < 0 ) { -- d; *d = '-'; }
        int len = std::end( buffer ) - d;
        if ( dest.rdbuf()->sputn( d, len ) != len ) {
            dest.setstate( std::ios_base::badbit );
        }
    }
    return dest;
}

int N, J;

std::random_device rd; // obtain a random number from hardware
std::mt19937 eng(rd()); // seed the generator


vector<int> _primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997};

int find_factor(LINT v)
{
    for(int p : _primes) {
        if(v % p == 0)
            return p;
    }
    return -1;
}

vector<long long> good(long long coin)
{
    vector<long long> factors;

    for(int base = 2; base <= 10; ++ base) {
        LINT base_p = 1;
        LINT v = 0;
        for(int j = 0; j < N; ++ j) {
            int coin_j = !!(coin & (1LL<<j));
            assert (coin_j == 0 || coin_j == 1);

            v += coin_j * base_p;
            base_p *= base;
        }
        //cerr << base << ' ' << v << " : " << base_p << endl;
        assert (v > 0);

        int f = find_factor(v);
        if(f == -1) {
            // pseudo-prime? skip!
            // cerr << base << ", " << v << " is not easily factorizable" << "\n";
            return vector<long long>();
        }

        //cerr << base << ", " << v << " is not prime due to factor " << f << "\n";

        assert(f > 0 && f != v);
        factors.push_back( (long long) f );
    }
    return factors;
}

int found = 0;

void generate()
{
    // random sampling based approach.
    long long pN = 1LL << N;
    std::uniform_int_distribution<long long> distr(0LL, pN); // define the range

    set<long long> dup;

    while (found < J) {
        long long r = distr(eng);
        if(dup.count(r)) continue;

        //fprintf(stderr, ". %lld\n", r);

        if(not (r & (1LL<<(N-1)))) continue;
        if(not (r & (1LL<<(0  )))) continue;

        vector<long long> ret = good(r);
        if(ret.empty()) {
            //fprintf(stderr, "invalid %lld\n", r);
            // invalid;
            continue;
        }
        else {
            ++found;
            dup.insert(r);

            for(int j = N-1; j >= 0; -- j) {
                cout << static_cast<int>(!!( (1LL<<j) & r ));
            }
            //cout << " [ " << r << " ] " ;

            for(long long x : ret) {
                cout << ' ' << x ;
            }
            cout << endl;
        }
    }
}


int main() {
    int T = 1;
    //cin >> T;
    assert (T == 1);

    //cin >> N >> J;
    N = 32; J = 500;
    cout << "Case #1:" << endl;

    //assert(N == 16 && J == 50);
    assert(N == 32 && J == 500);
    generate();

    return 0;
}

