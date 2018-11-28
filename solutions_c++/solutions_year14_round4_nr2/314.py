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

    int N;
    scanf("%d", &N);
    vector<int> A(N);
    for (int i = 0; i < N; i++) scanf("%d", &A[i]);

    int R = 0;

    for (int j = 0; j < N; j++) {
      int minid = min_element(A.begin(), A.end()) - A.begin();
      R += min(minid, int(A.size() - 1 - minid));
      A.erase(A.begin() + minid);
    }

    printf("%d\n", R);
  }
}
