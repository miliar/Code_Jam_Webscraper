#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <vector>
using namespace std;

#define REP2(i, m, n) for(int i = (int)(m); i < (int)(n); i++)
#define REP(i, n) REP2(i, 0, n)
#define ALL(c) (c).begin(), (c).end()
#define FOREACH(i, c) for(auto i = (c).begin(); i != (c).end(); ++i)
#define BIT(n, m) (((n) >> (m)) & 1)

typedef long long ll;

const ll inf = 1e15;
const ll mod = 1000 * 1000 * 1000 + 7;
const double eps = 1e-9;

int P, Q, N;
int H[300];
int G[300];
ll memo[110][210][1010][2];

ll calc(int pos, int h, int shot, bool turn){
  
    
  if (pos == N) return 0;
  if (memo[pos][h][shot][turn] != -1) return memo[pos][h][shot][turn];
  
  ll &res = memo[pos][h][shot][turn] = 0;
  
  if (turn == 0){
    if (h <= Q){
      res = calc(pos + 1, H[pos + 1], shot, !turn);
    } else {
      res = calc(pos, h - Q, shot, !turn);
    }
  } else {
    // shoot from stock
    if (shot > 0){
      if (h <= P){
        res = max(res, calc(pos + 1, H[pos + 1], shot - 1, turn) + G[pos]);
      } else {
        res = max(res, calc(pos, h - P, shot - 1, turn));
      }
    }
    
    // normally shoot
    {
      if (h <= P){
        res = max(res, calc(pos + 1, H[pos + 1], shot, !turn) + G[pos]);
      } else {
        res = max(res, calc(pos, h - P, shot, !turn));
      }
    }

    if (shot < 1005){
      res = max(res, calc(pos, h, shot + 1, !turn));
    }
  }
  return res;
}

void solve(){
  cin >> P >> Q >> N;
  REP(i, N) cin >> H[i] >> G[i];
  memset(memo, -1, sizeof(memo));
  cout << calc(0, H[0], 0, 1) << endl;
}

int main(){
  int T;
  cin >> T;
  REP(t, T){
    cout << "Case #" << t + 1 << ": ";
    solve();
  }
  return 0;
}
