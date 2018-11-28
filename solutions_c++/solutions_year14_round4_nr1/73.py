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
  int N, X, R = 0, num;
  int C[1000];
  memset(C, 0, sizeof(C));

  cin >> N >> X;
  
  REP(i, N){
    cin >> num;
    C[num]++;
  }

  int pos = 999;
  while (pos >= 0){
    if (C[pos] == 0){
      pos--;
    } else {
      C[pos]--;
      for (int i = pos; i >= 0; i--){
        if (pos + i <= X && C[i] > 0) {
          C[i]--;
          break;
        }
      }
      R++;
    }
  }
  cout << R << endl;
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
