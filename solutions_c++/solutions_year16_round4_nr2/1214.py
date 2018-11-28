#include <stdio.h>

#include <algorithm>
#include <utility>
#include <vector>


using std::max;
using std::swap;
using std::vector;


int main(void) {
  int num_cases;
  scanf("%d", &num_cases);

  for (int case_idx = 1; case_idx <= num_cases; ++case_idx) {
    int n, k;
    scanf("%d %d", &n, &k);

    vector<double> p(n);
    for (int i = 0; i < n; ++i) {
      scanf("%lf", &p[i]);
    }

    double ans = 0;
    for (int bits = 0, bits_end = 1 << n; bits < bits_end; ++bits) {
      vector<double> q;
      for (int i = 0; i < n; ++i) {
        if ((bits >> i) & 1) {
          q.push_back(p[i]);
        }
      }
      if (q.size() != k) {
        continue;
      }
      vector<double> prob(k + 1, 0);
      vector<double> tmp(k + 1, 0);
      prob[0] = 1;

      for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k; ++j) {
          tmp[j] = (1 - q[i]) * prob[j];
          if (j > 0) {
            tmp[j] += q[i] * prob[j - 1];
          }
        }
        swap(prob, tmp);
      }

      ans = max(ans, prob[k / 2]);
    }

    printf("Case #%d: %.9f\n", case_idx, ans);
  }
  return 0;
}
