#include <cstdio>

#include <vector>

using namespace std;

vector<int> generate(int k) {
  vector<int> result;

  if (k == 1) return{ 1 };
  if (k == 2) return{ 2 };

  vector<int> subResult = generate(k - 1);

  result.push_back(2);
  for (auto r : subResult) {
    result.push_back(r + 1);
  }

  return result;
}

int main() {
  int T;
  scanf("%d", &T);

  for (int kase = 1; kase <= T; kase++) {
    int K, C, S;
    scanf("%d %d %d", &K, &C, &S);

    printf("Case #%d:", kase);

    if (C == 1) {
      if (S != K) puts(" IMPOSSIBLE");
      else {
        for (int i = 1; i <= K; i++) {
          printf(" %d", i);
        }
        putchar('\n');
      }
    }
    else {
      vector<int> result = generate(K);
      if (S < result.size()) puts(" IMPOSSIBLE");
      else {
        for (int r : result) {
          printf(" %d", r);
        }
        putchar('\n');
      }
    }
  }

  return 0;
}
