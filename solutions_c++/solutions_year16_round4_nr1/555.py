#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>

#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <functional>

#include <sstream>
#include <iostream>

using namespace std;
typedef long long llint;
const llint inf = 1000000000000000000LL;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

string gen(int n, char c) {
  if (n == 0) {
    string ret = "";
    ret += c;
    return ret;
  }

  string L, R;
  
  switch (c) {
  case 'P': L =  gen(n - 1, 'P'); R = gen(n - 1, 'R'); break;
  case 'R': L =  gen(n - 1, 'R'); R = gen(n - 1, 'S'); break;
  case 'S': L =  gen(n - 1, 'P'); R = gen(n - 1, 'S'); break;
  }
  
  if (L > R) swap(L, R);
  return L + R;
}

void solve() {
  int N, R, P, S;
  scanf("%d%d%d%d", &N, &R, &P, &S);

  vector< string > s;
  s.push_back(gen(N, 'P'));
  s.push_back(gen(N, 'R'));
  s.push_back(gen(N, 'S'));

  string sol = "";

  for (auto z : s) {
    int r = R, p = P, s = S;
    REP(i, 1 << N) {
      switch (z[i]) {
      case 'P': --p; break;
      case 'R': --r; break;
      case 'S': --s; break;
      }
    }

    if (r == 0 && p == 0 && s == 0) {
      if (sol == "" || z < sol)
	sol = z;
    }
  }

  if (sol == "")
    puts("IMPOSSIBLE");
  else
    printf("%s\n", sol.c_str());
}

int main(void) 
{
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }

  return 0;
}
