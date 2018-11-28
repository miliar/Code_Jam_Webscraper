#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

const int infinity = 1e9 + 9;

int N;
double V, X;
double R[109];
double C[109];

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input
    scanf("%d %lf %lf", &N, &V, &X);
    for (int n = 0; n < N; ++n)
      scanf(" %lf %lf", &R[n], &C[n]);
    
    // Case N = 1
    if (N == 1)
    {
      if (X == C[0])
        printf("Case #%d: %lf\n", Ti, V / R[0]);
      else
        printf("Case #%d: IMPOSSIBLE\n", Ti);
      continue;
    }
    
    // Case N <= 2
    if (N == 2)
    {
      if ((C[0] == C[1]) && (C[0] == X))
        printf("Case #%d: %lf\n", Ti, V / (R[0] + R[1]));
      else if (C[0] == C[1])
        printf("Case #%d: IMPOSSIBLE\n", Ti);
      else
      {
        double y = (X * V - C[1] * V) / (C[0] - C[1]);
        if (y < 0 || y > V)
          printf("Case #%d: IMPOSSIBLE\n", Ti);
        else
          printf("Case #%d: %lf\n", Ti, max(y / R[0], (V - y) / R[1]));
      }
      continue;
    }
    
    
    // output
    printf("Case #%d: NOT IMPLEMENTED\n", Ti);
  }
  return 0;
}
