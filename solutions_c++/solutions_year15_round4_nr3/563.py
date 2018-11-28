#include <algorithm>
#include <bitset>
#include <climits>
#include <iterator>
#include <cstring>
#include <cstdio>
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
#define ALL(x) (x).begin(), (x).end()

typedef vector<int> VI;
typedef pair<int, int> PII;

int ri()
{
  int x;
  scanf("%d", &x);
  return x;
}

double rd()
{
  double x;
  scanf("%lf", &x);
  return x;
}

const int N = 20;
bitset<2000> b[N+2];
char a[1000000];

int main()
{
  int cases = ri();
  REP1(_c, cases) {
    int n = ri();
    while (getchar() != '\n');
    map<string, int> id;
    int m = 0;
    REP(i, n) {
      gets(a);
      b[i] = 0;
      for (char *p = a; ; p = NULL) {
        char *q = strtok(p, " \t\b\f");
        if (! q) break;
        if (! id.count(q))
          id[q] = m++;
        b[i].set(id[q]);;
      }
    }

    int ans = INT_MAX;
    for (int m = 0; m < 1 << n; m++)
      if ((m&3) == 1) {
        bitset<2000> en, fr;
        REP(i, n)
          if (m & 1 << i)
            en |= b[i];
          else
            fr |= b[i];
        ans = min(ans, (int)(en&fr).count());
      }
    printf("Case #%d: %d\n", _c, ans);
  }
}
