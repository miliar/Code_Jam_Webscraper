#include <stdio.h>
#include <vector>
#include <algorithm>

struct Barbar {
  int index;
  int time;
  int rest;
};

int eugrid(int n, int m) {
  if (n > m) {
    int _n = n;
    n = m;
    m = _n;
  }
  while(n != 0) {
    int _n = n;
    n = m % n;
    m = _n;
  }
  return m;
}

void dump(Barbar M[], int B) {
  printf("M = \n");
  for(int i = 0; i < B; i++) {
    printf("%3d ", M[i].rest);
  }
  printf("\n");
  for(int i = 0; i < B; i++) {
    printf("%3d ", M[i].time);
  }
  printf("\n");
  for(int i = 0; i < B; i++) {
    printf("%3d ", M[i].index);
  }
  printf("\n");
}

int solve(int B, int N, int M[]) {
  Barbar b[1000];

  int x = 1;
  for (int i = 0; i < B; i++) {
    x = x * M[i] / eugrid(x, M[i]);
  }
  int nn = 0;
  for (int i = 0; i < B; i++) {
    nn += x / M[i];
  }
  N %= nn;
  N += nn;
  //  printf("N=%d", N);

  for (int i = 0; i < B; i++) {
    b[i].index = i;
    b[i].time = M[i];
    b[i].rest = 0;
  }

  for (int i = 0; ; i++) {
    std::sort(b, b + B,
              [](const Barbar &_a, const Barbar &_b) -> bool {
                if (_a.rest == _b.rest) return _a.index < _b.index;
                return _a.rest < _b.rest;
              });

    //    dump(b, B);
    for (int j = 1; j < B; j++) {
      b[j].rest -= b[0].rest;
    }
    b[0].rest = b[0].time;
    if (N == 1) {
      return b[0].index + 1;
    }
    N -= 1;
  }
  return 0;
}

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 0; t < T; t++) {
    int B, N;
    scanf("%d %d", &B, &N);

    int M[1000];
    for (int m = 0; m < B; m++) {
      scanf("%d", &M[m]);
    }

    int r = solve(B, N, M);
    printf("Case #%d: %d\n", t + 1, r);
  }

  return 0;
}
