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

int Q1[MAX][MAX], Q2[MAX][MAX];

int main() {
#ifdef DK
//  freopen("in.txt", "r", stdin);
  freopen("A-small-attempt2.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  DRI(T);
  REP(t, T) {
    DRI(a1);
    REP(i, 4) {
      REP(j, 4) {
        RI(Q1[i][j]);
      }
    }
    DRI(a2);
    REP(i, 4) {
      REP(j, 4) {
        RI(Q2[i][j]);
      }
    }
    int cnt = 0, res = 0;
    REP(i, 4) {
      REP(j, 4) {
        if (Q1[a1 - 1][i] == Q2[a2 - 1][j]) {
          cnt++;
          res = Q1[a1 - 1][i];
        }
      }
    }
    if (cnt == 0) {
      printf("Case #%d: Volunteer cheated!\n", t + 1);
    } else if (cnt == 1) {
      printf("Case #%d: %d\n", t + 1, res);
    } else {
      printf("Case #%d: Bad magician!\n", t + 1);
    }
  }
  return 0;
}
