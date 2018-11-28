#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for(int i = 0; i < (int) (n); i++)
typedef pair<int, int> ii;

struct dot {
  int R, P, S;
  dot(int R = 0, int P = 0, int S = 0):R(R), P(P), S(S){}
};

bool operator == (dot a, dot b){
  return a.R == b.R &&
         a.P == b.P &&
         a.S == b.S;
}

int tc, n, r, p, s, TC;
dot init;
string ans;

dot transformar(dot a){ // el arreglo ans mide (1 << paso)
  int R, P, S;
  R = P = S = 0;
  
  string newAns;
  forn(i, ans.size()){
    if(ans[i] == 'R'){
      newAns += "RS";
    }
    else if(ans[i] == 'P'){
      newAns += "PR";
    }
    else {
      newAns += "PS";
    }
  }
  ans = newAns;

  R += a.R;
  P += a.P;
  S += a.S;
  
  S += a.R;
  R += a.P;
  P += a.S;
  
  return dot(R, P, S);
}

void solve(){
  
  int tam = ans.size();
  for(int sz = 2; sz < tam; sz *= 2){
    for(int pos = 0; pos < tam; pos += sz * 2){
      string v = ans.substr(pos, sz);
      string w = ans.substr(pos + sz, sz);
      //cout << "Comparando " << v << " y " << w << endl;
      if(w < v){
        forn(i, w.size()){
          ans[pos + i] = w[i];
        }
        forn(i, v.size()){
          ans[pos + sz + i] = v[i];
        }
      }
    }
  }
  
  printf("Case #%d: ", ++TC);
  cout << ans << endl;
}

int main(){
  freopen("input.in", "r", stdin);
  freopen("out.out", "w", stdout);
  
  scanf("%d", &tc);
  while(tc--){
    scanf("%d %d %d %d", &n, &r, &p, &s);
    dot x = dot(r, p, s);
    
    ans = "R";
    init = dot(1, 0, 0);
    forn(i, n){
      init = transformar(init);
    }
    if(init == x){
      // resolver aca...
      solve();
      continue;
    }
    
    ans = "P";
    init = dot(0, 1, 0);
    forn(i, n){
      init = transformar(init);
    }
    if(init == x){
      // resolver aca...
      solve();
      continue;
    }
    
    ans = "S";
    init = dot(0, 0, 1);
    forn(i, n){
      init = transformar(init);
    }
    if(init == x){
      // resolver aca
      solve();
      continue;
    }
    
    printf("Case #%d: IMPOSSIBLE\n", ++TC);
  }

  return 0;
}
