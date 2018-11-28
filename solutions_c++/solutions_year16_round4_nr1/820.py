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
#pragma warning(disable : 4244 4267 4018 4996 4800)
//#pragma comment( linker, "/stack:10000000" )
using namespace std; 
typedef vector<int> vi; typedef vector<vi> vvi; typedef vector<string> vs; typedef vector<double> vd;
typedef vector<vd> vvd; typedef long long ll; typedef vector<ll> vll; typedef vector<vll> vvll; typedef pair<int, int> pii;
#define all(v) begin(v), end(v)

#ifdef LOCAL
ifstream in( "a.in" );
#else
istream & in = cin;
#endif
//ostream & out = cout;
std::ofstream out("a.out");
template <class T> void read(T & t) { for (auto & x : t) in >> x; } template <class T> int sz(T const & t) { return (int)t.size(); }

int order[6][3] = {{0, 1, 2}, {0, 2, 1}, {2, 0, 1}, {2, 1, 0}, {1, 2, 0}, {1, 0, 2}};

int mmin(int a, int b, int k) {
    k = k % 6;
    for (int i = 0; i < 3; ++i) {
        if (order[k][i] == a) return a;
        if (order[k][i] == b) return b;
    }
}

int mmax(int a, int b, int k) {
    k = k % 6;
    for (int i = 0; i < 3; ++i) {
        if (order[k][i] == a) return b;
        if (order[k][i] == b) return a;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int ntests; in >> ntests;
    vvi v;
    v.resize(13);
    v[0].resize(1);
    for (int i = 1; i < v.size(); ++i) {
        v[i].resize(v[i-1].size() * 2);
    }    
    for (int test = 0; test < ntests; ++test) {
        int n, r, p, s;
        in >> n >> r >> p >> s;
        bool found = false;        
        for (int i = 0; i < 3; ++i) {
            v[0][0] = i;
            for (int j = 1; j <= n; ++j) {
                for (int k = 0; k < v[j].size(); k += 2) {
                    int prev = v[j-1][k / 2];
                    int l, r;
                    if (prev == 0) {       
                        l = 0, r = 1;
                    } else if (prev == 2) {
                        l = 0, r = 2;
                    } else {
                        l = 1, r = 2;
                    }
                    v[j][k] = mmin(l, r, n - j);
                    v[j][k + 1] = mmax(l, r, n - j);
                }
            }
            if (count(all(v[n]), 0) == p && count(all(v[n]), 1) == r) {
                found = true; break;
            }
        }
        out << "Case #" << test + 1 << ": ";
        if (!found)
            out << "IMPOSSIBLE\n";
        else {
            for (int i = 0; i < v[n].size(); ++i) {
                if (v[n][i] == 0) out << 'P';
                else if (v[n][i] == 1) out << 'R';
                else out << 'S';
            }
            out << "\n";
        }
    }
    return 0;
}
