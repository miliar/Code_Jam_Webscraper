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
        int n;
        cin >> n;
        vector<double> nao, ken;
        nao.clear();
        ken.clear();
        REP(i, n) {
            double x;
            cin >> x;
            nao.PB(x);
        }
        REP(i, n) {
            double x;
            cin >> x;
            ken.PB(x);
        }
        sort(nao.begin(), nao.end());
        sort(ken.begin(), ken.end());
        //REP(i, n) cout << nao[i] << " "; cout << endl;
        //REP(i, n) cout << ken[i] << " "; cout << endl;

        vector<double> aux = ken;
        int pwar = n, pdec = n;
        for (int i = 0; i < n; i++) {
        //for (int i = n-1; i >=0; i--) {
            for (int j = 0; j < aux.size(); j++) {
                if (nao[i] < aux[j]) {
                    aux.erase(aux.begin() + j);
                    pwar--;
                    break;
                }
            }
        }
        int k = ken.size();
        REP(i, n) {
            if (nao[i] > ken[0]) {
                ken.erase(ken.begin());
            } else {
                ken.erase(ken.begin() + ken.size() - 1);
                pdec--;
            }
            k--;
        }
        cout << "Case #" << ttt+1 << ": " << pdec << " " << pwar << endl;
    }
    return 0;
}
