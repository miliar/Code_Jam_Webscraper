#include <iostream>
#include <cstdio>

int a[1024];
int f[1024];
int result = 0;
int N;
int v[1024];

void trace(int index) {
  int t = 1;
  while (f[index] == 0) {
    f[index] = t;
    index = a[index];
    t += 1;
  }
  result = std::max(result, t - f[index]);
  v[index] = std::max(v[index], f[index]);
}

int solve() {
  result = 0;
  scanf("%d", &N);
  for (int i = 1; i <= N; i++) {
    v[i] = 0;
  }
  for (int i = 1; i <= N; i++) {
    scanf("%d", &a[i]);
  }

  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      f[j] = 0;
    }
    trace(i);
  }
  int sum = 0;
  for (int i = 1; i <= N; i++) {
    if (a[i] > i && a[a[i]] == i)
      sum += v[i] + v[a[i]];
  }
  result = std::max(result, sum);
  return result;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; i++) {
    printf("Case #%d: %d\n", i, solve());
  }
}
