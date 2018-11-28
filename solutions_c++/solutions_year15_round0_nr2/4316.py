#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;
int r;

void dfs(int curr, vector<int> &P)
{
  sort(P.rbegin(), P.rend());
  r = min(r, curr+P[0]);

  if (curr < P[0])
  {
    int p0 = P[0];
    for(int i = 1; i <= p0/2; i++)
    {
      vector<int> p;
      for(int j = 0; j < (int)P.size(); j++)
        p.push_back(P[j]);
      //if (i > p[(int)p.size()-1])
        p.push_back(i);
      p[0] = P[0]-i;
      dfs(curr+1, p);
    }
  }
}

int main(void)
{
  int T;

  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++)
  {
    int D;
    vector<int> P;
    scanf("%d", &D);
    for(int i = 0; i < D; i++)
    {
      int x;
      scanf("%d", &x);
      P.push_back(x);
    }
    r = 1024;
    dfs(0, P);

    printf("Case #%d: %d\n", caso, r);
  }
}
