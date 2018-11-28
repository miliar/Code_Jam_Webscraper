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
    cin >> T;
    REP(ttt, T) {
        cout << "Case #" << ttt+1 << ": ";
        int n;
        uint32_t row[2] = { 0, 0 };
        REP(k, 2) {
            cin >> n;
            REP(i, 4) {
                REP(j, 4) {
                    int c;
                    cin >> c;
                    if (i + 1 == n) {
                        row[k] |= (1 << c);
                    }
                }
            }
        }
        uint32_t rep = row[0] & row[1];
        if (!rep) {
            cout << "Volunteer cheated!";
        } else {
            n = 0;
            int i = 0;
            while (rep) {
                if (rep & 1) {
                    if (!n) {
                        n = i;
                    } else {
                        n = 0;
                        cout << "Bad magician!";
                        break;
                    }
                }
                i++;
                rep /= 2;
            }
            if (n)
                cout << n;
        }
        cout << endl;
    }
    return 0;
}
