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
const double EPS = 1e-8;

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
        int fc, sc, count = 0, ans;
        cin >> fc;
        vector<int> ra;
        FOR(i, 1, 5) {
            FOR(j, 1, 5) {
                int a;
                cin >> a;
                if (i == fc) ra.push_back(a);
            }
        }
        cin >> sc;
        FOR(i, 1, 5) {
            FOR(j, 1, 5) {
                int b;
                cin >> b;
                if (i == sc && find(ALL(ra), b) != ra.end()) {
                    ++count;
                    ans = b;
                }
            }
        }
        cout << "Case #" << test << ": ";
        if (count == 1) cout << ans << endl;
        else if (count > 1) cout << "Bad magician!" << endl;
        else cout << "Volunteer cheated!" << endl;
    }
    return 0;
}