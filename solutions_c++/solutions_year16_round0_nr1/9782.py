#include <bits/stdc++.h>

using namespace std;

int main() 
{
  freopen("A.in", "r", stdin);
  freopen("out", "w", stdout);
  int tt,qq;
  scanf("%d", &tt);
  for (qq = 1; qq <= tt; qq++) 
  { 
    int c[10]={0},n;
    scanf("%d",&n);
    int m = n;
    int k,co = 0,i=1;
    while(m <=1000000)
    {
      if(m==0)
        break;
      while(m) 
      {
          k = m%10;
          if(c[k]==0)
          {
            co++;
            c[k]++;
          }
          m /= 10;
      }
      m = n;
      if(co==10)
        break;
      i++;
      m *= i;
    }
    printf("Case #%d: ", qq);
    
    if(co==10)
      printf("%d\n", i*m);
    else
      printf("INSOMNIA\n");
  }

  return 0;
}