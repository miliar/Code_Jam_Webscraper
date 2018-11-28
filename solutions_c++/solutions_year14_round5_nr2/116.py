#include <algorithm>
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

typedef vector<int> VI;
typedef pair<int, int> PII;

int ri()
{
  int x;
  scanf("%d", &x);
  return x;
}

const int N = 100, H = 201, C = 1001;
int p, q, n, hp[N+1], price[N], dp[N][H][C][2][2];

int f(int i, int h, int c, int w, int atk)
{
  if (i == n) return 0;
  int &ret = dp[i][h][c][w][atk];
  if (ret >= 0) return ret;
  if (!w) {
    c += atk;
    ret = f(i, h, c, 1, 0);
    REP1(j, c) {
      if (p*j >= h) {
        ret = max(ret, f(i+1, hp[i+1], c-j, 1, 0) + price[i]);
        if (c+1-j > 0)
          ret = max(ret, f(i+1, hp[i+1], c-j, 0, 0) + price[i]);
        break;
      }
      else {
        ret = max(ret, f(i, h-p*j, c-j, 1, 0));
        if (c+1-j > 0)
          ret = max(ret, f(i, h-p*j, c-j, 0, 0));
      }
    }
    //if (p*(c+1) >= h) {
    //  int cc = (h+p-1)/p;
    //  ret = max(ret, f(i+1, hp[i+1], c+1-cc, 1) + price[i]);
    //}
  } else
    ret = q >= h ? f(i+1, hp[i+1], c, 0, 1) : f(i, h-q, c, 0, 1);
  return ret;
}

int main()
{
  int cases = ri();
  REP1(cc, cases) {
    p = ri(), q = ri(), n = ri();
    REP(i, n) {
      hp[i] = ri();
      price[i] = ri();
    }
    REP(i, n)
      memset(dp[i], -1, sizeof dp[i]);
    printf("Case #%d: %d\n", cc, f(0, hp[0], 0, 0, 1));
    fprintf(stderr,"Case #%d: %d\n", cc, f(0, hp[0], 0, 0, 1));
  }
}
