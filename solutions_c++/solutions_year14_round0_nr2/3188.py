#define PRETEST
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <cstring>
#include <cstdio>
using namespace std;

#define INF 0x7FFFFFFF
#define INFLL 0x7FFFFFFFFFFFFFFF
#define BIG 0x4F4F4F4F
#define PI acos(-1)
#define RESET(a,x) memset(a,x,sizeof(a))
#define EXIST(a,s) ((s).find(a) != (s).end())

typedef long long ll;
typedef unsigned long long ull;
typedef map<string, int> msi;
typedef map<int, int> mii;
typedef pair<int, int> pii;
typedef pair<string, int> psi;

#define DEBUG(x) cout << #x << " : " << x << endl

#define sqr(x) ((x)*(x))
#define MP(x,y) make_pair(x,y)
#define PB push_back
#define eps 1e-9
#define fst first
#define snd second
#define REP(I,N) for (int I = 0; I < (N); I++)
#define REPP(I,A,B) for (int I = (A); I < (B); I++)
#define REPE(I,A,B) for (int I = (A); I <= (B); I++)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define RS(X) scanf("%s", (X))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)

int main(int argc, char* argv[]) {
  #ifdef PRETEST
  freopen("in.txt", "r", stdin);
  #endif
  ios_base::sync_with_stdio(false);
  DRI(t);
  REPE(z, 1, t) {
    double c, f, x, k;
    scanf("%lf%lf%lf", &c, &f, &x);
    k = (int)(x / c - 2 / f + eps);
    k = max(0.0, k);
    double ans = 0;
    REP(i, k) {
      ans += c / (2 + f * i);
    }
    ans += x / (2 + f * k);
    printf("Case #%d: %.7lf\n", z, ans);
  }
  return 0;
}
