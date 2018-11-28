#include <stdio.h>
#include <vector>
#include <algorithm>

#define MAXM 1002
#define MAXN 1000000002
#define MOD 1000002013

using namespace std;

inline int min(int a, int b) {
  return a>b?b:a;
}
inline int max(int a, int b) {
  return a>b?a:b;
}

int o[MAXM], e[MAXM], p[MAXM];
int pb[2*MAXM][2*MAXM];
vector<int> map;
int N, M;

int cmp(const void *a, const void *b) {
  return (*((int*) a) - *((int*) b));
}

inline int overlap(int fi, int ti, int fj, int tj) {
  return (ti >= fj && !(fi > tj)) || (tj >= fi && !(fj > ti));
}
inline int contains(int fi, int ti, int fj, int tj) {
  return ((fi >= fj && ti <= tj)
      || (fj >= fi && tj <= ti));
}

int price(int i) {
  int one = ((long long) N)*i % MOD;
  int two = ((long long) i)*(i-1)/2;
  return one - two;
}

int cvalue() {
  int f, t;
  int v = 0;
  for (f=0; f<2*M; f++) {
    for (t=0; t<2*M; t++) {
      long long mv = ((long long) price(map[t] - map[f])) * pb[f][t];
      long long mv2 = mv % MOD;
      v += mv2;
      v = v % MOD;
    }
  }
  return v;
}

int onepass() {
  int fi, ti, fj, tj;
  int changed = 0;
  for (fi=0; fi<2*M; fi++)
    for (ti=0; ti<2*M; ti++)
      for (fj=0; fj<2*M; fj++)
        for (tj=0; tj<2*M; tj++)
          if (overlap(fi, ti, fj, tj) && !contains(fi, ti, fj, tj) && pb[fi][ti] > 0 && pb[fj][tj] > 0) {
            int opb;
            if (pb[fi][ti] < pb[fj][tj]) {
              opb = pb[fi][ti];
              pb[fi][ti] = 0;
              pb[fj][tj] -= opb;
            } else {
              opb = pb[fj][tj];
              pb[fj][tj] = 0;
              pb[fi][ti] -= opb;
            }
            pb[min(fi, fj)][max(ti, tj)] += opb;
            pb[max(fi, fj)][min(ti, tj)] += opb;
            changed = 1;
          }
  return changed;
}

int get(int x) {
  int pos = 0;
  while (map[pos] != x)
    pos++;
  return pos;
}

int main() {
  int T;
  scanf("%d", &T);
  int ncase;

  for (ncase=0; ncase<T; ncase++) {
    printf("Case #%d: ", ncase+1);
    scanf("%d %d", &N, &M);
    map.clear();
    int i;
    int j;
    for (i=0; i<M; i++) {
      scanf("%d %d %d", &(o[i]), &(e[i]), &(p[i]));
      map.push_back(o[i]);
      map.push_back(e[i]);
    }
    sort(map.begin(), map.end());
    for (i=0; i<2*M; i++) {
      for (j=0; j<2*M; j++) {
        pb[i][j] = 0;
      }
    }
    for (i=0; i<M; i++) {
      pb[get(o[i])][get(e[i])] += p[i];
    }
    int value=cvalue();
    //printf("current value: %d\n", value);
    while (onepass());
    int value2=cvalue();
    //printf("current value: %d\n", value2);
    printf("%d\n", (value - value2) % MOD);
  }
  return 0;
}
