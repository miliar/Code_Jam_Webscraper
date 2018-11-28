#include <cstdio>
#include <algorithm>
using namespace std;

const int infinity = 1e9 + 9;

int D;
int P[1009];

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input
    scanf("%d", &D);
    for (int i = 0; i < D; ++i)
      scanf("%d", &P[i]);
    
    // solve
    int y = infinity;
    for (int e = 1; e <= 1000; ++e)
    {
      int time = e;
      for (int i = 0; i < D; ++i)
        time += (P[i] - 1) / e;
      y = min(y, time);
    }
    
    // output
    printf("Case #%d: %d\n", Ti, y);
  }
  return 0;
}
