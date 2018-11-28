#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <map>
#include <set>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>
#include <iterator>
#include <cstring>
#include <climits>
#include <cmath>
#include <cassert>

using namespace std;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,start,end) for (int var=(start); var<=(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(end); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) ((int)((x).size()))

// typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector< vector<int> > VVI;
typedef vector< vector<bool> > VVB;

int main() {
    cout << setprecision(7) << fixed;

    int nTests = 0; cin >> nTests;
    FOR (test, 1, nTests) {
        double c = 0.0;
        cin >> c;
        double f = 0.0;
        cin >> f;
        double x = 0.0;
        cin >> x;

        double cookiesPerSecond = 2.0;
        double curr = 0.0;
        int lo = 0;
        int hi = (int)ceil(x / c);
        double best = x / 2.0;
        FOR (nFarmsToBuy, lo, hi) {
            curr += c / cookiesPerSecond;
            cookiesPerSecond += f;
            best = min(best, curr +
                       (x / (2.0 + ((double)nFarmsToBuy + 1) * f)));
        }

        cout << "Case #" << test << ": " << best << "\n";
    }

    return 0;
}
