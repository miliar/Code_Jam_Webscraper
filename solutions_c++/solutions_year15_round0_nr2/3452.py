#include<cstdio>
int z, n, i, j, nr, mn, wynik, t[1001];

int main()
{
  scanf("%d", &z);
  
  for(nr = 1; nr <= z; nr++)
  {
    scanf("%d", &n);
    
    for(i = 0; i < n; i++)
    {
      scanf("%d", &t[i]);
    }
    
    mn = 1000;
    
    for(i = 1; i <= 1000; i++)
    {
      wynik = i;
      for(j = 0; j < n; j++)
      {
	if (t[j] > i)
	{
	  if (t[j] % i == 0)
	  {
	    wynik--;
	  }
	  wynik += t[j] / i;
	}
      }
      if (wynik < mn)
      {
	mn = wynik;
      }
    }
    printf("Case #%d: %d\n", nr, mn);
  }
  
return 0;
}