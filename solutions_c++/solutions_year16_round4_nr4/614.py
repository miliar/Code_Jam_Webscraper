#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
#define Abs(x) ((x) < 0 ? (-(x)) : (x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

int Tests, n, m;
int p[100], q[100];
char a[100][100], b[100][100];

  bool f(int i) {
    if (i == n) {
      return true;
    }
    bool haha = false;
    for (int j = 0; j < n; ++j)
      if (!q[j] && b[p[i]][j] == '1') {
        q[j] = 1;
        haha = true;
        if (!f(i + 1)) return false;
        q[j] = 0;
      }
    return haha;
  }

int main() {
  scanf("%d", &Tests); 
  for (int tts = 0; Tests--; ) {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) scanf("%s", a[i]);
    
    int ans = n * n;
    for (int s = 0; s < two(n * n); ++s) {
      for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
          b[i][j] = a[i][j];
      int tot = 0;
      for (int i = 0; i < n * n; ++i)
        if (contain(s, i)) {
          b[i / n][i % n] = '1';
          ++tot;
        }
      for (int i = 0; i < n; ++i) p[i] = i;
      bool ok = true;
      do {
        for (int i = 0; i < n; ++i) q[i] = 0;
        if (!f(0)) {
          ok = false;
          break;
        }
      } while (next_permutation(p, p + n));
      if (ok) ans = min(ans, tot);
    }
    printf("Case #%d: %d\n", ++tts, ans);
  }
}