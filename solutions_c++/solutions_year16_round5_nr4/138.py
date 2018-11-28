#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAX = 222;

char a[MAX][MAX];
char b[MAX];

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    int N, L;
    scanf("%d %d", &N, &L);
    REP(i, N) scanf("%s", a[i]);
    scanf("%s", b);

    bool cant = false;
    REP(i, N) {
      bool same = true;
      REP(j, L) same &= a[i][j] == b[j];
      cant |= same;
    }
    
    printf("Case #%d: ", tp);
    if (cant) {
      puts("IMPOSSIBLE");
    } else {
      string A = "0";
      REP(i, L-1) A += "0?";
      string B = string(L-1, '1') + "0?" + string(L-1, '1');
      printf("%s %s\n", A.c_str(), B.c_str());
      assert(A.size() + B.size() <= 200);
    }
  }
  return 0;
}
