#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <iomanip>
#include <functional>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;


typedef long long lint, ll;
typedef long double ldouble, ld;

#ifdef LOCAL
	#define dbg(expr) cerr << "[" << __LINE__ << "] " << #expr << " = " << (expr) << '\n';
#else
	#define dbg(expr) (void) 0;
#endif


void apply(int ind, string & s, int k) {
    for (int i = ind; i < ind + k; i++) {
        if (s[i] == '-')
            s[i] = '+';
        else
            s[i] = '-';
    }
}

bool check(const string & s) {
    for (auto c : s) {
        if (c == '-')
            return false;
    }
    return true;
}

void solve(int test_case) {
    string s;
    int k;
    cin >> s >> k;
    int n = s.length();
    int q = 0;
    for (int i = 0; i < n - k + 1; i++) {
        if (s[i] == '-') {
            apply(i, s, k);
            q++;
        }
    }
    cout << "Case #" << test_case + 1 << ": ";
    if (check(s))
        cout << q << endl;
    else
        cout << "IMPOSSIBLE" << endl;
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
        solve(i);
}
