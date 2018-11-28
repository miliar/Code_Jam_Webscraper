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
void input_error(const char* m = "") {
    cerr << "Input failed at line " << line_number << ": " << m << endl; exit(1);
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


/////////////////////////////////////////////////////////////////////////////

const int INF = 999999999;
const size_t MAX_N = 100;
size_t N;
double V, T;
double vv[MAX_N];
double tt[MAX_N];

int num_cases = 1, part_cases = 0;
int main(int argc, const char** argv)
{
    cin >> num_cases >> skip_endl;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    forN ( nc, num_cases ) {
        // parse input
        cin >> N >> V >> T >> skip_endl;
        forN ( i, N ) {
            cin >> vv[i] >> tt[i] >> skip_endl;
        }
        //cin >> skip_endl;
        
        // error check
        if ( !cin ) input_error();
        // main code

        double result = -1;
        if ( N == 1 ) {
            if ( T == tt[0] )
                result = V/vv[0];
        }
        else if ( N == 2 ) {
            double t1 = tt[0], t2 = tt[1];
            double v1 = vv[0], v2 = vv[1];
            if ( t1 > t2 ) {
                swap(t1, t2);
                swap(v1, v2);
            }
            if ( t1 == T && t2 == T ) {
                result = V/(v1+v2);
            }
            else if ( t1 == T ) {
                result = V/v1;
            }
            else if ( t2 == T ) {
                result = V/v2;
            }
            else if ( t1 < T && t2 > T ) {
                double r1 = t2-T;
                double r2 = T-t1;
                if ( 1 ) {
                    double m = v1/r1;
                    r1 *= m;
                    r2 *= m;
                }
                if ( r2 > v2 ) {
                    double m = v2/r2;
                    r1 *= m;
                    r2 *= m;
                }
                result = V/(r1+r2);
            }
        }
        else {
            abort();
        }

        // output
        cout << "Case #"<<nc+1<<": ";
        if ( result < 0 )
            cout << "IMPOSSIBLE";
        else
            cout << fixed << setprecision(7) << result;
        cout << endl;
    }
    cin >> skip_eof;
}
