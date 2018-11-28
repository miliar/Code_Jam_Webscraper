#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

string str[16];
int p[16];
int m, n;
int res1, res2;

void f(void) {
  vector<vector<string>> v(n);
  REP(i,m) v[p[i]].push_back(str[i]);
  int cnt = 0;
  REP(i,n) {
    set<string> s;
    s.insert("");
    REP(j,v[i].size())
      REP(k,v[i][j].size()) s.insert(v[i][j].substr(0, k+1));
    if (s.size() > 1) {
      cnt += s.size();
    }
  }
  if (cnt > res1) {res1 = cnt; res2 = 1;}
  else if (cnt == res1) res2++;
}

void rec(int i) {
  if (i == m) {f(); return;}
  REP(j,n) {
    p[i] = j;
    rec(i+1);
  }
  return;
}

int main() {
  int t;
  cin >> t;
  REP(cas,t) {
    cin >> m >> n;
    res1 = -1; res2 = 0;
    REP(i,m) cin >> str[i];
    rec(0);
    printf("Case #%d: %d %d\n", cas+1, res1, res2);
  }
  return 0;
}
