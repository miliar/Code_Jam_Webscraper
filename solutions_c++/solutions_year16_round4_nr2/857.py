#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

const int nmax = 200 + 18;

double p[nmax], cp[nmax], ansp;
int N, K;

double tmpp[2][nmax * 2];
void update()
{
  int ni = 0;
  memset(tmpp[ni], 0, sizeof(tmpp[ni]));
  tmpp[ni][0 + nmax] = 1;
  for (int i = 1; i <= K; ++i) {
    int pi = ni ^ 1;
    memset(tmpp[pi], 0, sizeof(tmpp[pi]));
    for (int j = -(i - 1); j <= i - 1; ++j) {
      double l = tmpp[ni][j + nmax];
      tmpp[pi][j + 1 + nmax] += cp[i] * l;
      tmpp[pi][j - 1 + nmax] += (1 - cp[i]) * l;
    }
    ni = pi;
  }
  // printf("update: %.6f\n", tmpp[ni][nmax]);
  if (ansp < tmpp[ni][0 + nmax])
    ansp = tmpp[ni][0 + nmax];
}

void search(int i, int tot)
{
  if (i > N) {
    if (tot == K)
      update();
    return ;
  }
  if (tot == K)
    search(i + 1, tot);
  else {
    search(i + 1, tot);
    cp[tot + 1] = p[i];
    search(i + 1, tot + 1);
  }
}


int main()
{
  int T;
  scanf("%d", &T);
  for (int cases = 1; cases <= T; ++cases) {
    ansp = 0;
    scanf("%d%d", &N, &K);
    for (int i = 1; i <= N; ++i)
      scanf("%lf", p + i);
    search(1, 0);
    printf("Case #%d: %.10f\n", cases, ansp);
  }
  return 0;
}
