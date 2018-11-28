#include <bits/stdc++.h>
using namespace std;
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
template<class T>inline void check_min(T&a,T b){if(b<a)a=b;}
template<class T>inline void check_max(T&a,T b){if(a<b)a=b;}
typedef long long lint;

string read_it() {
  static char s[64];
  scanf("%s", s);
  return s;
}

string solve() {
  int n, l;
  scanf("%d%d", &n, &l);
  set<string> good;
  REP (i, n) {
    good.insert(read_it());
  }
  string bad = read_it();
  if (good.count(bad)) {
    return "IMPOSSIBLE";
  }
  string ans = string(l - 1, '1') + " ";
  if (l == 1) ans = "0 ";
  REP (i, l) ans += "0?";
  return ans;
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: %s\n", index, solve().c_str());
  }
  return 0;
}
