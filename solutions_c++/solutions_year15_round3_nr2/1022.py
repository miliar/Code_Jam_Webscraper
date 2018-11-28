
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
#define iter(i, a)              for(auto i=(a).begin(); i!=(a).end(); i++)
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

int k, l, s;
vi res;
S keys;
S pattern;

int ff(string str) {
    int ans = 0;
    rep(i, s-l+1) {
        ans += str.substr(i, l) == pattern;
    }
    return ans;
}
void solve(string a) {
    if (si(a) == s){
        res.pb(ff(a));
        return;
    }
    rep(i, k) {
        solve(a+keys[i]);
    }
}

int main() {
    freopen("/Users/mahesh/Desktop/Codejam/Codejam/test.txt", "r", stdin);
    freopen("/Users/mahesh/Desktop/Codejam/Codejam/out.txt", "w", stdout);
    int Cases = SS;
    rep(Case, Cases) {
        res.clear();
        k = SS; l = SS; s = SS;
        cin>>keys;
        cin>>pattern;        solve("");
        int mx = 0;
        double sum = 0;
        rep(i, si(res)){
             mx = max(mx, res[i]);

            sum += res[i];
        }
        double ans = mx - (double)sum/si(res);
        cout<<"Case #" << Case+1 << ": ";
        printf("%.9lf\n", ans);
    }
}



