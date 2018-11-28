#include<cstdio>
#include<algorithm>
using namespace std;
const int N = 1e4 + 1;
int z, n, nr, i, mx, wynik, t[N];

int main()
{
  scanf("%d", &z);
  
  for(nr = 1; nr <= z; nr++)
  {
    scanf("%d", &n);
    mx = 0;
    wynik = 0;
    for(i = 0; i < n; i++)
    {
      scanf("%d", &t[i]);
      mx = max(mx, t[i - 1] - t[i]);
      if (i > 0 && t[i - 1] > t[i])
      {
	wynik += t[i - 1] - t[i];
      }
    }
    printf("Case #%d: %d ", nr, wynik);
    wynik = 0;
    for(i = 0; i < n - 1; i++)
    {
      wynik += min(mx, t[i]);
    }
    printf("%d\n", wynik);
  } 
  
return 0;
}