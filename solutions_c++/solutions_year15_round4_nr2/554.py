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
long double V, X;

#define MAXN 111
#define EPS (1e-11)
pair<long double, long double> source[MAXN];

bool possible(long double t) {
  long double Min = 0, Max = 0, Vol = 0;
  REP(i, N) {
    long double tt = min(t, (V - Vol) / source[i].second);
    long double v = tt * source[i].second;
    Vol += v;
    Min += v * source[i].first;
  }
  reverse(source, source + N);
  Vol = 0;
  REP(i, N) {
    long double tt = min(t, (V - Vol) / source[i].second);
    long double v = tt * source[i].second;
    Vol += v;
    Max += v * source[i].first;
  }
  reverse(source, source + N);
  if (Vol + EPS < V) {
    // fprintf(stderr, "t: %Lf Vol: %Lf V: %Lf Min: %Lf X: %Lf Max: %Lf\n", t, Vol, V, Min, X, Max);
    return false;
  }
  // printf("t: %lf, Min: %lf Max: %lf X: %lf\n", t, Min, Max, X);
  return Min - EPS <= X && X <= Max + EPS;
}

void solve_testcase() {
  scanf("%d", &N);
  scanf("%Lf%Lf", &V, &X);
  X *= V;
  REP(i, N) scanf("%Lf%Lf", &(source[i].second), &(source[i].first));
  sort(source, source + N);
  long double l = 0, r = 1000000000;
  REP(i, 200) {
    long double m = (l + r) / 2;
    if (possible(m)) r = m;
    else l = m;
  }
  // if (N == 1) fprintf(stderr, "V: %Lf X: %Lf %Lf %Lf, l = %Lf r = %Lf\n", V, X / V, source[0].second, source[0].first, l, r);
  if (r > 100000000) printf("IMPOSSIBLE\n");
  else printf("%.9Lf\n", (l + r) / 2);
}

void solve_small() {
  scanf("%d", &N);
  scanf("%Lf%Lf", &V, &X);
  REP(i, N) scanf("%Lf%Lf", &(source[i].second), &(source[i].first));
  sort(source, source + N);
  // fprintf(stderr, "X: %.9Lf first: %.9Lf\n", X, source[0].first);
  if (X + EPS < source[0].first || source[N - 1].first + EPS < X) {
    printf("IMPOSSIBLE\n");
    return;
  }
  if (N == 1) {
    printf("%.9Lf\n", V / source[0].second);
    return;
  }
  if (abs(source[0].first - source[1].first) < EPS) {
    printf("%.9Lf\n", V / (source[0].second + source[1].second));
    return;
  }
  long double v0 = (V * X - V * source[1].first) / (source[0].first - source[1].first);
  long double v1 = (V * X - V * source[0].first) / (source[1].first - source[0].first);
  // fprintf(stderr, "%Lf %Lf\n", v0, v1);
  printf("%.9Lf\n", max(v0 / source[0].second, v1 / source[1].second));
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    printf("Case #%d: ", t);
    solve_small();
    // solve_testcase();
  }
  return 0;
}
