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
#define pb  push_back
#define rep(var,n)  for(int var=0;var<(n);var++)
#define all(c)  (c).begin(),(c).end()

bool palin(ll x) {
  ll x_=x, y=0LL;
  while (x_) {
    y *= 10LL;
    y += (x_ % 10LL);
    x_ /= 10LL;
  }
  return (y == x);
}

main(){
  vector<ll> palins;

  palins.pb(0);
  for (ll i=1; i<10000000LL; ++i) {
    if (!palin(i)) continue;
    ll x = i*i;
    if (palin(x)) palins.pb(x);
  }
  palins.pb(LONG_LONG_MAX);

  int _T; cin>>_T;
  rep(_t,_T){
    ll A, B; cin >> A >> B;
    int ans = (int)(upper_bound(all(palins), B) - lower_bound(all(palins), A));
    printf("Case #%d: %d\n", 1+_t, ans);
  }
}
