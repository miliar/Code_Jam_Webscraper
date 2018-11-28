#include <bits/stdc++.h>

#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define x first
#define y second

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

using namespace std;

typedef long long ll;
typedef pair < int, int > pii;

string str(int p, int r, int s){
  if (p+r+s == 1){
    if (p) return "P";
    if (r) return "R";
    if (s) return "S";
    assert(false);
  }

  string A, B;
  if (p == r) A = str(p/2, r/2+1, s/2), B = str(p/2+1, r/2, s/2);
  if (p == s) A = str(p/2, r/2, s/2+1), B = str(p/2+1, r/2, s/2);
  if (r == s) A = str(p/2, r/2+1, s/2), B = str(p/2, r/2, s/2+1);
  if (A+B < B+A) return A+B;
  else return B+A;
}

int n, r, p, s;

void solve(){

  cin >> n >> r >> p >> s;
  int nn = (1<<n);
  if (p < nn/3 || r < nn/3 || s < nn/3){cout << "IMPOSSIBLE\n"; return;}
  if (p > nn/3+1 || r > nn/3+1 || s > nn/3+1){cout << "IMPOSSIBLE\n"; return;}
  cout << str(p, r, s) << endl;
  
}

int main(){

  int t;
  cin >> t;
  REP(i,t) cout << "Case #" << i+1 << ": ", solve();

  return 0;
}
