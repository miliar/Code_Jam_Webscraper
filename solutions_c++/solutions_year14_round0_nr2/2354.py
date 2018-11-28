#include <cstdio>
#include <utility>
#include <iomanip>
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
typedef long double LD;
#define FOR(x, b, e) for(int (x)=(b); x<=(e); ++(x))
#define FORD(x, b, e) for(int (x)=(b); x>=(e); ––(x))
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

int main() {
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    FOR(z, 1, t) {
        LD C, F, X, prod = 2;
        cin >> C >> F >> X;
        LD tim = 0, best = X / prod;
        while (tim < best) {
            best = min(best, X / prod + tim);
            tim += C / prod;
            prod += F;
        }
        cout << "Case #" << z << ": " << setprecision(7) << fixed << best << endl;
    }
    return 0;
}
