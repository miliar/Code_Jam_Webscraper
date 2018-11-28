#include <cstdio>
#include <algorithm>
using namespace std;

void main2()
{
  int N;
  scanf("%d", &N);
  
  double naomi[N], ken[N];
  for (int i=0; i<N; i++)
    scanf("%lf", &naomi[i]);
  for (int i=0; i<N; i++)
    scanf("%lf", &ken[i]);
  
  sort(naomi, naomi+N);
  sort(ken, ken+N);
  
  int resA = 0;
  int inf=0;
  for (int i=0; i<N; i++)
  {
    if (naomi[i] > ken[inf])
    {
      resA++;
      inf++;
    }
  }
  
  int resB = 0;
  for (int i=0; i<N; i++)
  {
    bool tmp = false;
    for (int j=0; j<N; j++)
      if (!tmp && ken[j] > naomi[i])
      {
        tmp = true;
        ken[j] = -1;
      }
    if (!tmp) resB++;
  }
  
  printf("%d %d\n", resA, resB);
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
