/* Written by Filip Hlasek 2015 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<(b);i++)

using namespace std;

int N;
#define MAXN 222
int s[MAXN][2222];

int S[MAXN];

map<string, int> m;

long long eng[MAXN * MAXN * MAXN], french[MAXN * MAXN * MAXN], FLAG = 1;

void solve_testcase() {
  m.clear();
  scanf("%d\n", &N);
  fprintf(stderr, "N = %d\n", N);
  REP(i, N) {
    S[i] = 0;
    string ss = "";
    while (true) {
      char c;
      scanf("%c", &c);
      if (c == '\n' || c == ' ') {
        if (!m.count(ss)) { int M = m.size(); m[ss] = M; }
        s[i][S[i]++] = m[ss];
      }
      if (c == '\n') break;
      if (c == ' ') { ss = ""; continue; }
      ss.push_back(c);
    }
    fprintf(stderr, " %d", S[i]);
  }
  fprintf(stderr, "\n");
  fprintf(stderr, "different words: %d\n", (int)m.size());
  int ans = MAXN * MAXN * MAXN;
  REP(mask, 1 << N) if ((mask & 3) == 1) {
    FLAG++;
    REP(i, N) if (mask & (1 << i)) REP(j, S[i]) eng[s[i][j]] = FLAG;
    int tmp = 0;
    REP(i, N) if (!(mask & (1 << i))) REP(j, S[i]) if (french[s[i][j]] != FLAG) {
      french[s[i][j]] = FLAG;
      if (eng[s[i][j]] == FLAG) tmp++;
    }
    ans = min(ans, tmp);
  }
  printf("%d\n", ans);
  fprintf(stderr, "%d\n", ans);
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    printf("Case #%d: ", t);
    fprintf(stderr, "testcase #%d\n", t);
    solve_testcase();
  }
  return 0;
}
