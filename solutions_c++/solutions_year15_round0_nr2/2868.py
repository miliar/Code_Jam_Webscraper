#include <cstdio>
#include <utility>
#include <queue>
#include <set>
#include <list>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int (x)=(b); x<=(e); ++(x))
#define FORD(x, b, e) for(int (x)=(b); x>=(e); --(x))
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) __typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define PII pair<int, int>

bool is_ok(int k, const VI &P) {
    FOR(x, 1, k) {
        int y = 0;
        for (auto &&h : P) {
            if (h > x)
                y += (h - x) / x + !!((h - x) % x);
        }
        if (x + y <= k)
            return true;
    }
    return false;
}

int bins(int beg, int end, const VI &P) {
    if (beg == end)
        return beg;
    int sr = (beg + end) / 2;
    if (is_ok(sr, P))
        return bins(beg, sr, P);
    else
        return bins(sr + 1, end, P);
}

int main() {
    int t;
    cin >> t;
    FOR(z, 1, t) {
        int d;
        cin >> d;
        VI P(d);
        REP(i, d)
            cin >> P[i];
        cout << "Case #" << z << ": " << bins(1, 1000, P) << endl;
    }
    return 0;
}
