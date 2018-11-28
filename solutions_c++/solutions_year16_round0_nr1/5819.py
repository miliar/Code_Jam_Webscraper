#include <bits/stdc++.h>

using namespace std;

int main()
{
  int t;
  scanf("%d",&t );
  for(int i = 0 ; i < t ; i++)
  {
    set < int > digitos;
    int n;
    scanf("%d",&n);
    int copiaN = n;
    int cont = 2;
    if(n == 0)
    {
      printf("Case #%d: INSOMNIA\n",i+1);
      continue;
    }
    while(digitos.size() != 10)
    {
      while(n != 0)
      {
        digitos.insert(n%10);
        n/=10;
      }
      if(digitos.size() == 10)
        break;
      n = copiaN * cont;
      cont++;
    }
    printf("Case #%d: %d\n",i+1,copiaN*(cont-1) );
  }
  return 0;
}
