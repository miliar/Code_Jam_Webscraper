#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std;
 
#define FOREACH(i, c) for(__typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, a, n) for(__typeof(n) i = (a); i<(n); ++i)
#define REP(i, a, n) for(__typeof(n) i = (a); i<=(n); ++i)
#define ROF(i, n, a) for(__typeof(n) i = (n); i>=(a); --i)
#define error(n) cout << #n << " = " << n << endl
#define all(c) c.begin(), c.end()
#define pb push_back
#define po pop_back
#define Size(n) ((int)(n).size())
#define X first
#define Y second
int _ ;
#define scanf _ = scanf
// #define X real()
// #define Y imag()

typedef long long   ll ;
typedef long double ld ;
typedef pair<int,int> pii ;

const int maxn = 201 * 1000;

double c , f, x;

int main() {
    int T;
    cout << fixed << setprecision(7) ;
    cin >> T;
    REP (lv,1,T) {
        cin >> c >> f >> x;
        int m = x/f;
        m += 4;
        double sum = 0.0, rate = 2.0;
        double ans = x/2.0+1;
        for (int i = 0 ; ; ++i) {
            if (sum+x/rate < ans) {
                ans = sum+x/rate;
            } else {
//                 if (i > x/f)
//                 cerr << i << endl;
                break;
            }
            //
            sum += c/rate;
            rate += f;
        }
        cout << "Case #" << lv << ": " << ans << endl;
    }
    return 0 ;
}
