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
void input_error(const string& m = string()) {
    cerr << "Input failed at line " << line_number << ": " << m << endl; exit(1);
}
void check_space(const string& s) { for ( auto c : s ) assert(isspace(c&255)); }
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

string S;

string get(const string& S)
{
    if ( S.empty() ) return S;
    
    char c = *max_element(ALL(S));
    size_t p = S.find(c);
    string a, b;
    for ( size_t i = p; i < S.size(); ++i ) {
        if ( S[i] == c )
            a += c;
        else
            b += S[i];
    }
    return a + get(S.substr(0, p)) + b;
}

int num_cases = 1, part_cases = 0;
int main(int argc, const char** argv)
{
    cin >> num_cases >> skip_endl;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    forN ( nc, num_cases ) {
        cin >> S >> skip_endl;

        // error check
        if ( !cin ) input_error();
        // main code

        string result = get(S);
        
        // output
        cout << "Case #"<<nc+1<<": ";
        cout << result;
        cout << endl;
    }
    cin >> skip_eof;
}
