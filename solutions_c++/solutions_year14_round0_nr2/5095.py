#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string.h>
#include <queue>
#include <cstdio>
#include <cassert>
#include <deque>
#include <stack>
#include <utility>
#include <numeric>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

void solve(int tc) {
    cout << "Case #" << tc << ": ";
    double c, f, x;
    cin >> c >> f >> x;
    double rate = 2.0;
    double have = 0.0;
    double ans = x / rate;
    double t = 0.0;
    while (t < ans) {
        ans = min(ans, t + (x - have) / rate);
        if (have < c) {
            t += (c - have) / rate;  
			have = c;
        }
        have -= c;
        rate += f;
    }
    cout.precision(10);
    cout << fixed;
    cout << ans << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    forn(i, tc) solve(i + 1);
    return 0;
}
