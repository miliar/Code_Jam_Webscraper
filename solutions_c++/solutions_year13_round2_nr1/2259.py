#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  int examples;
  scanf("%d", &examples);
  for (int ex = 1; ex <= examples; ex++) {
    int A, N;
    scanf("%d%d", &A, &N);
    vector<int> v;
    for (int i = 0; i < N; i++) {
      int t;
      scanf("%d", &t);
      v.push_back(t);
    }
    sort(v.begin(), v.end());
    int sum = A;
    int res = 0;
    for (int i = 0; i < N; i++) {
      if (sum > v[i]) {
        sum += v[i];
      } else {
        if (sum == 1) {
          res += N - i;
          break;
        }

        int n = 0;
        while (sum <= v[i]) {
          sum += (sum - 1);
          n++;
        }

        if (n > N - i) {
          res += N - i;
          break;
        } else {
          sum += v[i];
          res += n;
        }

      }
    }
    // output
    printf("Case #%d: ", ex);
    printf("%d", res);
    printf("\n");
  }
}
