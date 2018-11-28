#include <iostream>
#include <vector>

using namespace std;

void solve(int test) {
  vector<long long> res;
  long long K, C, S;
  scanf("%lld%lld%lld", &K, &C, &S);
  long long j = 0;
  while ((long long)res.size() != S) {
    long long cur = 0;
    for (long long lvl = 0; lvl < C; lvl++) {
      cur *= K;
      cur += min(j, K - 1);
      j++;
    }
    res.push_back(cur);
  }
  printf("Case #%d:", test);
  if (j < K) {
    printf(" IMPOSSIBLE\n");
  } else {
    sort(begin(res), end(res));
    res.resize(unique(begin(res), end(res)) - begin(res));
    for (auto x : res) {
      printf(" %lld", x + 1);
    }
    printf("\n");
  }
}
int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; test++) {
    solve(test);
  }
}
