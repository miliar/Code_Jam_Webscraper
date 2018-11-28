#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;

pair<LL, LL> Solve() {
    int n;
    LL p;
    cin >> n >> p;

    pair<LL, LL> ans(-1, -1);

    LL lb = 0;
    for (int i = 0; i <= n; ++i) {
        LL what = (1LL << i) - 1;
        LL cnt = (i == 0 ? 1 : (1LL << (n - i)));
        LL ub = lb + cnt - 1;

        if (what < p) {
            ans.second = max(ans.second, ub);
        }
        if ((1LL << n) - 1 - what < p) {
            ans.first = max(ans.first, (1LL << n) - 1 - lb);
        }
        lb = ub + 1;
    }

    return ans;
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int nTests;
    cin >> nTests;

    for (int test = 0; test < nTests; ++test) {
        pair<LL, LL> ans = Solve();
        cout << "Case #" << test + 1 << ": " << ans.first << ' ' << ans.second << '\n';
    }

    return 0;
}
