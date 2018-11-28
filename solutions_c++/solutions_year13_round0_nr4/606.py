#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

#define IMPOSSIBLE 100
#define LEN 20
#define MAX (1<<(LEN))
#define TOT 41
char f[MAX];
int K, N, start[TOT];
int k[LEN], n[LEN], t[LEN][TOT];

char faz(int x)
{
  char &home = f[x];

  if (home < 0)
  {
    int keys[TOT];

    memset(keys, 0, sizeof(keys));
    for(int i = 0; i < K; i++)
      keys[start[i]]++;
    for(int i = 0; i < LEN; i++)
      if (x&(1<<i))
      {
        keys[n[i]]--;
        for(int j = 0; j < k[i]; j++)
          keys[t[i][j]]++;
      }

    home = IMPOSSIBLE;
    for(int i = 0; i < LEN; i++)
      if (!(x&(1<<i)))
        if (keys[n[i]] > 0)
        {
          faz(x|(1<<i));
          if (f[x|(1<<i)] != IMPOSSIBLE)
          {
            home = i;
            break;
          }
        }
  }

  return home;
}

int main(void)
{
  int T;

  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++)
  {
    scanf("%d %d", &K, &N);
    for(int i = 0; i < K; i++)
      scanf("%d", start+i);
    for(int i = 0; i < N; i++)
    {
      scanf("%d %d", n+i, k+i);
      for(int j = 0; j < k[i]; j++)
        scanf("%d", &t[i][j]);
    }

    memset(f, -1, sizeof(f));
    f[(1<<N)-1] = N;

    printf("Case #%d:", caso);

    int r = faz(0);
    if (r == IMPOSSIBLE) printf(" IMPOSSIBLE\n");
    else
    {
      int flag = 0;
      do
      {
        printf(" %d", r+1);
        flag = flag | (1<<r);
        r = faz(flag);
      } while (r != N);
      printf("\n");
    }
  }
}
