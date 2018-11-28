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

int main(){
  ios_base::sync_with_stdio(false);
 
  int n, j;
  cin >> n >> n >> j;
  cout << "Case #1:\n";

  REP(ttt,j){
    bitset < 100 > b;
    b[0] = b[n-1] = 1;
    REP(i,n/2-1) if ((ttt>>i)&1)
      b[2*i+1] = b[2*i+2] = 1;
    REP(i,n) cout << b[i]; cout << " ";
    FOR(i,2,11) cout << i+1 << " "; cout << endl;
  }
  
  return 0;
}
