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
ifstream in( "c.in" );
#else
istream & in = cin;
#endif
ofstream out("c.out");

int test;
int n;
vi a, b, elem, rev, len;

int incrsub(vi& elem, int idx) {
    for (int i = 0; i <= idx; ++i) if (elem[i] != -1) {
        len[i] = 0;
        for (int j = 0; j < i; ++j) if (elem[j] != -1 && elem[j] < elem[i]) {
            len[i] = max(len[i], len[j] + 1);
        }
    }
    return len[idx] + 1;
}

bool solve(int idx) {
    if (idx == n)
        return true;
    for (int i = 0; i < n; ++i) if (elem[i] == -1) {
        elem[i] = idx;
        rev[n-i-1] = idx;
        if (a[i] == incrsub(elem, i) && b[i] == incrsub(rev, n - i - 1)) {
            if (solve(idx + 1))
                return true;
        }
        elem[i] = -1;
        rev[n-i-1] = -1;
    }
    return false;
}

int main() {
    int ntests;
    in >> ntests;
    for (int test = 1; test <= ntests; ++test) {
        in >> n;
        a = vi(n); b = vi(n); len = vi(n);
        for (int i = 0; i < n; ++i) in >> a[i];
        for (int i = 0; i < n; ++i) in >> b[i];
        elem = rev = vi(n, -1);
        solve(0);
        out << "Case #" << test << ": ";
        for (auto i : elem)
            out << i + 1 << " ";
        out << "\n";
    }
    return 0;
}