#include <cstdio>
#include <algorithm>

#define Nmax 110


int K, L, S;
char Kb[Nmax], T[Nmax], V[Nmax];

int best, count, total;

void back(int cnt) {
  if (cnt == S) {
    int matches = 0;
    for (int i = 0; i + L <= cnt; ++i) {
      bool ok = true;
      for (int j = 0; ok && j < L; ++j)
        ok &= V[i + j] == T[j];
      if (ok)
        ++matches;
    }
    ++count;
    total += matches;
    best = (best > matches ? best : matches);
    return;
  }

  for (int i = 0; i < K; ++i) {
    V[cnt] = Kb[i];
    back(cnt + 1);
    V[cnt] = 0;
  }
}

int main() {
  int t;
  scanf("%d\n", &t);
  for (int ti = 1; ti <= t; ++ti) {
    scanf("%d%d%d\n", &K, &L, &S);
    fgets(Kb, Nmax, stdin);
    fgets(T, Nmax, stdin);

    count = total = best = 0;
    back(0);
    printf("Case #%d: %lf\n", ti, best - (1.0 * total) / count);
  }
  return 0;
}
