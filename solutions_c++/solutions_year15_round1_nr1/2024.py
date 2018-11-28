#include <cstdio>
#include <algorithm>

using namespace std;

void run(int t) {
  int N;
  int M[10000];
  int sumofdiff = 0;
  int maxdiff = 0;
  int last = -1;
  scanf("%d", &N);
  for (int i = 0; i < N; i++) {
    int x;
    scanf("%d", &x);
    M[i] = x;
    if (last > x) {
      int diff = last - x;
      maxdiff = max(maxdiff, diff);
      sumofdiff += diff;
    }
    last = x;
  }
  int sumspeed = 0;
  for (int i = 0; i < N - 1; ++i) {
    int x = M[i];
    if (x < maxdiff) {
      sumspeed += x;
    } else {
      sumspeed += maxdiff;
    }
  }
  printf("Case #%d: %d %d\n", t, sumofdiff, sumspeed);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    run(i + 1);
  }
}
