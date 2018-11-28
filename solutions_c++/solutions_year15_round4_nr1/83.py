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
#include <cstring>
#include <sstream>
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
typedef vector<int> VI; typedef vector<VI> VVI; typedef vector<string> VS;
typedef long long i64; typedef unsigned long long u64;

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

const int INF = 999999999;

size_t I, J;
VS bb;
bool hit(size_t i, size_t j, char c)
{
    int di = 0, dj = 0;
    switch ( c ) {
    case '^': di = -1; break;
    case 'v': di =  1; break;
    case '<': dj = -1; break;
    case '>': dj =  1; break;
    default: abort();
    }
    for ( ;; ) {
        i += di;
        j += dj;
        if ( i >= I || j >= J ) return 0;
        if ( bb[i][j] != '.' ) return 1;
    }
}

int num_cases = 1, part_cases = 0;
int main(int argc, const char** argv)
{
    cin >> num_cases >> skip_endl;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    forN ( nc, num_cases ) {
        cin >> I >> J >> skip_endl;
        bb.resize(I);
        forN ( i, I ) {
            cin >> bb[i] >> skip_endl;
            assert(bb[i].size() == J);
        }

        // error check
        if ( !cin ) input_error();
        // main code

        int result = 0;
        forN ( i, I ) forN ( j, J ) {
            if ( bb[i][j] == '.' ) continue;
            if ( hit(i, j, bb[i][j]) ) continue;
            bool can_hit = false;
            forN ( d, 4 ) {
                if ( hit(i, j, "v^<>"[d]) ) {
                    can_hit = true;
                    break;
                }
            }
            if ( can_hit ) {
                ++result;
            }
            else {
                result = -1;
                break;
            }
        }
        
        // output
        cout << "Case #"<<nc+1<<": ";
        if ( result >= 0 ) cout << result; else cout << "IMPOSSIBLE";
        cout << endl;
    }
    cin >> skip_eof;
}
