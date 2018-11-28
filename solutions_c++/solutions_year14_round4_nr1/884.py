#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int solve() {
    int n, X;
    cin >> n >> X;
    multiset<int> S;
    for (int i=0; i<n; ++i) {
        int sz;
        cin >> sz;
        S.insert(sz);
    }
    int sol = 0;
    while (S.size() > 1) {
        auto p = S.begin();
        auto t = p;
        ++t;
        if (*p + *t > X) {
            break;
        }
        t = S.upper_bound(X-*p);
        --t;
        if (t == p) {
            break;
        }
        assert(*t + *p <= X);
        S.erase(t);
        S.erase(p);
        ++sol;
    }
    sol += S.size();
    return sol;
}

int main() {
    int T;
    cin >> T;
    cerr << T << " cases total\n";
    for (int t=1; t<=T; ++t) {
        int sol = solve();
        cout << "Case #" << t << ": " << sol << '\n';
        cerr << "Case #" << t << ": " << sol << '\n';
    }
	return 0;
}
