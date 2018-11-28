#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    vector<int> A;

    int smax;
    scanf("%d ", &smax);

    for (int i = 0; i <= smax; i++) {
      int p = getchar() - '0';
      while (p--) A.push_back(i);
    }

    sort(A.begin(), A.end());

    int R = 0;
    for (int i = 0; i < (int)A.size(); i++) {
      R = max(R, A[i] - i);
    }

    printf("Case #%d: %d\n", tc, R);
  }
}
