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
#include <gmpxx.h>
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

inline u64 get_cost(u32 N, u32 d)
{
    return u64(2*N+1-d)*d/2;
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
        u32 N, M;
        cin >> N >> M >> skip_endl;
        map<u32, int> dd;
        u64 result = 0;
        forN ( i, M ) {
            u32 s, d, c;
            cin >> s >> d >> c;
            dd[s] += c;
            dd[d] -= c;
            result += c*get_cost(N, d-s);
        }
        assert(cin);

        while ( !dd.empty() ) {
            typeof(dd.begin()) it = dd.begin();
            u32 s = it->first;
            u32 c = it->second;
            u32 f = c;
            do {
                f = min(f, c);
                ++it;
                c += it->second;
            } while ( c );
            u32 d = it->first;
            result -= f*get_cost(N, d-s);
            if ( (dd[s] -= f) == 0 ) {
                dd.erase(s);
            }
            if ( (dd[d] += f) == 0 ) {
                dd.erase(d);
            }
        }

        // output
        cout << "Case #"<<nc+1<<": ";
        cout << result;
        cout << endl;
    }
}
