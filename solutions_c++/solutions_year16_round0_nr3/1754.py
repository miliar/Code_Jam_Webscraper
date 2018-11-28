#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <functional>
#include <cctype>
#include <sstream>
#include <cstring>
#include <iostream>
#include <iomanip>
//#include <gmp.h>
#ifdef HOME_RUN
# include <debug.hpp>
# include <dump.hpp>
# include <cassert>
#else
# define TR(x) do{}while(0)
# ifdef assert
#  indef assert
# endif
# define assert(x) do{}while(0)
#endif
using namespace std;

#define ALL(C) (C).begin(), (C).end()
#define forIter(I,C) for( auto I : (C) )
#define forNF(I,S,C) for( int I=(S); I<int(C); ++I )
#define forN(I,C) forNF(I,0,C)
#define forEach(I,C) forN(I,(C).size())
typedef long long i64; typedef unsigned long long u64; typedef unsigned u32;
typedef vector<int> VI; typedef vector<VI> VVI; typedef vector<string> VS;
typedef vector<u32> VU;

size_t line_number;
void input_error(const char* msg = 0) {
    cerr << "Input failed at line " << line_number;
    if ( msg ) cerr << ": " << msg;
    cerr << endl; exit(1);
}
void check_space(const string& s) {
    for ( auto c : s ) {
#ifdef HOME_RUN
        if ( !isspace(c&255) ) input_error("not a space");
        assert(isspace(c&255));
#endif
    }
}
string get_str(istream& in) {
    string ret; ++line_number; if ( !getline(in, ret) ) input_error(); return ret;
}
istream& skip_endl(istream& in) { check_space(get_str(in)); return in; }
istream& skip_eof(istream& in) { string s;
    while ( ++line_number, getline(in, s) ) check_space(s);
    if ( !in.eof() ) input_error(); return in;
}

map<string, int> str_index;
int get_index(const string& s) {
    return str_index.insert(make_pair(s, str_index.size())).first->second;
}
inline int get_str_index(istream& in) { return get_index(get_str(in)); }


typedef uint16_t u16;
VU primes;
static const u16 low_divisor_prime = 1;
std::vector<u16> low_divisor;

void make_primes(u32 max)
{
    ++max;
    primes.clear();
    size_t msize = 100+size_t(1.1*max/log(max+2));
    size_t mid = sqrt(max+1);
    primes.reserve(msize);
    low_divisor.assign(max, 0);
    auto ld = low_divisor.data();
    ld[0] = 1;
    ld[1] = 0;
    for ( u32 p = 2; p <= mid; ++p ) {
        if ( ld[p] ) continue;
        primes.push_back(p);
        ld[p] = low_divisor_prime;
        for ( u32 i = 2*p; i < max; i += p ) {
            auto& s = ld[i];
            if ( !s ) s = p;
        }
    }
    for ( u32 p = mid+1; p < max; ++p ) {
        if ( ld[p] ) continue;
        primes.push_back(p);
        ld[p] = low_divisor_prime;
    }
}

/////////////////////////////////////////////////////////////////////////////

const int INF = 999999999;

size_t N, J;

typedef __uint64_t u128;
u64 dd[9];

u64 get_divisor(u128 v)
{
    for ( auto p : primes ) {
        if ( v != p && v % p == 0 )
            return p;
    }
    return 0;
}

bool is_good(u32 v)
{
    for ( int b = 2; b <= 10; ++b ) {
        u128 r = 0, e = 1;
        for ( size_t i = 0; i < N; ++i, e *= b ) {
            if ( v & (1u<<i) )
                r += e;
        }
        u64 d = get_divisor(r);
        if ( !d ) return 0;
        dd[b-2] = d;
    }
    return true;
}

int num_cases = 1, part_cases = 0;
int main(int argc, const char** argv)
{
    cin >> num_cases >> skip_endl;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    make_primes(1000000);
    forN ( nc, num_cases ) {
        // parse input
        cin >> N >> J >> skip_endl;
        
        // error check
        if ( !cin ) input_error();
        // main code

        // output
        cout << "Case #"<<nc+1<<":"<<endl;

        size_t cnt = 0;
        for ( u32 i = 0; i < 1u<<(N-2); ++i ) {
            u32 v = i*2+1+(1u<<(N-1));
            if ( is_good(v) ) {
                for ( int i = N; i--; ) {
                    cout << ((v>>i)&1);
                }
                for ( int i = 0; i < 9; ++i )
                    cout << ' ' << dd[i];
                cout << endl;
                if ( ++cnt == J ) break;
            }
        }
    }
    cin >> skip_eof;
}
