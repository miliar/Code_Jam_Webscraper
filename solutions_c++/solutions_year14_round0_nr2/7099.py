#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <fstream>

#define REP(I, N) for (int I = 0; I < (N); ++I)
#define PER(I, N) for (int I = (N); I >= 0; --I)
#define PERR(I, A, B) for (int I = (A); I >= (B); --I)
#define REPP(I, A, B) for (int I = (A); I <  (B); ++I)
#define REPN(I, A, B) for (int I = (A); I <= (B); ++I)
#define REPC(I, A, C) for (int I = (A); (C); ++I)
#define REPPP(I, A, B, C) for (int I = (A); I <  (B); I += C)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define RIIII(X, Y, Z, W) scanf("%d%d%d%d", &(X), &(Y), &(Z), &(W))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define DRIIII(X, Y, Z, W) int X, Y, Z, W; scanf("%d%d%d%d", &X, &Y, &Z, &W)
#define RS(X) scanf("%s", (X))
#define LEN(X) int(strlen(X))
#define SZ(X) int((X).size())
#define SUM(X, N) accumulate(X, X + (N), 0)
#define MS0(X) memset((X), 0, sizeof(X))
#define MSI(X) memset((X), 0xFF, sizeof(X))
#define F first
#define S second
#define MP make_pair
#define PB push_back

#ifdef DK
  #define MAX 10
#else
  #define MAX 10
#endif

using namespace std;

static double g(double c, double f, double x) {
  double r = 2.0f, sum = 0.0f;
  double res = x / r;
  REPN(i, 2, 3000000) {
    sum += c / (r + (i - 2) * f);
    double nxt = sum + x / (r + (i - 1) * f);
    res = min(res, nxt);
  }
  return res;
}

int main() {
#ifdef DK
//  freopen("in.txt", "r", stdin);
  freopen("B-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  DRI(T);
  REP(t, T) {
    double c = 0.0, f = 0.0, x = 0.0;
    scanf("%lf%lf%lf", &c, &f, &x);
    printf("Case #%d: %.7f\n", t + 1, g(c, f, x));
  }
  return 0;
}
