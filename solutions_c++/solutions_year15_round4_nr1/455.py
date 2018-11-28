#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <stack>
#include <assert.h>
#include <unordered_map>
#include <iomanip>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define mplus(x, y) ((x) == -1 || (y) == -1) ? -1 : ((x) + (y))
#define mmax(x, y) ((x) == -1 || (y) == -1) ? -1 : max((x), (y))
#define mmin(x, y) ((x) == -1) ? (y) : ((y) == -1) ? (x) : min((x), (y))
#define checkbit(n, k) (((1L << (k)) & (n)) != 0)

#define debug(x) cerr << '>' << #x << ':' << x << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;

int f(int n, int m, vector<string> table) {
    vector<vector<bool> > ok_now(n, vector<bool>(m));
    vector<vector<bool> > can_be_ok(n, vector<bool>(m));
    for (int i = 0; i < n; ++i) {
        bool ok = false;
        for (int j = 0; j < m; ++j) {
            if (table[i][j] == '.') {
                ok_now[i][j] = can_be_ok[i][j] = true;
            } else {
                if (ok) {
                    can_be_ok[i][j] = true;
                    if (table[i][j] == '<')
                        ok_now[i][j] = true;
                }
                ok = true;
            }
        }
        ok = false;
        for (int j = m - 1; j >= 0; --j) {
            if (table[i][j] == '.') {
                ok_now[i][j] = can_be_ok[i][j] = true;
            } else {
                if (ok) {
                    can_be_ok[i][j] = true;
                    if (table[i][j] == '>')
                        ok_now[i][j] = true;
                }
                ok = true;
            }
        }
    }
    for (int j = 0; j < m; ++j) {
        bool ok = false;
        for (int i = 0; i < n; ++i) {
            if (table[i][j] == '.') {
                ok_now[i][j] = can_be_ok[i][j] = true;
            } else {
                if (ok) {
                    can_be_ok[i][j] = true;
                    if (table[i][j] == '^')
                        ok_now[i][j] = true;
                }
                ok = true;
            }
        }
        ok = false;
        for (int i = n - 1; i >= 0; --i) {
            if (table[i][j] == '.') {
                ok_now[i][j] = can_be_ok[i][j] = true;
            } else {
                if (ok) {
                    can_be_ok[i][j] = true;
                    if (table[i][j] == 'v')
                        ok_now[i][j] = true;
                }
                ok = true;
            }
        }
    }
    int res = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            // debug(i);
            // debug(j);
            // debug(can_be_ok[i][j]);
            // debug(ok_now[i][j]);
            if (!can_be_ok[i][j])
                return -1;
            if (!ok_now[i][j])
                ++res;
        }
    }
    return res;
}


int main() {
    int T;
    cin >> T;
    for (int tt = 1; tt <= T; ++tt) {
        // debug(tt);
        int64 n, m;
        cin >> n >> m;
        vector<string> strings(n);
        for (int i = 0; i < n; ++i)
            cin >> strings[i];
        int64 res = f(n, m, strings);
        if (res >= 0)
            cout << "Case #" << tt << ": " << res << endl;
        else
            cout << "Case #" << tt << ": " << "IMPOSSIBLE" << endl;
    }
}
