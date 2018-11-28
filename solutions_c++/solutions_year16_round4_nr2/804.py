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
double a[1000];
double f[210][210];
int t[1000];

int main() {
  scanf("%d", &Tests); 
  for (int tts = 0; Tests--; ) {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i) scanf("%lf", &a[i]);
    
    double ans = 0;
    for (int s = 0; s < two(n); ++s) {
      t[0] = 0;
      for (int i = 0; i < n; ++i)
        if (contain(s, i)) t[++t[0]] = i;
      if (t[0] == m) {
        f[0][0] = 1;
        for (int i = 1; i <= m; ++i)
          for (int j = 0; j <= i; ++j) {
            f[i][j] = f[i - 1][j] * (1 - a[t[i]]);
            if (j > 0) f[i][j] += f[i - 1][j - 1] * a[t[i]];
          }
        ans = max(ans, f[m][m / 2]);
      }
    }
    printf("Case #%d: %lf\n", ++tts, ans);
  }
}