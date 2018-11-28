#include <bits/stdc++.h>
using namespace std;
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
template<class T>inline void check_min(T&a,T b){if(b<a)a=b;}
template<class T>inline void check_max(T&a,T b){if(a<b)a=b;}
typedef long long lint;

char hs[300];

string gen(int depth, char c) {
  if (depth == 0) return string(1, c);
  string a = gen(depth - 1, c), b = gen(depth - 1, hs[(int)c]);
  if (a > b) swap(a, b);
  return a + b;
}

string solve() {
  int n, r, p, s;
  scanf("%d%d%d%d", &n, &r, &p, &s);
  vector<string> vs;
  for (char c: string("RPS")) {
    string str = gen(n, c);
    int o[3] = {};
    for (char i: str) {
      o[i == 'R' ? 0 : (i == 'P' ? 1 : 2)] += 1;
    }
    if (o[0] == r && o[1] == p && o[2] == s) vs.push_back(str);
  }
  sort(ALL(vs));
  return vs.empty() ? "IMPOSSIBLE" : vs[0];
}

int main() {
  hs['S'] = 'P', hs['P'] = 'R', hs['R'] = 'S';
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: %s\n", index, solve().c_str());
  }
  return 0;
}
