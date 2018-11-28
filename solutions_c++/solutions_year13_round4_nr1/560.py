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

const int N = 203, MOD = 1000002013;
int a[N], n, m, o, e, p;

LL nc2(LL x) { return x * (x + 1) / 2 % MOD; }

int main() {
    int T; scanf("%d", &T); FOE(ca, 1, T) {
        scanf("%d%d", &n, &m);
        CLR(a);
        LL orig = 0, best = 0;
        FOR(j, 0, m) {
            scanf("%d%d%d", &o, &e, &p);
            orig += nc2(e - o - 1) * p % MOD;
            orig %= MOD;
            FOR(k, o, e) {
                a[k] += p;
            }
        }
        
        while (true) {
            int s = 0;
            while (s < n && !a[s]) ++s;
            if (s == n) break;

            int mn = a[s], e = s;
            while (e < n && a[e]) {
                mn = min(mn, a[e]);
                ++e;
            }
            best += nc2(e - s - 1) * mn % MOD;
            best %= MOD;
            FOR(k, s, e) {
                a[k] -= mn;
            }
        }

        LL ans = (- orig + best) % MOD;
        ans += MOD;
        ans %= MOD;

        printf("Case #%d: %d\n", ca, (int)ans);
    }
    return 0;
}
