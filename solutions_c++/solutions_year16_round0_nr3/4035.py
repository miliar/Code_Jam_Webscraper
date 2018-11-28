#include <bits/stdc++.h>
using namespace std;

void bin(int k) {
  if (k == 0) return;
  bin(k/2);
  printf("%d", k % 2);
}

long long eval(int k, int b) {
  if (k == 0) return 0ll;
  return eval(k/2, b)*b + (k%2);
}

long long div(long long k) {
  for (long long i = 2; i <= sqrt(k); i++) {
    if (k % i == 0) return i;
  }
  return 0;
}

bool check(int k) {
  for (int b = 2; b <= 10; b++) {
    if (div(eval(k, b)) == 0) return 0;
  }
  return 1;
}

int main() {
  freopen("C-small-attempt0.in", "r", stdin);
  freopen("C-small-attempt0.out", "w+", stdout);
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    int N, J;
    scanf("%d%d", &N, &J);
    vector<int> ans;
    for (int i = 0, j; i < 1<<(N-2); i++) {
      j = (1<<N-1) + (i<<1) + 1;
      if (check(j)) {
        ans.push_back(j);
        if (ans.size() >= J) break;
      }
    }
    printf("Case #%d:\n", t);
    for (int i = 0; i < J; i++) {
      bin(ans[i]);
      for (int b = 2; b <= 10; b++) {
        printf(" %lld", div(eval(ans[i], b)), eval(ans[i], b));
      }
      printf("\n");
    }
  }
  return 0;
}

