#include <cstdio>
#include <algorithm>
using namespace std;

long long int gcd(long long int a, long long int b)
{
  if (b == 0) return a;
  if (a >= b)
    return gcd(b, a % b);
  else
    return gcd(b, a);
}

void main2()
{
  long long int P, Q;
  scanf("%lld/%lld", &P, &Q);
  
  long long int A, B;
  A = P / gcd(P, Q);
  B = Q / gcd(P, Q);
  
  if (gcd (B, 1ll<<40) != B)
  {
    printf("Impossible\n");
    return;
  }
  
  int n = 0;
  long long int res = (1ll << 40) / B;
  while (res/2 > 0)
  {
    n++;
    res /= 2;
  }
  
  res *= A;
  
  while (res/2 > 0)
  {
    n++;
    res /= 2;
  }
  
  printf("%d\n", 40 - n);
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
