#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

#define MAX 1024
int c[MAX];

int main(void)
{
  int T;

  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++)
  {
    int N, X, s;

    memset(c, 0, sizeof(c));
    scanf("%d %d", &N, &X);
    for(int i = 0; i < N; i++)
    {
      scanf("%d", &s);
      c[s]++;
    }

    int r = 0;
    for(int i = X; i >= 0; )
      if (c[i] > 0)
      {
        c[i]--;
        for(int j = i; j >= 0; j--)
          if (i+j <= X && c[j] > 0)
          {
            c[j]--;
            break;
          }
        r++;
      }
      else i--;

    printf("Case #%d: %d\n", caso, r);
  }
}
