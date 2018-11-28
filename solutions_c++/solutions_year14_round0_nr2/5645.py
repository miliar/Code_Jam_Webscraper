#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
typedef vector<int> VI;
typedef pair<int, int> PII;
#define CLR(c,n) memset(c,n,sizeof(c))
template <class T> void checkmin(T &a, T b) { if (b<a) a=b; }
template <class T> void checkmax(T &a, T b) { if (b>a) a=b; }
#define TR(it, container) for(typeof(container.begin()) it = container.begin();\
it != container.end(); it++)
#define CONTAIN(it, container) (container.find(it)!=container.end())

int main(int argc, char *argv[]) {
  int tc;
  double c, f, x;
  cin >> tc;
  FOR(ic, 1, tc) {
    cin >> c >> f >> x;
    int n = 0;
    double t = 0, v = 2;
    double ans = x / v;
    while (t < ans) {
      t += c / v;
      ++n;
      v = n * f + 2;
      double ans2 = t + x / v;
      if (ans2 > ans) break;
      ans = ans2;
    }
    printf("Case #%d: %.7lf\n", ic, ans);
  }
}
