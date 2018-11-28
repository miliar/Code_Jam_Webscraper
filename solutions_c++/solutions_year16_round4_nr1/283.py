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

template <typename S, typename T> ostream &operator<<(ostream &out, const pair<S, T> &p) {
  out << "(" << p.first << ", " << p.second << ")";
  return out;
}

template <typename T> ostream &operator<<(ostream &out, const vector<T> &v) {
  out << "[";
  REP(i, v.size()){
    if (i > 0) out << ", ";
    out << v[i];
  }
  out << "]";
  return out;
}

typedef long long ll;

const ll inf = 1e15;
const ll mod = 1000 * 1000 * 1000 + 7;
const double eps = 1e-9;

string rec(int win_type, int n){
  if (n == 0){
    switch (win_type){
    case 0 :
      return "R";
      break;
    case 1:
      return "P";
      break;
    case 2:
      return "S";
      break;
    default:
      assert(false);
    }
  } else {
    vector<string> vs;
    if (win_type == 0){
      vs.push_back(rec(0, n - 1));
      vs.push_back(rec(2, n - 1));
    } else if (win_type == 1){
      vs.push_back(rec(1, n - 1));
      vs.push_back(rec(0, n - 1));
    } else {
      vs.push_back(rec(2, n - 1));
      vs.push_back(rec(1, n - 1));
    }
    sort(vs.begin(), vs.end());
    return vs[0] + vs[1];
  }
}

void solve(){
  int N, R, P, S;
  cin >> N >> R >> P >> S;

  int tmp_R = R, tmp_P = P, tmp_S = S;
  bool impossible = false;
  while (tmp_R + tmp_P + tmp_S > 1){
    int sum = (tmp_R + tmp_P + tmp_S) / 2;
    int tmp_R_ = tmp_R;
    int tmp_P_ = tmp_P;
    int tmp_S_ = tmp_S;
    tmp_R = sum - tmp_P_;
    tmp_S = sum - tmp_R_;
    tmp_P = sum - tmp_S_;
    // cout << sum << " " << tmp_R << " " << tmp_P << " " << tmp_S << endl;
    if (min({tmp_R, tmp_S, tmp_P}) < 0) impossible = true;
  }
  

  if (impossible){
    cout << "IMPOSSIBLE" << endl;
    return;
  }

  int win_type = tmp_R ? 0 : tmp_P ? 1 : 2;
  cout << rec(win_type, N)  << endl;
}
 
int main(){
  int T;
  cin >> T;
  REP(t, T){
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
