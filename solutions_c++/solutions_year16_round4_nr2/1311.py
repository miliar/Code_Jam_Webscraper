
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
#include <sstream>

using namespace std;

#define ford(i, a, b, c)        for(int i=(a); i<(b); i+=(c))
#define fori(i, a, b)           ford(i,a,b,1)
#define rep(i, n)               fori(i,0,n)
#define ifor(i, a, b)           for(int i=(a); i>=(b); i--)
#define iter(i, a)              for(typeof(a.begin()) i=(a).begin(); i!=(a).end(); i++)
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



double a[2000];

int n, k;

double solve(int mask) {
    V<double> v;
    rep(i, n) {
        if (mask & (1<<i)) {
            v.pb(a[i]);
        }
    }
    double ans = 0;
    rep(i, 1<<k) {
        if (__builtin_popcount(i) == k/2) {
            double p = 1;
            rep(j, k) {
                if (i&(1<<j)) {
                    p*=v[j];
                } else {
                    p*=(1-v[j]);
                }
            }
            ans += p;
        }
    }
    return ans;
}

int main() {
    freopen("/Users/mahesh/Desktop/codejam/codejam/in.txt", "r", stdin);
    freopen("/Users/mahesh/Desktop/codejam/codejam/out.txt", "w", stdout);
    int t = SS;
    rep(_, t) {
        n = SS; k = SS;
        rep(i, n){
            scanf("%lf", &a[i]);
        }
        double ans = 0.0;
        rep(i, 1<<n) {
            if (__builtin_popcount(i) == k) {
                ans = max(ans, solve(i));
            }
        }
        printf("Case #%d: %.9lf\n", _+1, ans);
    }
}






