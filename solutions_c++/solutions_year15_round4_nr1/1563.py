#include<bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false);cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;
#define rep(i,a,b) for(int (i)=(a);(i)<(b);(i)++)
#define repd(i,a,b) for(int (i)=(b)-1;(i)>=(a);(i)--)
#define REP(i,n) rep(i,0,n)
#define REPD(i,n) repd(i,0,n)
#define pb push_back
#define mp make_pair
#define countbits(x) __builtin_popcount(x)
#define countbitslld(x) __builtin_popcountll(x)

typedef long long int lld;
typedef vector<int> vi;
typedef vector<lld> vlld;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

bool valid(int x, int n){
  if(0 <= x and x < n) return true;
  return false;
}

int main(){ IO;
  int t;
  cin >> t;

  rep(ncase,1,t+1){
    cout << "Case #" << ncase << ": ";

    int r, c;
    cin >> r >> c;

    vector<string> grid(r);
    REP(i,r) cin >> grid[i];

    int di[] = {-1, 0, 1, 0};
    int dj[] = { 0, 1, 0,-1};

    int ans = 0;
    bool impossible = false;

    REP(i,r) REP(j,c) if(grid[i][j] != '.'){
      bool good = false;
      int d;
      if(grid[i][j] == '^') d = 0;
      else if(grid[i][j] == '>') d = 1;
      else if(grid[i][j] == 'v') d = 2;
      else if(grid[i][j] == '<') d = 3;

      int cnt = false;
      REP(dir,4){
        rep(k,1,max(r,c)){
          int ii = i + k * di[dir];
          int jj = j + k * dj[dir];
          if(valid(ii, r) and valid(jj, c) and grid[ii][jj] != '.'){
            good = true;
	    if(d == dir) cnt++;
          }

          // if(dir == d and (!valid(ii, r) or !valid(jj, c))){
	  //   count = true;
          // }
        }
      }

    out:
      if(good == false) impossible = true;
      if(cnt == 0) ans++;
    }
    
    if(impossible) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
  }

  return 0;
}
