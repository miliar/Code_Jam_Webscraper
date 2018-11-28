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


/////////////////////////////////////////////////////////////////////////////

const int INF = 999999999;

size_t N;
VI ww[200];
size_t K;
vector<pair<int, int>> cc;

void set_lang(const VI& ww, int l)
{
    if ( l ) {
        for ( auto w : ww ) {
            cc[w].second += 1;
        }
    }
    else {
        for ( auto w : ww ) {
            cc[w].first += 1;
        }
    }
}

void reset_lang(const VI& ww, int l)
{
    if ( l ) {
        for ( auto w : ww ) {
            cc[w].second -= 1;
        }
    }
    else {
        for ( auto w : ww ) {
            cc[w].first -= 1;
        }
    }
}

void read_ww(VI& ww)
{
    ww.clear();
    istringstream ss(get_str(cin));
    string s;
    while ( ss >> s ) {
        ww.push_back(get_index(s));
    }
    ss.clear();
}

int num_cases = 1, part_cases = 0;
int main(int argc, const char** argv)
{
    cin >> num_cases >> skip_endl;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    forN ( nc, num_cases ) {
        // parse input
        cin >> N >> skip_endl;
        str_index.clear();
        forN ( i, N ) {
            read_ww(ww[i]);
        }
        //cin >> skip_endl;
        
        // error check
        if ( !cin ) input_error();
        // main code

        K = str_index.size();
        size_t result = K;
        
        cc.assign(K, make_pair(0, 0));
        set_lang(ww[0], 0);
        set_lang(ww[1], 1);
        forN ( bb, (1<<(N-2)) ) {
            forNF ( i, 2, N ) {
                set_lang(ww[i], (bb>>(i-2))&1);
            }
            size_t c = 0;
            for ( auto& b : cc ) {
                if ( b.first && b.second ) ++c;
            }
            result = min(result, c);
            forNF ( i, 2, N ) {
                reset_lang(ww[i], (bb>>(i-2))&1);
            }
        }
    
        // output
        cout << "Case #"<<nc+1<<": " << result;
        cout << endl;
    }
    cin >> skip_eof;
}
