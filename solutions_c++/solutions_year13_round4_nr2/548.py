#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <iterator>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define REP(i,n)   FOR(i,0,n)
#define ALL(x) (x).begin(), (x).end()
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
#define ITER(v)      __typeof((v).begin())
#define FOREACH(i,v) for(ITER(v) i=(v).begin();i!=(v).end();i++)
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
#define x first
#define y second

int main() {
    int T; scanf("%d", &T); FOE(ca, 1, T) {
        LL n, p; scanf("%lld%lld", &n, &p); --p;
        LL mn = 0, mx = 0;
        LL k = (1LL<<n) - 1;
        if (k == p) {
            mn = mx = k;
        } else {
            LL m = (1LL<<n-1), lo = m, a = 2;
            while (m >= 1 && p >= lo) {
                mn += a;
                m /= 2;
                a *= 2;
                lo += m;
            }

            lo = 1;
            m = 2;
            a = (1LL<<n-1);
            while (a > 1 && p >= lo) {
                mx += a;
                lo += m;
                a /= 2;
                m *= 2;
            }
        }
        printf("Case #%d: %lld %lld\n", ca, mn, mx);
    }
}
