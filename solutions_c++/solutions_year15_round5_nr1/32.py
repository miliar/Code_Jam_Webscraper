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

const int MAX = 2e6;

int S[MAX], M[MAX];
int A[MAX], B[MAX];
vector<int> E[MAX], F[MAX];

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    int N, D;
    int S0, As, Cs, Rs;
    int M0, Am, Cm, Rm;
    scanf("%d %d", &N, &D);
    scanf("%d %d %d %d", &S0, &As, &Cs, &Rs);
    scanf("%d %d %d %d", &M0, &Am, &Cm, &Rm);
    
    S[0] = S0, M[0] = M0;
    REP(i, N) {
      S[i+1] = (S[i] * llint(As) + Cs) % Rs;
      M[i+1] = (M[i] * llint(Am) + Cm) % Rm;
    }
    FOR(i, 1, N) M[i] %= i;
    
    REP(i, Rs) E[i].clear(), F[i].clear();

    A[0] = B[0] = S[0];
    FOR(i, 1, N) {
      A[i] = min(A[M[i]], S[i]);
      B[i] = max(B[M[i]], S[i]);
    }
    
    REP(i, N) E[B[i]].push_back(i);
    int cnt = 0, ans = 0;
    REP(R, Rs) {
      for (int i: E[R])
        if (B[i] - A[i] <= D) {
          cnt++;
          if (A[i] + D + 1 < Rs)
            F[A[i] + D + 1].push_back(i);
        }
      for (int i: F[R]) cnt--;
      if (R >= B[0] && R-D <= B[0]) ans = max(ans, cnt);
    }

    printf("Case #%d: ", tp);
    printf("%d\n", ans);
  }
  return 0;
}
