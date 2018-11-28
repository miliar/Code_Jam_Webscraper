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
  
  vector<double> A(N), B(N);
  REP(i, N) cin >> A[i];
  REP(i, N) cin >> B[i];
  
  sort(ALL(A));
  sort(ALL(B));
  int dwar = 0;
  int war = 0;
  {                             // dwar
    int pos = 0;
    REP(i, N){
      while (pos < N && A[pos] < B[i]) pos++;
      if (pos < N){
        dwar++;
        pos++;
      }
    }
  }

  {                             // war
    vector<bool> used(N, false);
    REP(i, N){
      int c = -1;
      int d = -1;
      
      REP(j, N) if (!used[j]){
        if (B[j] > A[i] && c == -1){
          c = j;
        } else if (d == -1){
          d = j;
        }
      }
      
      if (c != -1){
        used[c] = true;
      } else {
        war++;
        used[d] = true;
      }
    }
  }
  cout << dwar << " " << war << endl;
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
