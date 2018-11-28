#include <cstdio>
#include <cstring>

#include <vector>
#include <set>
#include <map>
#include <iostream>

using namespace std;
typedef long long llint;
const llint inf = 1000000000000000000LL;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

const int MAX = 105;

void solve() {
  string s; cin >> s; s += "+";
  int cnt = 0;
  REP(i, (int)s.size() - 1)
    cnt += (s[i] != s[i + 1]);
  printf("%d\n", cnt);
}

int main(void) 
{
  int T;
  scanf("%d", &T);
  FOR(t, 1, T + 1) {
    printf("Case #%d: ", t);
    solve();
  }

  return 0;
}
