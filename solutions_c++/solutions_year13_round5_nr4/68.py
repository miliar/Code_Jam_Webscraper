#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <cassert>
#include <string>
#include <memory.h>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <cctype>
#include <iomanip>
#include <sstream>
#include <cctype>
#include <fstream>
#include <cmath>
using namespace std;

#define REP2(i, m, n) for(int i = (int)(m); i < (int)(n); i++)
#define REP(i, n) REP2(i, 0, n)
#define ALL(c) (c).begin(), (c).end()
#define ITER(c) __typeof((c).begin())
#define PB(e) push_back(e)
#define FOREACH(i, c) for(ITER(c) i = (c).begin(); i != (c).end(); ++i)
#define MP(a, b) make_pair(a, b)
#define PARITY(n) ((n) & 1)

typedef long long ll;
typedef pair<ll, ll> P;
const int INF = 1000 * 1000 * 1000 + 7;
const double EPS = 1e-10;

double memo[1 << 20];

double calc(int mask, int n){
  if(mask == 0){
    return 0;
  }
  if(memo[mask] > -EPS){
    return memo[mask];
  }

  double &ans = memo[mask] =0;
  REP(i, n){
    int pos = i;
    int fee = n;
    while(PARITY(mask >> pos) == 0){
      fee--;
      pos = (pos + 1) % n;
    }
    int nmask = mask & ~(1 << pos);
    ans += fee + calc(nmask, n);
  }
  
  ans /= n;
  return ans;
}

double solve(){
  string str;
  cin >> str;

  fill(memo, memo + (1 << 20), -1);


  int N = str.size();
  int mask = 0;    
  REP(i, N) if(str[i] != 'X') mask |= 1 << i;
  return calc(mask, N);
}

int main(){
  int T;
  cin >> T;
  REP2(t, 1, T + 1){
    cout << "Case #" << t << ": " << fixed << setprecision(20) << solve() << endl;
  }
  return 0;
}
