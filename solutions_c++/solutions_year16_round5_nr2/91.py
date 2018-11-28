/* Written by Filip Hlasek 2016 */
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

#define MAXN 111
int P[MAXN];
char Name[MAXN];

int Desc[MAXN];

char text[MAXN];
bool done[MAXN];
int options[MAXN], O;
void gen_random() {
  REP(i, N) done[i] = false;
  REP(i, N) {
    O = 0;
    int total = 0;
    REP(j, N) if (!done[j] && (P[j] == 0 || done[P[j] - 1])) {
      options[O++] = j;
      total += Desc[j];
    }
    int val = rand() % total;
    int kk;
    REP(k, O) {
      if (val < Desc[options[k]]) { kk = options[k]; break; }
      val -= Desc[options[k]];
    }
    done[kk] = true;
    text[i] = Name[kk];
  }
}

int M;
char Word[MAXN][MAXN];
int valid[MAXN], W[MAXN];

bool is_substring(int w) {
  REP(i, N - W[w] + 1) {
    bool ok = true;
    REP(j, W[w]) if (text[i + j] != Word[w][j]) { ok = false; break; }
    if (ok) return true;
  }
  return false;
}

void dfs(int n) {
  Desc[n] = 1;
  REP(i, N) if (P[i] == n + 1) { dfs(i); Desc[n] += Desc[i]; }
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(testcase, 1, T) {
    scanf("%d", &N);
    REP(i, N) scanf("%d", P + i);
    REP(i, N) Desc[i] = 0;
    REP(i, N) if (P[i] == 0) dfs(i);
    scanf("%s", Name);
    scanf("%d", &M);
    REP(i, M) {
      scanf("%s", Word[i]);
      valid[i] = 0;
      W[i] = strlen(Word[i]);
    }
    int Q = 20000;
    REP(i, Q) {
      gen_random();
      REP(j, M) if (is_substring(j)) valid[j]++;
    }
    printf("Case #%d:", testcase);
    REP(i, M) printf(" %.04lf", (double)valid[i] / Q);
    printf("\n");
  }
  return 0;
}
