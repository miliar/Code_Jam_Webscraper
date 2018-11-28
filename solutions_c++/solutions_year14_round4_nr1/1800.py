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
#define scanf _ = scanf
// #define X real()
// #define Y imag()

typedef long long   ll ;
typedef long double ld ;
typedef pair<int,int> pii ;

const int maxn = 1111;

bool is[maxn];
int n,x,s[maxn];

int main() {
    int T;
    cin >> T;
    REP (lv,1,T) {
        cin >> n >> x;
        FOR (i,0,n)
            cin >> s[i];
        sort (s,s+n);
        memset (is,false,sizeof(is));
        int ans = 0;
        ROF (i,n-1,0) {
            int ptr = -1;
            if (is[i]) continue;
            FOR (j,0,i) {
                if (s[i]+s[j] <= x) { 
                    if (!is[j])
                        ptr = j;
                } else
                    break;
            }
            if (ptr != -1) {
                is[ptr] = true;
            }
            ++ans;
        }
        cout << "Case #" << lv << ": " << ans << endl;
    }
    return 0 ;
}
