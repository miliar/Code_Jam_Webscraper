#include <cstdio>
#include <vector>
#include <cassert>

using namespace std;

typedef long long ll;
typedef double ld;

bool bit_set(ll set, ll bit) {
  return ((set>>bit)&1)==1;
}
ll bit_add(ll set, ll bit) {
  return set | (1<<bit);
}

bool ok(vector<vector<int>> M, ll left, ll rU, ll cU) {
  if(left == 0) { return true; }
  bool had_good = false;
  bool had_bad = false;
  for(ll r=0; r<M.size(); r++) {
    for(ll c=0; c<M[r].size(); c++) {
      if(!bit_set(rU, r) && !bit_set(cU, c) && M[r][c]) {
        bool result = ok(M, left-1, bit_add(rU, r), bit_add(cU, c));
        if(result) {
          had_good = true;
        } else {
          had_bad = true;
        }
      }
    }
  }
  return (had_good && !had_bad);
}


int main() {
  ll T;
  scanf("%lld", &T);
  for(ll cas=1; cas<=T; cas++) {
    ll n;
    scanf("%lld", &n);
    vector<vector<int>> M(n, vector<int>(n, false));
    for(ll i=0; i<n; i++) {
      char buf[n+1];
      scanf("%s", buf);
      for(ll j=0; j<n; j++) {
        M[i][j] = (buf[j]=='1');
      }
    }

    ll best = n*n;
    for(ll a=0; a<(1<<(n*n)); a++) {
      vector<vector<int>> M2(n, vector<int>(n, 0));
      for(ll r=0; r<n; r++) {
        for(ll c=0; c<n; c++) {
          M2[r][c] = bit_set(a, r*n+c);
        }
      }
      bool bad = false;
      ll cost = 0;
      for(ll r=0; r<n; r++) {
        for(ll c=0; c<n; c++) {
          if(M[r][c] && !M2[r][c]) { bad=true; }
          if(!M[r][c] && M2[r][c]) { cost++; }
        }
      }
      if(!bad && cost < best && ok(M2, n, 0, 0)) {
        /*
        for(ll r=0; r<n; r++) {
          for(ll c=0; c<n; c++) {
            printf("%d", M2[r][c]);
          }
          printf("\n");
        }
        */
        best = cost;
      }
    }
    printf("Case #%lld: %lld\n", cas, best);
  }
}
