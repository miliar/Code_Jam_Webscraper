#include <bits/stdc++.h>

#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,n) FOR(i,0,n)
#define ll long long
#define pii pair < int, int >
#define x first
#define y second
#define pb push_back

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

using namespace std;

void Solve(){

  ll k, c, s;
  cin >> k >> c >> s;

  if (s < (k+c-1)/c){cout << "IMPOSSIBLE\n"; return;}
  s = (k+c-1)/c;

  REP(i,s){
    ll tmp = 0;
    FOR(j,i*c,i*c+c) tmp = k * tmp + j%k;
    cout << tmp+1 << " ";
  } cout << endl;
  
}

int main(){
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  REP(i,t) cout << "Case #" << i+1 << ": ", Solve();

  return 0;
}
