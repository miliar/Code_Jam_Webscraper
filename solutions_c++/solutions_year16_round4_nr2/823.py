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
using namespace std;
typedef vector<int> vi; typedef vector<vector<int>> vvi; typedef vector<string> vs; typedef vector<double> vd;
typedef vector<vd> vvd; typedef long long ll; typedef vector<ll> vll; typedef vector<vll> vvll; typedef pair<int, int> pii;
#define all(v) begin(v), end(v)

#ifdef LOCAL
ifstream in("b.in");
#else
istream & in = cin;
#endif
//ostream & out = cout;
std::ofstream out("b.out");
template <class T> void read(T & t) { for (auto & x : t) in >> x; } template <class T> int sz(T const & t) { return (int)t.size(); }

int main() {
    ios_base::sync_with_stdio(false);
    int ntests; in >> ntests;
    for (int test = 0; test < ntests; ++test) {
        int n, k; in >> n >> k;
        vector<double> v(n);
        read(v);
        double res = 0;
        for (int i = 0; i < (1 << n); ++i) {
            int cnt = 0;
            for (int j = 0; j < n; ++j) if (i & (1 << j)) ++cnt;
            if (cnt != k) continue;
            vvd pr(n, vd(k + 1));
            if (i & 1) {
                pr[0][0] = 1 - v[0];
                pr[0][1] = v[0];
            } else 
                pr[0][0] = 1;
            for (int j = 1; j < n; ++j) {
                if (i & (1 << j)) {
                    for (int l = 0; l <= k; ++l) {
                        if (l)
                            pr[j][l] += pr[j-1][l-1] * v[j];
                        pr[j][l] += pr[j-1][l] * (1 - v[j]);
                    }
                } else {
                    pr[j] = pr[j-1];
                }
            }
            res = max(res, pr[n-1][k/2]);
        }
        out.precision(10);
        out.setf(ios::fixed);
        out << "Case #" << test + 1 << ": " << res << "\n";
    }
    return 0;
}
