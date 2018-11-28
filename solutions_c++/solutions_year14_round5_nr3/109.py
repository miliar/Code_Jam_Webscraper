#include <algorithm>
#include <cstdio>
#include <cstring>
#include <functional>
#include <map>
#include <set>
#include <utility>
#include <vector>
using namespace std;

#define REP(i, n) for (int i = 0; i < (n); i++)
#define REP1(i, n) for (int i = 1; i <= (n); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define ROF(i, a, b) for (int i = (b); --i >= (a); )
#define pb push_back
#define mp make_pair
#define fi first
#define se second

typedef vector<int> VI;
typedef pair<int, int> PII;

int ri()
{
  int x;
  scanf("%d", &x);
  return x;
}

const int N = 15;
char ev[N];
int f[1<<N], g[1<<N], x[N];

static inline void set_min(int &x, int y)
{
  if (x == -1 || y < x) x = y;
}

int main()
{
  int cases = ri();
  REP1(cc, cases) {
    int n = ri(), z = 0;
    char e;
    map<int, int> m;
    REP(i, n) {
      scanf(" %c%d", &ev[i], &x[i]);
      if (x[i]) {
        if (! m.count(x[i])) {
          int t = m.size();
          m[x[i]] = t;
        }
        x[i] = m[x[i]];
      } else {
        z++;
        x[i] = -1;
      }
    }
    int nn = m.size()+z;
    f[0] = 0;
    FOR(i, 1, 1<<nn)
      f[i] = f[i>>1] + (i&1);
    REP(i, n) {
      fill_n(g, 1<<nn, -1);
      REP(j, 1<<nn)
        if (f[j] >= 0) {
          if (ev[i] == 'E') {
            if (x[i] >= 0) {
              if (! (j & 1<<x[i]))
                set_min(g[j | 1<<x[i]], f[j]+1);
            } else {
              REP(k, nn)
                if (! (j & 1<<k))
                  set_min(g[j | 1<<k], f[j]+1);
            }
          } else {
            if (x[i] >= 0) {
              if (j & 1<<x[i])
                set_min(g[j & ~(1<<x[i])], f[j]-1);
            } else {
              REP(k, nn)
                if (j & 1<<k)
                  set_min(g[j & ~(1<<k)], f[j]-1);
            }
          }
        }
      copy_n(g, 1<<n, f);
    }

    int opt = nn+1, opti = -1;
    REP(i, 1<<nn)
      if (f[i] != -1 && f[i] < opt)
        opt = f[i], opti = i;
    printf("Case #%d: ", cc);
    if (opti == -1)
      puts("CRIME TIME");
    else
      printf("%d\n", opt);
  }
}
