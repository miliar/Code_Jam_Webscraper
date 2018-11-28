#include <cstdio>
#include <vector>
#include <string>

using namespace std;
typedef long long LL;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int nn;
  scanf("%d", &nn);

  for (int i (1); i <= nn; ++i) {
    printf("Case #%d: ", i);

    vector<LL> vec;
    int tt, temp;
    scanf("%d", &tt);
    for (int k (0); k < tt; ++k) {
      scanf("%d", &temp);
      vec.push_back(temp);
    }
    int slope (0);
    LL sum1 (0), sum2 (0);
    for(unsigned k = 1; k < vec.size(); ++k) {
      if (vec[k] < vec[k - 1]) {
        sum1 += vec[k - 1] - vec[k];
        if (vec[k - 1] - vec[k] > slope)
          slope = vec[k - 1] - vec[k];
      }
    }

    for(unsigned k = 0; k < vec.size() - 1; ++k) {
      if (vec[k] < slope)
        sum2 += vec[k];
      else
        sum2 += slope;
    }
    printf("%lld %lld\n", sum1, sum2);
  }
  return 0;
}