#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;
#define MAX 1024
int v[MAX];

int main(void)
{
  int T;

  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++)
  {
    int N;
    scanf("%d", &N);
    for(int i = 0; i < N; i++)
    {
      scanf("%d", v+i);
    }

    int r1, r2;
    r1 = r2 = 0;

    int q = 0;
    for(int i = 1; i < N; i++)
    {
      q = max(q, v[i-1]-v[i]);
      if (v[i] < v[i-1])
      {
        r1 += (v[i-1]-v[i]);
      }
    }

    for(int i = 0; i < N-1; i++)
    {
      r2 += min(v[i], q);
    }

    printf("Case #%d: %d %d\n", caso, r1, r2);
  }
}
