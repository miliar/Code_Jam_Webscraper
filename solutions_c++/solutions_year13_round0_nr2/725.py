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
#define rep(var,n)  for(int var=0;var<(n);var++)

int N, M;
vector<vector<int> > a;

int solve() {
  int mx=0;
  rep(n,N) rep(m,M) {
    mx = max(mx, a[n][m]);
  }

  for(int lv=1; lv<=mx; ++lv){
    vector<bool> cn(N,false), cm(M,false);
    rep(n,N){
      bool ok=true;
      rep(m,M) if (a[n][m]!=lv) { ok=false; break; }
      cn[n] = ok;
    }
    rep(m,M){
      bool ok=true;
      rep(n,N) if (a[n][m]!=lv) { ok=false; break; }
      cm[m] = ok;
    }

    rep(n,N){
      rep(m,M){
        if (a[n][m] == lv) {
          if (cn[n] || cm[m]) continue;
          return 0;
        }
      }
    }

    rep(n,N) rep(m,M) {
      if (a[n][m] == lv) ++a[n][m];
    }
  }
  return 1;
}

main(){
  int _T; cin>>_T;
  rep(_t,_T){
    cin >> N >> M;
    a.resize(N);
    rep(i,N){
      a[i].resize(M);
      rep(j,M){
        cin >> a[i][j];
      }
    }

    printf("Case #%d: %s\n", 1+_t, solve() ? "YES":"NO");
  }
}
