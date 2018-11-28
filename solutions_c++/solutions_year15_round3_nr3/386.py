#include <cstdio>
#include <cstring>

#define Vmax 1000
#define Nmax 100

int best, C, D, V;
bool ok[Vmax], viz[Vmax];
int bestS[Nmax], S[Nmax];

bool check(int cnt) {
  memset(ok, 0, sizeof(ok));

  for (int i = 0; i < D + cnt; ++i) {
    for (int j = V; j >= 1; --j) {
      if (ok[j] && j + S[i] <= V)
        ok[j + S[i]] = true;
    }
    ok[S[i]] = true;   
  }

  bool all = true;
  for (int i = 1; i <= V; ++i)
    all &= ok[i];
  return all;
}

void back(int last, int cnt) {
  if (check(cnt)) {
    if (cnt < best) { //= (cnt < best ? cnt : best);
      best = cnt;
      memcpy(bestS, S, sizeof(S));
    }
    return;
  }
  if (cnt >= 5)
    return;

  for (int i = last + 1; i <= V; ++i) {
    if (viz[i])
      continue;
    viz[i] = true;
    S[cnt + D] = i;
    back(i, cnt + 1);
    viz[i] = false;
  }
} 

int main() {
  int t;
  scanf("%d", &t);
  for (int ti = 1; ti <= t; ++ti) {
    memset(viz, 0, sizeof(viz));
    best = 99;
    scanf("%d%d%d", &C, &D, &V);
    for (int i = 0; i < D; ++i) {
      scanf("%d", &S[i]);
      viz[ S[i] ] = true;
    }
    back(0, 0);
    printf("Case #%d: %d\n", ti, best);
    //printf("final set: ");
    //for (int i = 0; i < D + best; ++i)
    //  printf("%d ", bestS[i]);
    //printf("\n");
  }

  return 0;
}
