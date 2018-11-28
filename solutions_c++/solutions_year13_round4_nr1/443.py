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

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define debug(x) cout << '>' << #x << ':' << x << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;

// bool bit(int64 mask, int k) {
//     return ((1LL << k) & mask) != 0;
// }

const int64 MOD = 1000002013;
int64 win(int64 o, int64 e) {
    int64 n = e - o;
    return (n * (n - 1) / 2) % MOD;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testCount;
    cin >> testCount;
    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        int64 n, m;
        cin >> n >> m;
        vector< pair<pair<int64, int64>, int64> > pass;
        vector< pair<int64, int64> > stops;
        int64 initWin = 0;
        for (int i = 0; i < m; ++i) {
            int64 o, e, p;
            cin >> o >> e >> p;
            pass.push_back(make_pair(make_pair(o, e), p));
            initWin += (p * win(o, e)) % MOD;
            initWin %= MOD;

            stops.push_back(make_pair(o, -p));
            stops.push_back(make_pair(e, p));
        }

        sort(stops.begin(), stops.end());
        stack< pair<int64, int64> > origins;
        
        int64 best_win = 0;
        for (int i = 0; i < stops.size(); ++i) {
            pair<int64, int64> stop = stops[i];
            // cerr << stop.first << " " << stop.second << endl;
            int64 p = stop.second;
            if (p < 0) {
                int64 o = stop.first;
                origins.push(make_pair(o, -p)); 
            } else {
                int64 e = stop.first;
                while (p > 0) {
                    pair<int64, int64> last = origins.top();
                    origins.pop();
                    int64 o = last.first;
                    int64 p1 = last.second;
                    int64 p2 = min(p, p1);
                    best_win += (p2 * win(o, e)) % MOD;
                    best_win %= MOD;
                    // cerr << o << " " << e << " " << best_win << endl;
                    p -= p2;
                    p1 -= p2;
                    if (p1 > 0) {
                        origins.push(make_pair(o, p1));
                    }
                }
            }
        }
        // cerr << initWin << endl;
        // cerr << best_win << endl;
        assert(origins.empty());
        int64 res = best_win + MOD - initWin;
        res %= MOD;
        
        cout << "Case #" << testNumber << ": " << res << endl;
    }

    return 0;
}