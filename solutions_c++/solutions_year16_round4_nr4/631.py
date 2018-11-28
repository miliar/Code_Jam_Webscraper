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
typedef vector<int> vi; typedef vector<vector<int>> vvi; typedef vector<string> vs; typedef vector<double> vd;
typedef vector<vd> vvd; typedef long long ll; typedef vector<ll> vll; typedef vector<vll> vvll; typedef pair<int, int> pii;
#define all(v) begin(v), end(v)

#ifdef LOCAL
ifstream in("d.in");
#else
istream & in = cin;
#endif
//ostream & out = cout;
std::ofstream out("d.out");
template <class T> void read(T & t) { for (auto & x : t) in >> x; } template <class T> int sz(T const & t) { return (int)t.size(); }

int n;
vvi v;
int mask;
vi perm;
vi taken;

bool search(int pos) {
    if (pos == n)
        return true;
    int i = perm[pos];
    bool empty = true;
    for (int j = 0; j < n; ++j) {
        if (taken[j]) continue;
        if (!v[i][j] && !(mask & (1 << (n * i + j))))
            continue;
        empty = false;
        taken[j] = true;
        if (!search(pos + 1)) {
            taken[j] = false;
            return false;
        }
        taken[j] = false;
    }
    return !empty;
}

int main() {
    ios_base::sync_with_stdio(false);
    ios_base::sync_with_stdio(false);
    int ntests; in >> ntests;
    for (int test = 0; test < ntests; ++test) {
        in >> n;
        v.assign(n, vi(n));
        perm = taken = vi(n);
        for (int i = 0; i < n; ++i) {
            string str; in >> str;
            for (int j = 0; j < n; ++j)
                v[i][j] = str[j] == '1';
        }
        int res = n * n;
        for (mask = 0; mask < (1 << (n * n)); ++mask) {
            for (int i = 0; i < n; ++i) perm[i] = i;
            bool good = true;
            do {
                good = good && search(0);
                if (!good) break;
            } while (next_permutation(all(perm)));
            if (good) {
                int cnt = 0, m = mask;
                while (m) {
                    ++cnt; m = m & (m - 1);
                }
                res = min(res, cnt);
            }
        }
        out << "Case #" << test + 1 << ": " << res << "\n";
    }
    return 0;
}
