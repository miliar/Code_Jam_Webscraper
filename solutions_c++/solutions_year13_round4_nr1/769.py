/* Author: Mahesh */

/* 1. Did you interpret the qns correctly ?
 2. Is your i/o correct ?
 3. Int overflow, double precision
 4. Array size correct ?
 5. Clearing/resetting vector, map etc.
 6. Stack ovrflow
 7. Global/local conflict
 8. Check for obvious typo(most imp)
 9. Think about edge cases
 */

#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <memory.h>
#include <cassert>

using namespace std;

#define ford(i, a, b, c)        for(int i=(a); i<(b); i+=(c))
#define fori(i, a, b)           ford(i,a,b,1)
#define rep(i, n)               fori(i,0,n)
#define ifor(i, a, b)           for(int i=(a); i>=(b); i--)
#define iter(i, a)              for(typeof((a).begin()) i=(a).begin(); i!=(a).end(); i++)
#define si(x)                   ((int)x.size())
#define SS                      ({int x;scanf("%d",&x);x;})
#define pb                      push_back
#define mp                      make_pair
#define all(a)                  a.begin(),a.end()
#define fill(a, v)              memset(a, v, sizeof(a))
#define inf                     (int)1e9
#define linf                    (long long)1e18
#define V                       vector
#define S                       string
#define XX                      first
#define YY                      second
#define P(v)                    rep(i, si(v)) cout<<v[i]<<" "; puts("")

typedef V<int> vi;
typedef V<S> vs;
typedef long long ll;
typedef pair<int,int> pii;

/* Program Body starts here */

V<pair<pii, ll>> v, tp;
map<ll, ll> m;
const int MOD = 1000002013;


V<pair<pii, ll>> filter(V<pair<pii, ll>> v) {
    tp.clear();
    rep(i, si(v)) {
      if (v[i].YY) {
        tp.pb(v[i]);
      }
    }
    return tp;
}

ll ff(ll N, ll x) {
    return (x*(2*N+1-x)/2)% MOD;
}
int main () {
    
    int T = SS;
    rep(_, T) {
        int N = SS, M = SS;
        set<ll> st;
        m.clear();
        st.clear();
        ll TL = 0;
        rep(i, M) {
            int s = SS, e = SS, p = SS;
            TL += (ll)p*ff(N, e-s) % MOD;
            st.insert(s);
            st.insert(e);
            m[s] += p;
            m[e] -= p;
        }
        ll last = -1, w = 0;
        v.clear();
        iter(i, st) {
            if (last != -1) {
                v.pb(mp(mp(last, *i), w));
            }
            
            w += m[*i];
            last = *i;
        }
        v = filter(v);
        
        ll ans = 0;
        while(si(v)) {
            int start = -1;
            rep(i, si(v)) {
                if (start == -1) {
                    start = i;
                }
                if (i== si(v) - 1 || v[i+1].XX.XX != v[i].XX.YY) {
                    ll mn = linf;
//                    cout<<start<<" "<<i+1<<endl;
                    fori(j, start, i+1) {
                        mn = min(mn, v[j].YY);
                    }
                    assert(mn > 0);
                    ans += mn*ff(N, v[i].XX.YY - v[start].XX.XX) % MOD;
                    ans %= MOD;
                    fori(j, start, i+1) {
                        v[j].YY -= mn;
                    }
                    start = -1;
                    
                }
            }
            v = filter(v);
        }

        ans = TL - ans;
        while(ans<0) ans+= MOD;
        printf("Case #%d: %lld\n", _+1, ans%MOD);
    }
    
}

