#include <stdio.h>

#include <algorithm>
#include <vector>

using namespace std;

int solve(const vector<int> &ns, int i, int A, int N) {
  if (i >= N) return 0;
  if (A > ns[i]) {
    return solve(ns, i+1, A+ns[i], N);
  } else {
    int a = 1+solve(ns, i+1, A, N);
    int need = 0;
    while (A <= ns[i]) {
      A += A-1;
      ++need;
    }
    int b = need+solve(ns, i+1, A+ns[i], N);
    return min(a, b);
  }
}

int main() {
  int result;
  int T = 0;
  result = scanf("%d", &T);
  for (int ti = 0; ti < T; ++ti) {
    int A = 0;
    int N = 0;
    result = scanf("%d%d", &A, &N);
    vector<int> ns(N, 0);
    for (int ni = 0; ni < N; ++ni) {
      int tmp = 0;
      scanf("%d", &tmp);
      ns[ni] = tmp;
    }
    sort(ns.begin(), ns.end());
    int ans = 0;
    if (A == 1) ans = N;
    else ans = solve(ns, 0, A, N);
    printf("Case #%d: %d\n", ti+1, ans);
  }
  return 0;
}
