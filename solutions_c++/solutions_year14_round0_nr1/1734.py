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
  int v, num;
  vector<int> count(20);

  REP(i, 2){
    cin >> v;
    REP(r, 4) REP(c, 4){
      cin >> num;
      if (r + 1 == v) count[num]++;
    }
  }

  vector<int> ans;
  for (int i = 0; i < 20; i++)
    if (count[i] == 2)
      ans.push_back(i);
  if (ans.empty()){
    cout << "Volunteer cheated!" << endl;
  } else if ((int)ans.size() > 1){
    cout << "Bad magician!" << endl;
  } else {
    cout << ans[0] << endl;
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
