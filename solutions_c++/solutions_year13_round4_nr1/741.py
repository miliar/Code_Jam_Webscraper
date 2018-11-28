#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef vector<long long> vll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define mset(arr,val)  memset(arr,val,sizeof(arr))
#define tr(i,c)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define forr(var,from,to) for(int var=(from);var<=(to);var++) 
#define found(s,e)  ((s).find(e)!=(s).end())
#define remove_(c,val) (c).erase(remove((c).begin(),(c).end(),(val)),(c).end())
#define lastc(str) (*((str).end()-1))

// #include "cout.h"

typedef pair<ll,ll> LL;


inline ll f(ll x) { return (x * (x-1) / 2LL) % 1000002013LL; }

main(){
  int _T; cin>>_T;
  rep(_t,_T){
    ll N, M; cin>>N>>M;

    map<ll, set<LL> > chu; // o ep

    ll hon = 0;
    rep(m, M) {
      ll o,e,p; cin >> o>>e>>p;
      hon = (hon + p * f(e-o)) % 1000002013LL;
      chu[o].insert(LL(e,p));
    }
    // cout << chu << endl;

    priority_queue<LL> oq, eq; // o,p e,p

    ll dum = 0;
    tr(it, chu) {
      ll now = it->first;
      while (!eq.empty()) {
        ll ee = -eq.top().first, ep = eq.top().second;
        if (ee < now) {
          eq.pop();
          while (ep) {
            ll oo = oq.top().first, op = oq.top().second; oq.pop();
            ll u = min(ep, op); ep -= u;
            dum = (dum + u * f(ee-oo)) % 1000002013LL;
            if (op > u) {
              oq.push(LL(oo, op-u));
            }
          }
        } else break;
      }

      tr(jt, it->second) {
        ll e = jt->first, p = jt->second;
        oq.push(LL(now, p));
        eq.push(LL(-e, p));
      }
    }

    while (!eq.empty()) {
      ll ee = -eq.top().first, ep = eq.top().second;
      eq.pop();
      while (ep) {
        ll oo = oq.top().first, op = oq.top().second; oq.pop();
        ll u = min(ep, op); ep -= u;
        dum = (dum + u * f(ee-oo)) % 1000002013LL;
        if (op > u) {
          oq.push(LL(oo, op-u));
        }
      }
    }

    ll ans = (dum + 1000002013LL - hon) % 1000002013LL;
    printf("Case #%d: %lld\n", 1+_t, ans);
  }
}
