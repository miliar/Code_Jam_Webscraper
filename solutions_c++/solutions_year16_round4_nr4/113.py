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

bool mat[30][30];
bool m2[30][30];
bool check(int n){

  vector < int > a;
  REP(i,n) a.pb(i);
  do {
    vector < int > b;
    REP(i,n) b.pb(i);
    do {
      REP(i,n) REP(j,n) m2[i][j] = mat[a[i]][b[j]];
      bool ch = true;
      REP(i,n) if (!m2[i][i]) ch = false;
      REP(i,n) REP(j,n) if (i != j && m2[i][j]){
	if (i < j) if (!m2[i+1][j] || !m2[i][j-1]) ch = false;
	if (i > j) if (!m2[i-1][j] || !m2[i][j+1]) ch = false;
	if (!m2[j][i]) ch = false;
      }
      vector < int > x(n, 0), y(n, 0);
      REP(i,n) REP(j,n) if (m2[i][j]) ++x[i], ++y[j];
      REP(i,n) REP(j,n) if (m2[i][j] && x[i] != y[j]) ch = false;
      if (ch) return true;
    } while (next_permutation(b.begin(), b.end()));
  } while (next_permutation(a.begin(), a.end()));
  return false;
  
}

int n;
string in[30];

bool good[5][1<<16];

void solve(){

  cin >> n;
  REP(i,n) cin >> in[i];
  int curr = 0;
  REP(i,n) REP(j,n) if (in[i][j] == '1') curr |= (1<<(i*n+j));

  int r = n*n;
  REP(i,1<<(n*n)) if (good[n][curr|i]){
    r = min(r, __builtin_popcount(i));
    //if (r == 5){cout << bitset<16>(curr) << endl; cout << bitset<16>(curr|i) << endl; exit(0);}
  }
  cout << r << endl;
  
}

int main(){

  FOR(nn,1,5) REP(i,1<<(nn*nn)){
    REP(a,nn) REP(b,nn) if ((i>>(a*nn+b))&1) mat[a][b] = true;
    else mat[a][b] = false;
    good[nn][i] = check(nn);
  }

  int t;
  cin >> t;
  REP(i,t) cout << "Case #" << i+1 << ": ", solve();

  return 0;
}
