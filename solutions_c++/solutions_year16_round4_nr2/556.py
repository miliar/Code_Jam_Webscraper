#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>

#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <functional>

#include <sstream>
#include <iostream>

using namespace std;
typedef long long llint;
const llint inf = 1000000000000000000LL;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

const int MAX = 205;

int N, K;
double p[MAX];

int bio[MAX][2 * MAX];
double dp[MAX][2 * MAX];

vector< double > ps;

double calc_prob(int i, int d) {
  if (i == K) {
    if (d == 0)
      return 1.0;
    else
      return 0.0;
  }

  if (bio[i][d + MAX])
    return dp[i][d + MAX];

  double sol = 0.0;
  sol = 
    calc_prob(i + 1, d + 1) * ps[i] +
    calc_prob(i + 1, d - 1) * (1.0 - ps[i]);

  bio[i][d + MAX] = 1;
  dp[i][d + MAX] = sol;

  return sol;
}

void solve() {
  scanf("%d%d", &N, &K);
  REP(i, N) scanf("%lf", p + i);
  sort(p, p + N);

  double sol = 0.0;

  for (int i = 0; i < N; ++i) {
    ps.clear();
    for (int j = 0; j < K; ++j) {
      int J = (i + j) % N;
      ps.push_back(p[J]);
    }
    memset(bio, 0, sizeof bio);
    sol = max(sol, calc_prob(0, 0));
  }
  
  printf("%.10lf\n", sol);
}

int main(void) 
{
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }

  return 0;
}
