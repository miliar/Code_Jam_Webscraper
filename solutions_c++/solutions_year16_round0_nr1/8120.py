#include <cstdio>
#include <iostream>

using namespace std;

int i, cases;
int done[1000005][15];

int main()
{
  scanf("%d", &cases);
  for(int q=1; q<=cases; q++)
  {
    scanf("%d", &i);
    if(!i)
    {
      printf("Case #%d: INSOMNIA\n", q);
      continue;
    }
    for(int j=i; j; j+=i)
    {
      for(int c=j; c; c/=10)
        done[i][c%10]=1;
      int d=1;
      for(int k=0; k<10; k++)
        if(!done[i][k])
          d=0;
      if(d)
      {
        printf("Case #%d: %d\n", q, j);
        break;
      }
    }
  }
}
