#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAX = 1010;

struct Pt {
  int x, y, z;
} a[MAX], v[MAX];

int N, S;

bool bio[MAX];

double dist(Pt& a, Pt& b) {
  return (a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y) + (a.z-b.z)*(a.z-b.z);
}

void dfs(int i, double R) {
  if (bio[i]) return;
  bio[i] = true;
  REP(j, N)
    if (dist(a[i], a[j]) <= R*R) dfs(j, R);
}

bool can(double R) {
  REP(i, N) bio[i] = false;
  dfs(0, R);
  return bio[1];
}

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    scanf("%d %d", &N, &S);
    REP(i, N) {
      scanf("%d %d %d %d %d %d", &a[i].x, &a[i].y, &a[i].z, &v[i].x, &v[i].y, &v[i].z);
    }

    double lo = 0, hi = 1e4;
    REP(it, 50) {
      double mid = (lo + hi) / 2;
      if (can(mid)) hi = mid;
      else lo = mid;
    }
    
    printf("Case #%d: ", tp);
    printf("%.10lf\n", lo);
  }
  return 0;
}
