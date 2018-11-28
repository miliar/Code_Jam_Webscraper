//mishraiiit
#include<bits/stdc++.h>
#define ll long long int
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);
using namespace std;
typedef pair <ll, ll> pll;

#ifdef TRACE
  #include "trace.h"
#else
  #define trace1(x)
  #define trace2(x, y)
  #define trace3(x, y, z)
  #define trace4(a, b, c, d)
  #define trace5(a, b, c, d, e)
  #define trace6(a, b, c, d, e, f)
#endif

ll check(ll elem, ll limit) {
  if (elem > limit) return 1;
  return elem;
}

ll power(ll base, ll exp) { if(exp == 0) return 1LL; ll root = power(base, exp / 2); if(exp & 1LL) return (((root * root)) * base); return (root * root); }

ll doit(vector<ll> a, ll k, ll c) {
  ll ans = 1;
  for(int i = 1; i <= c; i++) {
    ans += (power(k, c - i) * (a[i - 1] - 1));
  }
  return ans;
}

vector<ll> solve(ll k, ll c) {
  vector<ll> ans;
  ll last = 0;
  while(last < k) {
    vector<ll> curr;
    for(int i = 0; i < c; i++) {
      curr.push_back(check(++last, k));
    }
    ans.push_back(doit(curr, k, c));
  }
  return ans;
}

int main() {
    fastScan;
    ll t;
    cin >> t;
    for(int i = 1; i <= t; i++) {
      cout << "Case #" << i <<": ";
      ll k, c, s;
      cin >> k >> c >> s;
      auto b = solve(k, c);
      if(b.size() <= s) {
        for(auto x : b) {
          cout << x << " ";
        }
      } else {
        cout << "IMPOSSIBLE";
      }
        cout << endl;
    }
    return 0;
}
