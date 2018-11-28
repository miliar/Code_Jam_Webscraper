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

ll solve(ll n) {
  ll nums[10];
  for(int i = 0; i < 10; i++) nums[i] = 0;
  ll start = 1;
  while(1) {
    ll curr = start * n;
    while(curr) {
      nums[curr % 10]++;
      curr = curr / 10;
    }
    bool allDone = true;
    for(int i = 0; i < 10; i++) allDone = allDone && (nums[i] >= 1);
    if(allDone) break;
    start++;
  }
  return start * n;
}


int main() {
    fastScan;

    ll t;
    cin >> t;

    for(int i = 1; i <= t; i++) {
      ll n; cin >> n;
      if(n == 0) cout << "Case #" << i << ": " << "INSOMNIA" << endl;
      else cout << "Case #" << i << ": " << solve(n) << endl;
    }

    return 0;
}
