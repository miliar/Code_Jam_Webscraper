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
typedef unsigned u32; typedef int i32;
typedef long long i64; typedef unsigned long long u64;
typedef vector<int> VI; typedef vector<VI> VVI; typedef vector<string> VS;
typedef pair<int, int> P; typedef vector<P> VP; typedef vector<VP> VVP;

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

struct snum_less {
    bool operator()(const string& a, const string& b) const {
        if ( a.size() != b.size() ) return a.size() < b.size();
        return a < b;
    }
};

typedef set<string, snum_less> PP;
PP pp, pp0;

u64 rev(u64 n)
{
    char b[32];
    sprintf(b, "%llu", n);
    reverse(b, b+strlen(b));
    sscanf(b, "%llu", &n);
    return n;
}

inline bool is_p(const char b[], int L)
{
    for ( int i = 0, j = L-1; i < j; ++i, --j )
        if ( b[i] != b[j] ) return 0;
    return 1;
}

inline bool is_p(const char b[])
{
    return is_p(b, strlen(b));
}

inline bool is_p(const string& b)
{
    return is_p(b.data(), b.size());
}

void check_p(const string& n)
{
    //TR(n);
    assert(is_p(n));
    int L = n.size(), L2 = L*2-1;
    string n2(L2, '0');
    forN ( i, L ) {
        int v = n[i] - '0';
        if ( !v ) continue;
        forN ( j, L ) {
            int u = n[j] - '0';
            if ( !u ) continue;
            n2[i+j] += v*u;
            assert(n2[i+j] <= '9');
        }
    }
    assert(is_p(n2));
    pp.insert(n2);
    pp0.insert(n);
}

int main(int argc, const char** argv)
{
    NTR = 10000;
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    int part_cases = 0;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }

    check_p("1");
    check_p("2");
    check_p("3");
    forNF ( l, 1, 26 ) {
        // 1abba1 max 3 ones
        // 1ab0ba1 max 3 ones
        // 1ab1ba1 max 3 ones
        // 1ab2ba1 max 1 ones
        // 200002
        // 2000002
        // 2001002
        char b[64];
        forN ( k, 4 ) {
            if ( k > l-1 ) break;
            fill_n(b, l*2, '0');
            b[l*2] = 0;
            b[0] = '2'; b[l*2-1] = '2';
            check_p(b);
            b[0] = '1'; b[l*2-1] = '1';
            fill_n(b+l-k, k, '1');
            do {
                forN ( i, l ) b[l*2-1-i] = b[i];
                check_p(b);
            } while ( next_permutation(b+1, b+l) );
        }
        forN ( k, 4 ) {
            if ( k > l-1 ) break;
            fill_n(b, l*2+1, '0');
            b[l*2+1] = 0;
            b[0] = '2'; b[l*2] = '2';
            check_p(b);
            b[l] = '1';
            check_p(b);
            b[l] = '0';
            b[0] = '1'; b[l*2] = '1';
            fill_n(b+l-k, k, '1');
            do {
                forN ( i, l ) b[l*2-i] = b[i];
                check_p(b);
                b[l] = '1';
                check_p(b);
                if ( k <= 1 ) {
                    b[l] = '2';
                    check_p(b);
                }
                b[l] = '0';
            } while ( next_permutation(b+1, b+l) );
        }
    }
    TR(pp.size()|pp.rbegin()->size());
    //TR(pp);

    forN ( nc, num_cases ) {
        // parse input  
        string A, B;
        cin >> A >> B >> skip_endl;
        assert(!snum_less()(B, A));
        
        // error check
        if ( !cin ) { cout << "Error parsing input" << endl; return 1; }
        // main code

        TR(A|B);
        u64 ret = 0;
        for ( PP::iterator it = pp.lower_bound(A);
              it != pp.end() && !snum_less()(B, *it); ++it ) {
            TR(*it);
            ++ret;
        }


        // output
        cout << "Case #"<<nc+1<<": ";
        cout << ret;
        cout << endl;
    }
}
