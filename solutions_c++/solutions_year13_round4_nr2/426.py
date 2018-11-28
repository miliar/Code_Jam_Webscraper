#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <fstream>
#include <functional>
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
ofstream out("b.out");

template < class T > T pow( T v, int n ) {
    T res = 1;
    for ( ; n; n >>= 1, v = v * v )
        if ( n & 1 ) res = res * v;
    return res;
}

template <class T>
ll binary_search(ll l, ll r, T func) {
    while (l < r - 1) {
        ll m = (l + r) / 2;
        if (func(m))
            l = m;
        else
            r = m;
    }
    return l;
}

ll best_place(ll i, ll n)
{
    if (i == n - 1) return n - 1;
    ll left = (n - i) / 2;
    return best_place(n / 2 - left, n / 2);
}

ll worst_place(ll i, ll n)
{
    if (i == 0) return 0;
    ll left = (i - 1) / 2;
    return n / 2 + worst_place(left, n / 2);
}

int main() {
    int ntests;
    in >> ntests;
    for (int test = 1; test <= ntests; ++test) {
        int n, p;
        in >> n >> p;
        ll l = 0, r = pow<ll>(2, n);
        ll x = binary_search(l, r, [=](ll i) { return worst_place(i, r) < p; });
        ll y = binary_search(l, r, [=](ll i) { return best_place(i, r) < p; });
        out << "Case #" << test << ": " << x << " " << y << "\n";
    }
    return 0;
}