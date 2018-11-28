// P < R < S
// P = 0
// R = 1
// S = 2

#include <cstdio>
#include <vector>
#include <cassert>
#include <string>

using namespace std;

typedef long long ll;

ll lose(ll x) {
  if(x==0) { return 1; }
  if(x==1) { return 2; }
  if(x==2) { return 0; }
  assert(false);
  return -1;
}

int main() {
  vector<vector<vector<ll>>> C(12+1, vector<vector<ll>>(3, vector<ll>(3, 0)));
  C[0][0][0] = 1;
  C[0][1][1] = 1;
  C[0][2][2] = 1;
  for(ll n=1; n<C.size(); n++) {
    for(ll i=0; i<3; i++) {
      for(ll j=0; j<3; j++) {
        C[n][i][j] = C[n-1][i][j] + C[n-1][lose(i)][j];
      }
    }
  }
  for(ll n=1; n<C.size(); n++) {
    for(ll i=0; i<3; i++) {
      for(ll j=0; j<i; j++) {
        assert(C[n][i][0] != C[n][j][0] || C[n][i][1] != C[n][j][1] || C[n][i][2] != C[n][j][2]);
      }
    }
  }
  vector<vector<string>> B(C.size(), {"", "", ""});
  B[0][0] = "P";
  B[0][1] = "R";
  B[0][2] = "S";
  for(ll n=1; n<B.size(); n++) {
    for(ll i=0; i<3; i++) {
      string s1 = B[n-1][i] + B[n-1][lose(i)];
      string s2 = B[n-1][lose(i)] + B[n-1][i];
      B[n][i] = min(s1, s2);
//      printf("B[%lld][%lld] = %s\n", n, i, B[n][i].c_str());
    }
  }

  ll T;
  scanf("%lld", &T);
  for(ll cas=1; cas<=T; cas++) {
    ll n, p, r, s;
    scanf("%lld %lld %lld %lld", &n, &r, &p, &s);
    string best = "Z";
    for(ll w=0; w<3; w++) {
      if(p == C[n][w][0] && r==C[n][w][1] && s==C[n][w][2]) {
        best = min(best, B[n][w]);
      }
    }
    if(best == "Z") {
      printf("Case #%lld: IMPOSSIBLE\n", cas);
    } else {
      printf("Case #%lld: %s\n", cas, best.c_str());
    }
  }
}
