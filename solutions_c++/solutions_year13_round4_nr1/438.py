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
ofstream out("a.out");

ll mod = 1000002013;

ll pay(ll n, ll len) {
    return (n * (n+1) / 2 - (n-len)*(n-len+1) / 2) % mod;
}

int main() {
    int ntests;
    in >> ntests;    
    for (int test = 1; test <= ntests; ++test) {
        int n, m;
        in >> n >> m;
        vector<pii> v;
        ll city = 0;
        for (int i = 0; i < m; ++i) {
            int o, e, p;
            in >> o >> e >> p;
            v.push_back(make_pair(o, -p));
            v.push_back(make_pair(e, p));
            city = (city + pay(n, e - o) * p) % mod;
        }
        sort(all(v));
        vector<pii> s;
        ll total = 0;
        for (int i = 0; i < v.size(); ++i) {
            if (v[i].second < 0) {
                s.push_back(make_pair(v[i].first, -v[i].second));
            } else {
                int left = v[i].second;
                while (left) {
                    int x = min(left, s.back().second);
                    left -= x; s.back().second -= x;
                    total = (total + pay(n, v[i].first - s.back().first) * x) % mod;
                    if (!s.back().second)
                        s.pop_back();
                }
            }
        }
        out << "Case #" << test << ": " << (city - total + mod) % mod << "\n";
    }
    return 0;
}