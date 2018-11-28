#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    printf("Case #%d: ", tc);

    int N, X;
    scanf("%d%d", &N, &X);
    vector<int> S(N);
    for (int i = 0; i < N; i++) scanf("%d", &S[i]);
    sort(S.begin(), S.end());

    int R = 0;
    vector<bool> selected(N, false);

    for (int a = N-1; a >= 0; a--) {
      if (selected[a]) continue;
      selected[a] = true;
      R++;
      for (int b = a-1; b >= 0; b--) {
        if (selected[b]) continue;
        if (S[a] + S[b] > X) continue;
        selected[b] = true;
        break;
      }
    }
    printf("%d\n", R);
  }
}
