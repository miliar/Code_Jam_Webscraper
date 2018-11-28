#include <cstdio>
#include <algorithm>
using namespace std;

void main2()
{
  double C, F, X;
  scanf("%lf%lf%lf", &C, &F, &X);
  
  int n = X / C - 2. / F;
  if (n < 0) n = 0;
  
  double res = X / (2. + n*F);
  for (int i=0; i<n; i++)
    res += C / (2 + i*F);
  
  printf("%.9lf\n", res);
}

int main()
{
  int N;
  scanf("%d", &N);
  
  for (int i=0; i<N; i++)
  {
    printf("Case #%d: ", i+1);
    main2();
  }
}
