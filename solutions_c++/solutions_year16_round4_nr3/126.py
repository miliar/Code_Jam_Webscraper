#include <cstdio>
#include <vector>
#include <cassert>
#include <string>
#include <utility>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;

vector<ll> as_start(ll R, ll C, ll p) {
  if(p < C) {
    return {0, p, 0};
  } else if(p < C+R) {
    return {p-C, C-1, 1};
  } else if(p < C+R+C) {
    return {R-1, (C-1)-(p-(C+R)), 2};
  } else {
    assert(p < C+R+C+R);
    return {(R-1)-(p-(C+R+C)), 0, 3};
  }
}
vector<ll> as_end(ll R, ll C, ll p) {
  if(p < C) {
    return {-1, p, 2};
  } else if(p < C+R) {
    return {p-C, C, 3};
  } else if(p < C+R+C) {
    return {R, (C-1)-(p-(C+R)), 0};
  } else {
    assert(p < C+R+C+R);
    return {(R-1)-(p-(C+R+C)), -1, 1};
  }
}
vector<ll> move(vector<vector<int>> M, vector<ll> in) {
  ll r = in[0];
  ll c = in[1];
  ll d = in[2];
  if(M[r][c]) {
    if(d == 0) {
      return {r, c-1, 1};
    } else if(d==1) {
      return {r+1, c, 0};
    } else if(d==2) {
      return {r, c+1, 3};
    } else {
      assert(d==3);
      return {r-1, c, 2};
    }
  } else {
    if(d==0) {
      return {r, c+1, 3};
    } else if(d==1) {
      return {r-1, c, 2};
    } else if(d==2) {
      return {r, c-1, 1};
    } else {
      assert(d==3);
      return {r+1, c, 0};
    }
  }
}
vector<ll> dest(vector<vector<int>> M, vector<ll> in) {
  in = move(M, in);
  while(0 <= in[0] && in[0] < M.size() && 0<=in[1] && in[1]<M[0].size()) {
    in = move(M, in);
  }
  return in;
}
bool ok(vector<vector<int>> M, vector<ll> P) {
  bool bad = false;
  for(ll i=0; i<P.size(); i+=2) {
    vector<ll> st = as_start(M.size(), M[0].size(), P[i]);
    vector<ll> ed = as_end(M.size(), M[0].size(), P[i+1]);
    //printf("P[%lld]=%lld -> (%lld %lld %lld)\n", i, P[i], st[0], st[1], st[2]);
    //printf("P[%lld]=%lld -> (%lld %lld %lld)\n", i+1, P[i+1], ed[0], ed[1], ed[2]);
    vector<ll> st_dest = dest(M, st);
    if(st_dest[0] != ed[0] || st_dest[1] != ed[1] || st_dest[2] != ed[2]) {
      bad = true;
    }
  }
  return !bad;
}

bool bit_set(ll set, ll bit) {
  return ((set>>bit)&1)==1;
}

int main() {
  ll T;
  scanf("%lld", &T);
  for(ll cas=1; cas<=T; cas++) {
    printf("Case #%lld:\n", cas);
    bool possible = false;

    ll R, C;
    scanf("%lld %lld", &R, &C);
    vector<ll> P(2*(R+C), 0);
    for(ll i=0; i<2*(R+C); i++) {
      scanf("%lld", &P[i]);
      P[i]--;
    }
    for(ll a=0; a<(1<<(R*C)); a++) {
      if(!possible) {
        vector<vector<int>> M(R, vector<int>(C, 0));
        for(ll r=0; r<R; r++) {
          for(ll c=0; c<C; c++) {
            M[r][c] = bit_set(a, r*C+c);
          }
        }
        if(ok(M, P)) {
          for(ll r=0; r<R; r++) {
            for(ll c=0; c<C; c++) {
              printf("%s", M[r][c] ? "/" : "\\");
            }
            printf("\n");
          }
          possible = true;
        }
      }
    }
    if(!possible) {
      printf("IMPOSSIBLE\n");
    }
  }
}
