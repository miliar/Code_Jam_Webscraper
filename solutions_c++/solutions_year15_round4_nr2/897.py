#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <unordered_set>
#endif

using namespace std;

#define ALL(x) (x).begin(), (x).end()
#define EACH(itr,c) for(__typeof((c).begin()) itr=(c).begin(); itr!=(c).end(); itr++)  
#define FOR(i,b,e) for (int i=(int)(b); i<(int)(e); i++)
#define MP(x,y) make_pair(x,y)
#define REP(i,n) for(int i=0; i<(int)(n); i++)

int N;
double V, X;
pair<double, double> s[128];

void solve() {

    cin >> N >> V >> X;
    REP (i, N) 
        cin >> s[i].first >> s[i].second;

    double tmax = -1e6;
    double tmin = +1e6;
    
    REP (i, N) {
        tmax = max(tmax, s[i].second);
        tmin = min(tmin, s[i].second);
    }

    if (X < tmin || tmax < X) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    if (N == 1) {
        cout << V / s[0].first << endl;
        return;
    }


    double a = s[0].second;
    double b = s[1].second;

    if (a == b) {
        cout << V / (s[0].first + s[1].first) << endl;
        return;
    }

    double x1 = (X - b) / (a - b) * V;
    double x2 = (a - X) / (a - b) * V;

    double t1 = x1 / s[0].first;
    double t2 = x2 / s[1].first;

    double ret = max(t1, t2);

    cout << fixed << setprecision(10) << ret << endl;
    
    
/*
    sort(s, s+N);

    double ret = 0;

    double curV = 0;
    double curX = 0;

    for (int i = N-1; i >= 0; i--) {
        
        if (i == 0) {
            throw;  
        }

        double lo = 0;
        double hi = V;

        REP (k, 1000) {
            double mid = (lo + hi) / 2;

            double nextX = (curV * curX + mid * s[i].second) / (curV + mid);
            
        }
        
        ret = max(ret, hi / s[i].first);
    }

    cout << ret << endl;
*/    
}

int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    REP (i, T) {
        cerr << "Case #" << i+1 << ": " << endl;
        cout << "Case #" << i+1 << ": ";
        solve();
    }

    return 0;
}
