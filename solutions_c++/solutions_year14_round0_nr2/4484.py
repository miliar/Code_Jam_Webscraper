#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <complex>
#include <bitset>
#include <limits>
#include <vector>
#include <list>
#include <functional>
#include <deque>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <stack>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;

typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef pair<ll, ll> pll;

const int INF = (int) 1e9;
const ll LINF = (ll) 1e15;
const double PI = 2.0 * acos(0.0);
const double EPS = 1e-7;

#define pb push_back
#define mp make_pair

#define ZERO(x) memset(x,0,sizeof(x))
#define SET(x) memset(x,-1,sizeof(x))
#define SZ(x) (int)x.size()
#define REP(i,b) for(int i=0;i<b;++i)
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin() ;it!=(c).end();++it)
#define ALL(X) X.begin(),X.end()
#define RALL(X) X.rbegin(),X.rend()

int main() {
    int T;
    cin >> T;
    FOR(test, 1, T + 1) {
        double C, F, X;
        cin >> C >> F >> X;
        cout << "Case #" << test << ": ";
        
        /*
        FOR(i, 0, 20) {
            double ans = 0.0, curr = 2.0;
            int amt = i;
            while (amt--) {
                ans += C / curr;
                curr += F;
            }
            ans += X / curr;
            cout << ans << endl;
        }
        */
        int l = 0, r = 1000000;
        double ans = 1e15;
        REP(j, 300) {
            int lt = (2*l + r)/3;
            int rt = (l + 2*r)/3;
            double lamt = 0.0, ramt = 0.0, curr = 2.0;
            REP(i, lt) {
                lamt += C / curr;
                curr += F;
            }
            lamt += X / curr;
            curr = 2.0;
            REP(i, rt) {
                ramt += C / curr;
                curr += F;
            }
            ramt += X / curr;
            if (lamt + EPS < ramt) {
                r = rt;
            } else l = lt;
            ans = min(ans, lamt);
            ans = min(ans, ramt);
        }
        cout << setprecision(7) << fixed << ans << endl;
    }
    return 0;
}