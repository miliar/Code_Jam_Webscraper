#include <cstdio>
#include <vector>
#include <cassert>
#include <string>
#include <algorithm>
#include <utility>
#include <stack>
#include <cmath>

using namespace std;

typedef long long ll;
typedef double ld;
typedef pair<ld, pair<ll, ll>> pdll;

vector<ll> UF;
ll find(ll x) {
  if(UF[x]==x) { return x; }
  else {
    return UF[x] = find(UF[x]);
  }
}
void mix(ll x, ll y) {
  UF[find(x)] = find(y);
}

int main() {
  ll T;
  scanf("%lld", &T);
  for(ll cas=1; cas<=T; cas++) {
    ll n, s;
    scanf("%lld %lld", &n, &s);
    vector<vector<ll>> A;
    for(ll i=0; i<n; i++) {
      ll x, y, z, vx, vy, vz;
      scanf("%lld %lld %lld %lld %lld %lld", &x, &y, &z, &vx, &vy, &vz);
      A.push_back({x, y, z, vx, vy, vz});
    }
    UF = vector<ll>(n, 0);
    for(ll i=0; i<n; i++) {
      UF[i]=i;
    }

    vector<pdll> E;
    for(ll i=0; i<n; i++) {
      for(ll j=i+1; j<n; j++) {
        ld dx = A[i][0]-A[j][0];
        ld dy = A[i][1]-A[j][1];
        ld dz = A[i][2]-A[j][2];
        ld d = sqrt(dx*dx + dy*dy + dz*dz);
        E.push_back(make_pair(d, make_pair(i, j)));
      }
    }
    sort(E.begin(), E.end());
    for(pdll e : E) {
      ld d = e.first;
      ll x = e.second.first;
      ll y = e.second.second;
      mix(x, y);
      if(find(0) == find(1)) {
        printf("Case #%lld: %.9f\n", cas, d);
        break;
      }
    }
  }
}
