#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define popb pop_back

#define pii pair<int,int>
#define pdd pair<long double, long double>
#define mp make_pair
//#define X first
//#define Y second

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

#define maxN 105

int T;
int N;
long double V, X;
pdd source[maxN];

#define err 1e-9

bool lt(long double x1, long double x2) {
  return x1 < x2 - err;
}
bool eq(long double x1, long double x2) {
  return abs(x1-x2) < err;
}
bool lteq(long double x1, long double x2) {
  return lt(x1, x2) || eq(x1, x2);
}

long double best_time;
long double minC, maxC;
long double bestT = -1;

pdd for_second;

void update(long double newT) {
  if (eq(bestT, -1)) bestT = newT;
  else bestT = min(bestT, newT);
}

pdd operator-(pdd A) {
  return mp(A.first, -A.second);
}

pdd combine(pdd A, pdd B) {
  return mp((A.first * A.second + B.first * B.second) / (A.second + B.second),
      A.second + B.second);
}

long double two_sources(pdd A, pdd B) {
  if (eq(X, A.first)) return V / A.second;
  long double k2 = V * (X - A.first) / (B.second * B.first - B.second * A.first);
  long double k1 = (V - k2 * B.second) / A.second;
//        printf("%d, %d: %Lf %Lf\n", i, j, k1, k2);
  return max(k1, k2);
}

int main() {
  scanf("%d", &T);
  FOR(t, 1, T) {
    bestT = -1;
    scanf("%d%Lf%Lf", &N, &V, &X);
    for_second = mp(0, 0);
    REP(i, N) {
      long double R, C;
      scanf("%Lf%Lf", &R, &C);
      source[i] = mp(C, R);
      for_second = combine(for_second, source[i]);
    }
    sort(source, source + N);
    if (lt(X, source[0].first) || lt(source[N-1].first, X)) {
      printf("Case #%d: IMPOSSIBLE\n", t);
      continue;
    }
    int start; int dir;
    if (eq(for_second.first, X)) {
      printf("Case #%d: %.9Lf\n", t, V / for_second.second);
      continue;
    }
    if (lt(for_second.first, X)) {
      start = 0; dir = 1;
    } else {
      start = N - 1; dir = -1;
    }
    for (int i = start; i != -1 && i != N; i += dir) {
      pdd new_for_second = combine(for_second, -source[i]);
      if (eq(new_for_second.first, X) || (lt(for_second.first, X) ^ lt(new_for_second.first, X))) {
        bestT = two_sources(new_for_second, source[i]);
        break;
      } else {
        for_second = new_for_second;
      }
    }
    printf("Case #%d: %.9Lf\n", t, bestT);
  }

  return 0;
}
