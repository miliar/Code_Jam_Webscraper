#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#pragma warning( disable : 4244 4267 4018 4996 4800 )
//#pragma comment( linker, "/stack:10000000" )
using namespace std; 
typedef vector< int > vi; typedef vector< vector< int > > vvi; typedef vector< string > vs; typedef vector< double > vd;
typedef vector< vd > vvd; typedef long long ll; typedef vector< ll > vll; typedef vector< vll > vvll; typedef pair< int, int > pii;
#define all( v ) (v).begin( ), (v).end( )

#ifdef LOCAL
ifstream in( "b.in" );
#else
istream & in = cin;
#endif
//ostream & out = cout;
ofstream out( "b.out" );

int main() {
    int ntests;
    in >> ntests;
    for (int test = 1; test <= ntests; ++test) {
        int n;
        in >> n;
        vi v(n);
        for (int i = 0; i < n; ++i)
            in >> v[i];
        vi w = v;
        sort(all(w));
        int res = 0;
        for (int i = 0; i < n; ++i) {
            int idx = find(all(v), w[i]) - v.begin();
            int l = 0, r = 0;
            for (int j = 0; j < n; ++j) {
                if (v[j] <= w[i]) continue;
                if (j < idx) ++l;
                else ++r;
            }
            res += min(l, r);
        }
        out << "Case #" << test << ": " << res << "\n";
    }
    return 0;
}