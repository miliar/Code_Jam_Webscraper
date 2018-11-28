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

const int inf = 1e9;
const double eps = 1e-9;

int memo[16][1 << 16];
int N;
char D[20];
int  I[20];

int calc(int pos, int mask){
  if (pos == N) return __builtin_popcount(mask);
  
  if (memo[pos][mask] != -1) return memo[pos][mask];
  
  int &res = memo[pos][mask] = inf;

  int idx = I[pos];
  
  if (idx > 0){
    if (D[pos] == 'E' && BIT(mask, idx) == 0){
      res = min(res, calc(pos + 1, mask ^ (1 << idx)));
    } else if (D[pos] == 'L' && BIT(mask, idx) == 1){
      res = min(res, calc(pos + 1, mask ^ (1 << idx)));
    }
  } else {
    for (int i = 1; i <= N; i++){
      if (D[pos] == 'E' && BIT(mask, i) == 0){
        res = min(res, calc(pos + 1, mask ^ (1 << i)));
      } else if (D[pos] == 'L' && BIT(mask, i) == 1){
        res = min(res, calc(pos + 1, mask ^ (1 << i)));
      }
    }
  }
  return res;
}

void solve(){
  memset(memo, -1, sizeof(memo));
  cin >> N;
  vector<int> VI(N);
  REP(i, N){
    cin >> D[i] >> I[i];
    VI[i] = I[i];
  }

  VI.push_back(0);
  sort(ALL(VI));
  
  VI.erase(unique(ALL(VI)), VI.end());
  
  REP(i, N) I[i] = lower_bound(ALL(VI), I[i]) - VI.begin();
  
  
  int res = inf;
  memset(memo, -1, sizeof(memo));

  REP(mask, 1 << (N + 1)) {
    res = min(res, calc(0, mask));
  }
  
  if (res == inf){
    cout << "CRIME TIME" << endl;
  } else {
    cout << res << endl;
  }
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
