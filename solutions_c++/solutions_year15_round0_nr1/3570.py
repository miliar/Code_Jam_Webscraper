#include<cstdio>
int z, i, n, s, nr, wynik;
char a;

int main()
{
  scanf("%d", &z);
  
  for(nr = 1; nr <= z; nr++)
  {
    scanf("%d", &n);
    s = 0;
    wynik = 0;
    for(i = 0; i <= n; i++)
    {
      scanf(" %c", &a);
      a -= '0';
      if (s < i)
      {
	wynik += i - s;
	s = i;
      }
      s += a;
    }
    printf("Case #%d: %d\n", nr, wynik);
  }
  
return 0;
}