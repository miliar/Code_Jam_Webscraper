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
#include <gmp.h>
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
#define forIter(I,C) for(typeof((C).end()) I=(C).begin(); I!=(C).end(); ++I)
#define forNF(I,S,C) for(int I=(S); I<int(C); ++I)
#define forN(I,C) forNF(I,0,C)
#define forEach(I,C) forN(I,(C).size())
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef long long i64;
typedef unsigned long long u64;
typedef unsigned u32;

inline istream& skip_endl(istream& in)
{
    string s;
    getline(in, s);
    forIter( i, s ) assert(isspace(*i));
    return in;
}

inline string get_str()
{
    string ret;
    getline(cin, ret);
    return ret;
}

map<string, int> str_index;
int get_index(const string& s)
{
    return str_index.insert(make_pair(s, str_index.size())).first->second;
}
int get_str_index()
{
    return get_index(get_str());
}

/////////////////////////////////////////////////////////////////////////////

const int INF = 999999999;

typedef u64 Bits;

bool surely_win(Bits i, u32 N, Bits P)
{
    Bits S = Bits(1)<<N;
    assert(i < S);
    assert(P > 0);
    if ( i == 0 ) return 1;
    Bits H = S/2;
    if ( P <= H ) return 0;
    return surely_win((i-1)/2, N-1, P-H);
}

bool can_win(Bits i, u32 N, Bits P)
{
    Bits S = Bits(1)<<N;
    assert(i < S);
    assert(P < S);
    if ( i == S-1 ) return 0;
    Bits H = S/2;
    if ( P >= H ) return 1;
    return can_win(H-(S-i)/2, N-1, P);
}

Bits calc_min_win(u32 N, Bits P)
{
    Bits a = 0, b = Bits(1)<<N;
    while ( b-a > 1 ) {
        //TR(N|P|a|b);
        Bits m = a+(b-a)/2;
        if ( surely_win(m, N, P) )
            a = m;
        else
            b = m;
    }
    return a;
}

Bits calc_max_win(u32 N, Bits P)
{
    Bits a = 0, b = Bits(1)<<N;
    if ( P == b ) return b-1;
    while ( b-a > 1 ) {
        Bits m = a+(b-a)/2;
        //TR( N|P|a|b|m);
        if ( can_win(m, N, P) )
            a = m;
        else
            b = m;
    }
    return a;
}

int main(int argc, const char** argv)
{
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    int part_cases = 0;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    forN ( nc, num_cases ) {
        // parse input
        u32 N;
        Bits P;
        cin >> N >> P >> skip_endl;

        // error check
        if ( !cin ) {
            cout << "Error parsing input" << endl;
            return 1;
        }
        // main code

        Bits min_win = 0, max_win = 0;
        min_win = calc_min_win(N, P);
        max_win = calc_max_win(N, P);

        // output
        cout << "Case #"<<nc+1<<": ";
        cout << min_win << ' ' << max_win;
        cout << endl;
    }
}
