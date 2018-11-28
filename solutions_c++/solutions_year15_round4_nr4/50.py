#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <bitset>
#include <cmath>
#include <numeric>
#include <complex>
#include <algorithm>
#include <functional>
#include <cctype>
#include <cstring>
#include <sstream>
#include <iostream>
#include <iomanip>
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
typedef vector<int> VI; typedef vector<VI> VVI; typedef vector<string> VS;
typedef long long i64; typedef unsigned long long u64; typedef unsigned u32;

size_t line_number;
void check_space(const string& s) { for ( auto c : s ) assert(isspace(c&255)); }
void input_error() {
    cerr << "Input failed at line " << line_number << endl; exit(1);
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


/////////////////////////////////////////////////////////////////////////////

inline int count_low_zeros(u32 v) { return __builtin_ctz(v); }
inline int count_low_zeros(u64 v) { return __builtin_ctzll(v); }

// binary gcd
template<typename T>
T gcd(T a, T b)
{
    if ( !a ) return b;
    if ( !b ) return a;
    int s = count_low_zeros(a|b);
    a >>= count_low_zeros(a);
    b >>= count_low_zeros(b);
    for (;;) {
        while ( a > b ) {
            a -= b;
            a >>= count_low_zeros(a);
        }
        {
            if ( !(b -= a) ) return a<<s;
            b >>= count_low_zeros(b);
        }
    }
}

/////////////////////////////////////////////////////////////////////////////

const u32 MOD = 1000000007;

map<pair<int, int>, u32> cc;

int R, C;

const u32 NP = 5;
const u32 pp[NP] = { 1, 3, 4, 6, 12 };

struct State
{
    u64 cc2[NP], cc3[NP];

    void clear() {
        fill_n(cc2, NP, 0);
        fill_n(cc3, NP, 0);
    }
    void init() {
        clear();
        cc2[0] = 1;
        cc3[0] = 1;
    }
};

pair<u32, u32> combine(u32 /*k*/, u32 p, u32 p2, u32 c)
{
    u32 g = gcd(p, p2);
    u32 np = p/g*p2;
    u32 nk = find(pp, pp+NP, np)-pp;
    u32 nc = u64(c)*g%MOD;
    return make_pair(nk, nc);
}

u32 calc()
{
    State ss[128];
    ss[0].init();
    forN ( i, R ) ss[i+1].clear();
    forN ( r, R ) {
        const State& s = ss[r];
        forN ( k, NP ) {
            u32 p = pp[k];
            if ( u32 c = s.cc2[k]%MOD ) {
                // 2222222222
                ss[r+1].cc3[k] += c;
                // 221221
                // 221221
                if ( C%3 == 0 ) {
                    pair<u32, u32> nn = combine(k, p, 3, c);
                    u32 nk = nn.first;
                    u32 nc = nn.second;
                    ss[r+2].cc3[nk] += nc;
                }
                // 112222112222
                // 222112222112
                if ( C%6 == 0 ) {
                    pair<u32, u32> nn = combine(k, p, 6, c);
                    u32 nk = nn.first;
                    u32 nc = nn.second;
                    ss[r+2].cc3[nk] += nc;
                }
                // 12221222
                // 12121212
                // 22122212
                if ( C%4 == 0 ) {
                    pair<u32, u32> nn = combine(k, p, 4, c);
                    u32 nk = nn.first;
                    u32 nc = nn.second;
                    ss[r+3].cc3[nk] += nc;
                }
            }
            if ( u32 c = s.cc3[k]%MOD ) {
                // 3333333
                // 3333333
                ss[r+2].cc2[k] += c;
            }
        }
    }
    u64 ret = 0;
    const State& s = ss[R];
    forN ( k, NP ) {
        ret += s.cc2[k];
        ret += s.cc3[k];
    }
    return ret % MOD;
}

int num_cases = 1, part_cases = 0;
int main(int argc, const char** argv)
{
    NTR = 100;
    cin >> num_cases >> skip_endl;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    forN ( nc, num_cases ) {
        // parse input
        cin >> R >> C >> skip_endl;

        // error check
        if ( !cin ) input_error();
        // main code

        u32& result = cc[make_pair(R, C)];
        if ( !result ) {
            result = calc();
        }
        
        // output
        cout << "Case #"<<nc+1<<": ";
        cout << result;
        cout << endl;
    }
    cin >> skip_eof;
}
