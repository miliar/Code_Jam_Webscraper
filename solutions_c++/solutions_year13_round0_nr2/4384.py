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

string solve(){
  int N, M;
  cin >> N >> M;
  vector<vector<int> > A(N, vector<int>(M, 0));
  REP(i, N)REP(j, M) cin >> A[i][j];
  
  vector<int> hr(N, 0);
  vector<int> hc(M, 0);
  REP(i, N)REP(j, M) hr[i] = max(hr[i], A[i][j]);
  REP(j, M)REP(i, N) hc[j] = max(hc[j], A[i][j]);
  REP(i, N)REP(j, M) if(A[i][j] != min(hr[i], hc[j])) return "NO";
  return "YES";
}

int main(){
  int T;
  cin >> T;
  REP(t, T){
    printf("Case #%d: %s\n", t + 1, solve().c_str());
  }
  return 0;
}
