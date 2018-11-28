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
    printf("Case #%d: ", z);
    double a[1111], b[1111];
    DRI(n);
    set<double> bb;
    REP(i, n)
      scanf("%lf", &a[i]);
    REP(i, n) {
      scanf("%lf", &b[i]);
      bb.insert(b[i]);
    }
    sort(a, a + n);
    sort(b, b + n);
    int l = 0, ra = n - 1, rb = n - 1;
    int cnt = 0;
    while (l <= ra) {
      if (a[ra] > b[rb]) {
        ra--;
        rb--;
        cnt++;
      }
      else {
        l++;
        rb--;
      }
    }
    printf("%d ", cnt);
    cnt = 0;
    REP(i, n) {
      set<double>::iterator it = bb.lower_bound(a[i]);
      if (it != bb.end()) {
        bb.erase(it);
      }
      else {
        cnt++;
        bb.erase(bb.begin());
      }
    }
    printf("%d\n", cnt);
  }
  return 0;
}
