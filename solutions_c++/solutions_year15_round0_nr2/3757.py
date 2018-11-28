#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <sstream>
#include <iostream>
#include <set>
#include <map>
#include <cassert>

#define REP(AA,BB) for(int AA=0; AA<(BB); ++AA)
#define FOR(AA,BB,CC) for(int AA=(BB); AA<(CC); ++AA)
#define FC(AA,BB) for(__typeof((AA).begin()) BB=(AA).begin(); BB!=(AA).end(); ++BB)
#define SZ(AA) ((int)((AA).size()))
#define ALL(AA) (AA).begin(), (AA).end()
#define PB push_back
#define MP make_pair

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;
typedef long double LD;

const int M = 1000;

int test() {
  int n; scanf("%d", &n);
  VI p(n);
  REP (i, n) {
    scanf("%d", &p[i]);
  }
  int best = 2 * M;
  for (int i = 1; i <= M; ++i) {
    int can = i;
    REP (j, n) {
      if (p[j] >= i) {
        can += (p[j] + i - 1) / i - 1;
      }
    }
    best = min(best, can);
  }
  return best;
}

int main(void) {
  int T; scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    printf("Case #%d: %d\n", t, test());
  }
  return 0;
}
