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
#define forIter(I,C) for(typeof((C).end()) I=(C).begin(); I!=(C).end(); ++I)
#define forNF(I,S,C) for(int I=(S); I<int(C); ++I)
#define forN(I,C) forNF(I,0,C)
#define forEach(I,C) forN(I,(C).size())
typedef long long i64; typedef unsigned long long u64;
typedef vector<int> VI; typedef vector<VI> VVI; typedef vector<string> VS;

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

/////////////////////////////////////////////////////////////////////////////

const int MAX_N = 128;
const int MAX_M = 1024;
int M, N;
string ss[MAX_M];

struct P {
    const char* ptr;
    int size;
};
ostream& operator<<(ostream& out, P p)
{
    return out.write(p.ptr, p.size);
}
inline
bool operator<(const P& a, const P& b)
{
    if ( a.size != b.size )
        return a.size < b.size;
    return memcmp(a.ptr, b.ptr, a.size) < 0;
}

map<P, int> tt[MAX_N];
int max_size;
i64 max_count;

void go(int k)
{
    if ( !k ) {
        int size = 0;
        forN ( i, N ) {
            size += tt[i].size();
            TR(tt[i]);
        }
        if ( size > max_size ) {
            max_size = size;
            max_count = 0;
        }
        if ( size == max_size ) {
            max_count += 1;
        }
        return;
    }
    P p;
    p.ptr = ss[--k].data();
    int size = ss[k].size();
    forN ( i, N ) {
        forN ( j, size+1 ) {
            p.size = j;
            ++tt[i][p];
        }
        go(k);
        forN ( j, size+1 ) {
            p.size = j;
            if ( --tt[i][p] == 0 ) {
                tt[i].erase(p);
            }
        }
    }
}

int main(int argc, const char** argv)
{
    NTR = 100;
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    int part_cases = 0;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    
    forN ( nc, num_cases ) {
        // parse input
        cin >> M >> N >> skip_endl;
        forN ( i, M ) {
            cin >> ss[i] >> skip_endl;
        }

        // error check
        if ( !cin ) {
            cout << "Error parsing input" << endl;
            return 1;
        }
        // main code

        forN ( i, N ) tt[i].clear();
        max_size = 0;
        max_count = 0;
        go(M);
        
        // output
        cout << "Case #"<<nc+1<<": "<<max_size<<" "<<max_count;
        cout << endl;
    }
}
