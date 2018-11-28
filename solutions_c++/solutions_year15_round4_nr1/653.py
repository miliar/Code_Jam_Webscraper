#include <algorithm>
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

typedef vector<int> VI;
typedef pair<int, int> PII;

int ri()
{
  int x;
  scanf("%d", &x);
  return x;
}

const int N = 1000;
char a[N][N+1];
bool b[N][N];

int f(int m, int n, int i, int j)
{
  int c = 0, s = 0;
  bool f;

  f = true;
  ROF(jj, 0, j)
    if (a[i][jj] != '.') {
      c++;
      f = false;
      break;
    }
  if (f && a[i][j] == '<') s++;

  f = true;
  FOR(jj, j+1, n)
    if (a[i][jj] != '.') {
      c++;
      f = false;
      break;
    }
  if (f && a[i][j] == '>') s++;

  f = true;
  ROF(ii, 0, i)
    if (a[ii][j] != '.') {
      c++;
      f = false;
      break;
    }
  if (f && a[i][j] == '^') s = 1;

  f = true;
  FOR(ii, i+1, m)
    if (a[ii][j] != '.') {
      c++;
      f = false;
      break;
    }
  if (f && a[i][j] == 'v') s = 1;

  return c ? s : -1;
}

int main()
{
  int cases = ri();
  REP1(cc, cases) {
    int m = ri(), n = ri();
    bool tak = true;
    int ans = 0;
    REP(i, m)
      scanf("%s", a[i]);
    REP(i, m)
      REP(j, n)
        if (a[i][j] != '.') {
          int x = f(m, n, i, j);
          if (x < 0) { tak = false; goto L1; }
          ans += x;
        }
L1:;
   if (tak)
     printf("Case #%d: %d\n", cc, ans);
   else
     printf("Case #%d: IMPOSSIBLE\n", cc);
  }
}
