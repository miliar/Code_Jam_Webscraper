#include <cstdio>
#include <algorithm>
using namespace std;

void main2()
{
  int a, b, k;
  scanf("%d%d%d", &a, &b, &k);
  
  int res = 0;
  for (int i=0; i<a; i++)
  for (int j=0; j<b; j++)
    if ((i & j) < k)
      res++;
  printf("%d\n", res);
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
