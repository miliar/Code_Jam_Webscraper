#include <cstdio>
#include <cmath>
#include <cassert>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#define SIZE(x) ((int) (x).size())
#define REP(i, n) for (int i = 0; i < (int) (n); ++i)
#define FOR(i, a, b) for (int i = (int) (a); i <= (int) (b); ++i)
#define FORD(i, a, b) for (int i = (int) (a); i >= (int) (b); --i)
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

const int INF = 1023456789;

int solve() {
  int n;
  scanf("%d", &n);
  int res = 0, cnt = 0;
  REP(i, n + 1) {
    char c;
    scanf(" %c", &c);
    int x = c - '0';
    if (x > 0) {
      while (cnt < i) {
        ++cnt;
        ++res;
      }
      cnt += x;
    }
  }
  return res;
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(i, 1, t) {
    printf("Case #%d: %d\n", i, solve());
  }
}
