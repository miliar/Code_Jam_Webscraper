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

void solve(){
  int N;
  cin >> N;
  vector<int> A(N);
  REP(i, N) cin >> A[i];
  vector<int> B(A);
  sort(ALL(B));

  int res = 0;
  
  REP(i, N){
    int l = 0, lv = 0;
    int r = N, rv = 0;
    while (A[l] != B[i]){
      if (A[l] > B[i]) lv++;
      l++;
    }
    
    while (A[--r] != B[i]){
      if (A[r] > B[i]) rv++;
    }

    // cout << i << " " << lv << " " << rv << endl;
    res += min(lv, rv);
  }
  cout << res << endl;
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
