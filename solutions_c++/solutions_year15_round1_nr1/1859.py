#include <bits/stdc++.h>

using namespace std;

typedef long long          ll;
typedef vector<int>        vi;
typedef pair<int, int>     ii;
typedef vector<ii>         vii;
typedef set<int>           si;
typedef map<string, int>   msi;

int main() {
  int t, tc=0; scanf("%d", &t);

  while(t--) {
    ll n; scanf("%lld", &n);
    vector<ll> V(n);
    for(int i=0; i<n; i++) scanf("%lld", &V[i]);

    ll a = 0, b = 0, x=0;
    for(int i=1; i<n; i++) {
      if(V[i] < V[i-1]) {
	a += (V[i-1] - V[i]);
	x = max(x, V[i-1] - V[i]);
      }
    }

    for(int i=0; i<n-1; i++) {
      if(V[i] < x) b += V[i];
      else b += x;
    }

    printf("Case #%d: %lld %lld\n", ++tc, a, b);
  }

  return 0;
}
