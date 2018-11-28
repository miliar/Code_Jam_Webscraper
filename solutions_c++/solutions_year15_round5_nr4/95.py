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

const u32 MAX_P = 10000;
u32 P;
vector<i64> ss;
vector<u64> cc;

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
        cin >> P >> skip_endl;
        ss.resize(P);
        forN ( i, P ) cin >> ss[i];
        cin >> skip_endl;
        cc.resize(P);
        forN ( i, P ) cin >> cc[i];
        cin >> skip_endl;

        // error check
        if ( !cin ) input_error();
        // main code

        vector<i64> rr;
        if ( u32 zcnt = __builtin_ctzll(cc[0]) ) {
            rr.resize(zcnt);
            for ( auto& c : cc ) c >>= zcnt;
        }
        //TR(ss);TR(cc);
        i64 last_v0 = ss[0];
        while ( cc.size() > 1 ) {
            map<i64, u64> nc;
            if ( ss[0] < 0 ) {
                for ( auto v0 : ss ) {
                    if ( v0 < last_v0 ) continue;
                    nc.clear();
                    for ( size_t i = cc.size(); i--; ) {
                        nc[ss[i]-v0] = cc[i];
                    }
                    //TR(v0|nc);
                    for ( auto i = begin(nc); i != end(nc); ++i ) {
                        i64 v = i->first;
                        u64 c = i->second;
                        if ( c ) {
                            u64& pc = nc[v-v0];
                            if ( c > pc ) {
                                v0 = 0;
                                break;
                            }
                            pc -= c;
                        }
                    }
                    //TR(v0|nc);
                    if ( v0 ) {
                        rr.push_back(v0);
                        last_v0 = v0;
                        break;
                    }
                }
            }
            else {
                i64 v0 = ss[1];
                //TR(v0);
                rr.push_back(v0);
                forEach ( i, cc ) {
                    i64 v = ss[i];
                    u64 c = cc[i] - nc[v-v0];
                    nc[v] = c;
                }
            }
            ss.clear();
            cc.clear();
            for ( auto i : nc ) {
                if ( i.second ) {
                    ss.push_back(i.first);
                    cc.push_back(i.second);
                }
            }
            //TR(ss);TR(cc);
        }
        
        sort(ALL(rr));
        //TR(rr);
        
        // output
        cout << "Case #"<<nc+1<<":";
        for ( auto v : rr )
            cout << ' ' << v;
        cout << endl;
    }
    cin >> skip_eof;
}
