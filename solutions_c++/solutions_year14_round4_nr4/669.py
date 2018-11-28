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
const int MOD=1000000007;

int m, M, n, cnt[256], g_cnt;
int dp[9][256], tot[9][256];
char s[8][12];
struct Node {
  Node *next[26];
  Node() {
    CLR(next, 0);
  }
  ~Node() {
    REP(i, 26) if (next[i]) delete next[i];
  }
  int insert(char *c) {
    if (*c == '\0') return 0;
    int ans = 0;
    if (next[*c - 'A'] == NULL) {
      next[*c - 'A'] = new Node();
      ++ans;
    }
    return ans + next[*c-'A']->insert(c+1);
  }
};

int count_trie(int mask) {
  Node p;
  int ans = 1;
  REP(i, m) if (mask & (1<<i)) ans += p.insert(s[i]);
  return ans;
}

int getmax(int ng, int mask, int *num) {
  if (ng == 1) {
    *num = 1;
    return cnt[mask];
  }
  int &ans = dp[ng][mask];
  int &total= tot[ng][mask];
  if (ans != -1) {
    *num = total;
    return ans;
  }
  ans = 0;
  total = 0;
  int subtotal;
  REP(i, M) if (i != 0 && i != mask && (mask & i) == i) {
    int sub = cnt[i] + getmax(ng-1, mask-i, &subtotal);
    if (sub > ans) {
      ans = sub;
      total = subtotal;
    } else if (sub == ans) {
      total += subtotal;
      if (total >= MOD) total -= MOD;
    }
  }
  *num = total;
  return ans;
}

void work(int idx) {
  scanf("%d%d", &m, &n);
  M = 1 << m;
  REP(i, m) scanf("%s", s[i]);
  CLR(cnt, 0);
  REP(i, M) cnt[i] = count_trie(i);
  memset(dp, -1, sizeof(dp));
  int total;
  int mx = getmax(n, M-1, &total);
  printf("Case #%d: %d %d\n", idx, mx, total);
}

int main(int argc, char *argv[]) {
  int tc;
  scanf("%d", &tc);
  FOR(i, 1, tc) work(i);
}
