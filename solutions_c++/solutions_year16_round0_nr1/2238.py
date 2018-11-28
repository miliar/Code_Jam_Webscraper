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

const int MAXIT = 10000000;

void solve() {
  int N;
  scanf("%d", &N);

  int cnt = 0;
  vector< int > got(10, 0);

  FOR(i, 1, MAXIT) {
    llint x = (llint) i * N;
    while (x) {
      if (!got[x % 10]++) ++cnt;
      x /= 10;
    }
    if (cnt == 10) {
      printf("%lld\n", (llint)i * N);
      return;
    }
  }

  puts("INSOMNIA");
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
