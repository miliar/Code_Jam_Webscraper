#include <cstdio>
#include <algorithm>

using namespace std;

const int max_n = 2000;

double nw[max_n], kw[max_n];
int n;

int bestup()
{
  int ni = 0;
  int ki = 0;
  int sc = 0;

  while((ni<n) && (ki<n)) {
    if(nw[ni] > kw[ki]) {
      sc++;
      ni++;
      ki++;
    } else
      ni++;
  }
  return sc;
}

int bestwar()
{
  int sc = 0;
  int gi;
  
  for(int i=0; i<n; i++) {
    gi = -1;
    for(int j=0; j<n; j++)
      if((kw[j] >= 0) && (kw[j] > nw[i])) {
        gi = j;
        break;
      }
    if(gi >= 0) {
      kw[gi] = -1;
      continue;
    }
    for(int j=0; j<n; j++)
      if(kw[j] >= 0) {
        gi = j;
        break;
      }
    kw[gi] = -1;
    sc++;
  }
  return sc;
}

void solve(int tt)
{
  scanf("%d",&n);
  for(int i=0; i<n; i++)
    scanf("%lf",&nw[i]);
  for(int i=0; i<n; i++)
    scanf("%lf",&kw[i]);

  sort(nw,nw+n);
  sort(kw,kw+n);
  int dsc = bestup();
  printf("Case #%d: %d %d\n",tt+1, dsc, bestwar());
}

main()
{
  int t;
  scanf("%d",&t);
  for(int tt=0; tt<t; tt++)
    solve(tt);
}
