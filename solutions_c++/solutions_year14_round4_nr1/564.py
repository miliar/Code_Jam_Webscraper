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
ifstream in( "a.in" );
#else
istream & in = cin;
#endif
ofstream out( "a.out" );
//ostream & out = cout;

int main() {
    int ntests;
    in >> ntests;
    for (int test = 1; test <= ntests; ++test) {
        int n, x;
        in >> n >> x;
        multiset<int> v;
        for (int i = 0; i < n; ++i) {
            int t;
            in >> t;
            v.insert(t);
        }
        int res = 0;
        while (!v.empty()) {
            ++res;
            auto it = v.end();
            --it;
            int a = *it;
            v.erase(it);
            if (v.empty())
                break;
            auto it2 = v.lower_bound(x - a);
            if (it2 == v.end() || *it2 > x - a) {
                if (it2 == v.begin())
                    continue;
                --it2;
            }
            v.erase(it2);
        }
        out << "Case #" << test << ": " << res << "\n";
    }
    return 0;
}