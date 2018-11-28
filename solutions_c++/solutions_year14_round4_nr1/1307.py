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
#define forIter(I,C) for(typeof((C).end()) I=(C).begin(); I!=(C).end(); ++I)
#define forNF(I,S,C) for(int I=(S); I<int(C); ++I)
#define forN(I,C) forNF(I,0,C)
#define forEach(I,C) forN(I,(C).size())
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef long long i64;
typedef unsigned long long u64;

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

const int INF = 999999999;
const int MAX_N = 99999;
const int MAX_L = 64;
int N, X;
int ff[MAX_N];

int num_cases = 1, part_cases = 0;
int main(int argc, const char** argv)
{
    cin >> num_cases >> skip_endl;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    forN ( nc, num_cases ) {
        cin >> N >> X >> skip_endl;
        forN ( i, N ) {
            cin >> ff[i];
        }
        cin >> skip_endl;

        // error check
        if ( !cin ) {
            cout << "Error parsing input" << endl;
            return 1;
        }
        // main code

        sort(ff,ff+N);

        int result = 0;

        int A = 0, B = N-1;
        while ( A < B ) {
            if ( ff[A]+ff[B] > X ) {
                ++result;
                --B;
            }
            else {
                ++result;
                ++A;
                --B;
            }
        }
        if ( A == B ) {
            ++result;
        }
        
        // output
        cout << "Case #"<<nc+1<<": "<<result;
        cout << endl;
    }
}
