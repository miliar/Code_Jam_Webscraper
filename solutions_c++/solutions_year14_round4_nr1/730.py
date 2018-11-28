#include <assert.h>
#include <ctype.h>
#include <float.h>
#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#include <algorithm>
#include <complex>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
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
#define CLR(c,n) memset(c, n, sizeof(c))
#define TR(it, c) for(typeof(c.begin()) it = c.begin();it != c.end(); ++it)
#define CONTAIN(it, c) (c.find(it) != c.end())
typedef vector<int> VI;
typedef pair<int, int> PII;
template <class T> void checkmin(T &a, T b) { if (b<a) a=b; }
template <class T> void checkmax(T &a, T b) { if (b>a) a=b; }

int n, x;
int cnt[1024];
void work(int idx) {
  scanf("%d%d", &n, &x);
  memset(cnt, 0, sizeof(cnt));
  int s;
  REP(i, n) {
    scanf("%d", &s);
    ++cnt[s];
  }
  int ans = 0;
  for (int i = x; i >= 0; --i) {
    int j = x - i;
    while (cnt[i] > 0) {
      --cnt[i];
      ++ans;
      while (j > 0 && cnt[j] == 0) --j;
      if (cnt[j] > 0) --cnt[j];
    }
  }
  printf("Case #%d: %d\n", idx, ans);
}

int main(int argc, char *argv[]) {
  int tc;
  scanf("%d", &tc);
  FOR(i, 1, tc) work(i);
}
