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


void solve(){
  string S;
  cin >> S;
  string G(S.size(), '+');
  queue<string> que;
  map<string, int> visit;
  que.push(S);
  visit[S] = 0;

  while (!que.empty()){
    string s = que.front(); que.pop();
    if (s == G){
      cout << visit[s] << endl;
      return;
    }
    
    REP(i, S.size()){
      string t = s;
      reverse(t.begin(), t.begin() + i + 1);
      REP(j, i + 1) t[j] = (t[j] == '+' ? '-' : '+');
      
      if (visit.count(t) == 0){
        que.push(t);
        visit[t] = visit[s] + 1;
      }
    }
  }
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
