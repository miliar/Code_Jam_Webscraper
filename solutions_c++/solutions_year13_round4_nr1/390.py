#ifdef SHTRIX 
#include "/Users/roman/Dev/SharedCpp/DebugOutput.h"
#endif
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <memory>
using namespace std;
#define pb push_back
#define INF 1000000000
#define L(s) (int)((s).end()-(s).begin())
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define C(a) memset((a),0,sizeof(a))
#define ll long long
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define VI vector<int>
#define ppb pop_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
//#define x first
//#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pi 3.1415926535897932384626433832795028841971
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())

const int MOD = 1000002013;

struct seg {
    int l, r, p;
    seg(){}
    seg(int l, int r, int p) : l(l), r(r), p(p) {}
    bool isin(int x) {
        return l <= x && x <= r;
    }
};

inline ll f(ll n, ll d) {
    return (ll)n * d - (ll)(d - 1) * d / 2; 
}

VI w;

int get(int x) {
    return lower_bound(all(w), x) - w.begin();
}

inline void solve(int case_id) {
    w.clear();
    cerr << case_id << endl;
    int ans = 0, tot = 0, n, m;
    scanf("%d%d", &n, &m);
    vector<seg> v(m);
    rept(i, m)
        scanf("%d%d%d", &v[i].l, &v[i].r, &v[i].p), v[i].l--, v[i].r--;
    rept(i, m) {
        w.pb(v[i].l);
        w.pb(v[i].r);
    }
    UN(w);
    ll d[3111];
    C(d);
    rept(i, L(v)) {
        for (int j = get(v[i].l); j < get(v[i].r); j++)
            d[j] += v[i].p;
        tot = (tot + (ll)(f(n, v[i].r - v[i].l) % MOD) * (ll)v[i].p) % MOD;
    }
    rept(i, L(w) - 1) {
        while (d[i] > 0) {
            int j = i;
            for (; j < L(w) - 1; j++) {
                if (d[j] == 0) break;
            }
            ll mn = d[i];
            for (int k = i; k < j; k++)
                mn = min(mn, d[k]);
            for (int k = i; k < j; k++)
                d[k] -= mn;
            ans = (ans + (ll)mn * (f(n, w[j] - w[i]) % MOD)) % MOD;
        }
    }
    ans = ((ll)tot - ans + MOD) % MOD;
    printf("Case #%d: %d\n", case_id, ans);
}

int main()
{
    freopen("input.txt","rt",stdin);
	int TC; scanf("%d", &TC); rep(tc, TC) solve(tc);
    return 0;
}
