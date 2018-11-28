#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <time.h>
#include <cctype>
#include <functional>
#include <deque>
#include <iomanip>
#include <bitset>
#include <assert.h>
#include <numeric>
#include <sstream>
#include <utility>

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(a) (a).begin(),(a).end()
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define FORD(i,a,b) for (int i=(a); i>=(b); i--)
#define REP(i,b) FOR(i,0,b)
#define ll long long
#define sf scanf
#define pf printf
#define Maxn 1111
using namespace std;
const int maxint = -1u>>1;
const double pi = 3.14159265358979323;
const double eps = 1e-8;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<int>::iterator vit;

const ll mod = 1000002013LL;
int n, m;
ll sum, ans;
struct Tnode {
    int s, t, p;
    bool operator<(const Tnode&b) const {
        return t < b.t;
    }
}d[Maxn*20];
ll cnt[Maxn*3];
int b[Maxn*3], tot;
ll calc(int o, int e, ll ss) {
    if (o == e) return 0;
    ll ret = e - o;
    ret = (ret * (n + n + 1 - ret)) / 2;
    ret %= mod;
    ret = (ret * ss) % mod;
    return ret;
}
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, ca = 0;
    sf("%d", &T);
    while (T--) {
        sum = 0;
        tot = 0;
        sf("%d%d", &n, &m);
        REP(i, m) {
            sf("%d%d%d", &d[i].s, &d[i].t, &d[i].p);
            b[tot++] = d[i].s;
            b[tot++] = d[i].t;
            if (d[i].s != d[i].t) {
                ll x = d[i].t - d[i].s;
                ll tmp = 1LL * x * (n + (n + 1 - x)) / 2;
                sum += (tmp % mod) * d[i].p % mod;
                sum %= mod;
            }
        }
        //cout <<sum <<" "<<ans <<endl;
        ans = 0;
        sort(d, d+m);
        sort(b, b+tot);
        tot = unique(b, b+tot) - b;
        memset(cnt, 0, sizeof(cnt));
        REP(i, m) {
            cnt[lower_bound(b, b+tot, d[i].s) - b] += d[i].p;
        }
            //REP(j, tot) cout <<cnt[j] <<" ";
            //cout <<endl;
        REP(i, m) {
            int r = lower_bound(b, b+tot, d[i].t) - b;
            int l = lower_bound(b, b+tot, d[i].s) - b;
            ll num = d[i].p;
            //cnt[l] -= d[i].p;
            for (int j = r; j >= 0 && num; j--) {
                ans += calc(b[j], b[r], min(num, cnt[j]));
                ans %= mod;
                //cout <<" calc " <<b[j] <<" "<<b[r] <<" "<<min(num, cnt[j]) <<endl;
                //cnt[r] += min(num, cnt[j]);
                ll tmp = min(num, cnt[j]);
                cnt[j] -= tmp;
                num -= tmp;
            }
            //cout <<ans << " --- " <<num <<" "<<r <<endl;
            if (num) {
                ans += calc(d[i].s, d[i].t, num);
                cnt[l] -= num;
                ans %= mod;
            }
            //REP(j, tot) cout <<cnt[j] <<" ";
            //cout <<endl;
        }
        //cout <<sum <<" "<<ans <<endl;
        ans = (sum - ans + mod) % mod;
        pf("Case #%d: %d\n", ++ca, ans);
    }
    return 0;
}

