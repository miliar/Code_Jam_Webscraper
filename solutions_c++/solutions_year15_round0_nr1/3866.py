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

char c[1010];

int test() {
  int n; scanf("%d%s", &n, c);
  for (int i = 0; i <= n; ++i) {
    c[i] -= '0';
  }
  int cnt = c[0], res = 0;
  for (int i = 1; i <= n; ++i) {
    if (c[i] && cnt < i) {
      res += i - cnt;
      cnt = i;
    }
    cnt += c[i];
  }
  return res;
}

int main(void) {
  int T; scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    printf("Case #%d: %d\n", t, test());
  }
  return 0;
}
