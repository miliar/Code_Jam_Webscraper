#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define RREP(i,s,e) for (i = s; i >= e; i--)
#define rrep(i,n) RREP(i,n,0)
#define REP(i,s,e) for (i = s; i < e; i++)
#define rep(i,n) REP(i,0,n)
#define INF 100000000

typedef long long ll;

int main() {
    int i, t;
    cin >> t;
    rep (i,t) {
        int k, c, s, x, y;
        cin >> k >> c >> s;
        cout << "Case #" << i+1 << ": ";
        if (k-c+1-s > 0) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        x = 0;
        while (x < k) {
            ll pos = x++;
            for (y = 0; x < k && y < c-1; y++) {
                pos *= k;
                pos += x++;
            }
            cout << pos+1 << " ";
        }
        cout << endl;
    }
    return 0;
}
