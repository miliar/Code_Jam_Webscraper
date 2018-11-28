#include <bitset>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#define repi(i, a, b) for(int i = (a); i < (int)(b); i++)
#define rep(i, a) repi(i, 0, a)
#define repd(i, a, b) for(int i = (a); i >= (int)(b); i--)
#define repit(i, v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define reprit(i, v) for(__typeof((v).rbegin()) i = (v).rbegin(); i != (v).rend(); i++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define uniq(v) (v).erase(unique(all(v)), (v).end())
#define pb push_back
#define mp make_pair

using namespace std;
typedef long long ll;

const int MAX = 128;
char f[MAX][MAX];
string ds = "^>v<";
const int di[] = {-1, 0, 1, 0};
const int dj[] = { 0, 1, 0,-1};
int r, c;
bool inrange(int i, int j) { return i >= 0 and j >= 0 and i < r and j < c; }

bool reach(int i, int j, int k) {
  i += di[k]; j += dj[k];
  while(inrange(i, j) and f[i][j] == '.') {
    i += di[k];
    j += dj[k];
  }
  if(!inrange(i, j)) return false;
  return true;
}
const long inf = 10000000000LL;
long partial(int i, int j) {
  int dir = 0;
  rep(k, 4) if(ds[k] == f[i][j]) {
    dir = k;
    break;
  }
  
  if(reach(i, j, dir)) return 0;
  rep(k, 4) 
    if(reach(i, j, k)) {
      //cout << i << " " << j << " " << k << endl;
      return 1;
    }
  return inf;
}

void solve() {
  cin >> r >> c;
  rep(i, r) rep(j, c) cin >> f[i][j];

  bool ok = true;
  rep(i, r) rep(j, c) if(f[i][j] != '.') ok = false;
  if(ok) {
    cout << 0 << endl;
    return;
  }
  
  long ans = 0;
  rep(i, r) rep(j, c) if(f[i][j] != '.') {
    ans += partial(i, j);
  }

  if(ans < inf) 
    cout << ans << endl;
  else
    cout << "IMPOSSIBLE" << endl;
}

int main() {
  int T;
  cin >> T;
  rep(t, T) {
    cout << "Case #" << t+1 << ": ";
    solve();
  }
  
  return 0;
}
