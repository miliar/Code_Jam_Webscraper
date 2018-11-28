#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <inttypes.h>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define ST first
#define ND second
#define MP make_pair
#define PB push_back
#define POP pop_back

typedef long long LL;
typedef long double LD;
typedef double D;
typedef pair<int, int> PII;
typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<PII> VII;
typedef vector<VI> VVI;
typedef map<int, int> MII;
typedef map<int, VI > MIVI;
typedef vector<pair<int, VI > > VPIVI;

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
#define ZERO(x) memset(x,0,sizeof(x))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(a,b) ((a)>(b)?(a-b):(b-a))

#define MAXN 500

int main ()
{

    int T;
    scanf("%d", &T);
    // cin >> T;
    // std::cout.precision(10);

    REP(ttt, T) {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        // cin >> c >> f >> x;
        double ttime = 0;
        double r0 = 2;
        while (1) {
            double t0 = x/r0;
            double r1 = r0 + f;
            double t1 = c/r0 + x/r1;
            //cout << t0 << " ? " << t1 << " = ";
            if (t0 > t1) {
                ttime += c/r0;
                //cout << c/r0 << " / " << ttime << endl;
                r0 = r1;
            } else {
                ttime += t0;
                //cout << t0 << endl;
                break;
            }
        }
        printf("Case #%d: %.7lf\n", ttt+1, ttime);
        //cout << "Case #" << ttt+1 << ": " << ttime << endl;
    }
    return 0;
}
