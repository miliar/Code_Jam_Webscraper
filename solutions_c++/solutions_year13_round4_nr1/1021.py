#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

typedef long long huge;

#define MOD 1000002013LL
#define MAX 1024

int N,M,o[MAX],e[MAX],p[MAX];

#define P(_o, _e) ((_o) == (_e) ? 0 : PD((_e)-(_o)))
#define PD(_d) ((_d)*N - (((_d)*(_d-1))/2))

int main(void)
{
  int T;

  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++)
  {
    printf("Case #%d: ", caso);

    scanf("%d %d", &N, &M);
    for(int i = 0; i < M; i++)
      scanf("%d %d %d", o+i, e+i, p+i);

    huge r = 0;

    while(1)
    {
      int x,y;
      huge b = -1;

      for(int j = 0; j < M; j++)
        if (p[j] > 0)
        {
          huge pj = P(o[j], e[j]);
          for(int k = 0; k < M; k++)
            if (p[k] > 0 && o[k] > o[j] && o[k] <= e[j])
            {
              huge pk = P(o[k], e[k]);

              huge novo = P(o[k], e[j]);
              novo += P(o[j], e[k]);

              //printf("[%d %d] = (%lld %lld)", j,k,novo,pj+pk);
              huge mp = (huge)min(p[j],p[k]);
              huge nb = ((huge)(pj+pk)-novo)*mp;
              if (nb > 0 && nb > b)
              {
                b = nb;
                x = j;
                y = k;
              }
            }
          }

      //printf("\n");
      if (b > 0)
      {
        //r = (r+(b%MOD))%MOD;
        r += b;
        int menor = min(p[x], p[y]);
        p[x] -= menor;
        p[y] -= menor;

        o[M] = o[y];
        e[M] = e[x];
        p[M++] = menor;

        o[M] = o[x];
        e[M] = e[y];
        p[M++] = menor;
      }
      else break;
    }

    printf("%lld\n", r);
  }
}
