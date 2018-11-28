#include <cassert>
#include <cstring>

#include <algorithm>
#include <iostream>
#include <set>

using namespace std;

#define REP(i, n) FOR(i, 0, n)
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAXS = 1123;
const int MAXCOMP = 123;
const int mod = 1e9 + 7;

int ns, nc;
string S[MAXS];
int where[MAXS];

int maks, kol;

void rek(int x) {
  if (x == ns) {
    int suma = 0;
    
    REP(ic, nc) {
      static set<string> prefs; prefs.clear();
      REP(is, ns) if (where[is] == ic) {
        int sz = S[is].size();
        REP(L, sz+1) prefs.insert(S[is].substr(0, L));
      }
      suma += (int)prefs.size();
    }

    if (suma > maks) { maks = suma; kol = 0; }
    if (suma == maks) ++kol;
    return;
  }

  REP(i, nc) {
    where[x] = i;
    rek(x+1);
  }
}

int main(void)
{
  int ntc; scanf("%d", &ntc);
  REP(tc, ntc) {
    scanf("%d %d", &ns, &nc);

    REP(i, ns) {
      static char buff[123]; scanf("%s", buff);
      S[i] = buff;
    }

    maks = -1; kol = 0;
    rek(0);

    printf("Case #%d: %d %d\n", tc+1, maks, kol%mod);
    fflush(stdout);
  }
  return 0;
}
