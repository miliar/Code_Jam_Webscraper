#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;
#define N 105

int n , m , a[N][N] , ca;

void work()
{
  int i , j , k;
  scanf("%d%d",&n ,&m);
  for (i = 1 ; i <= n ; ++ i)
    for (j = 1 ; j <= m ; ++ j)
      scanf("%d",&a[i][j]);
  for (i = 1 ; i <= n ; ++ i)
    for (j = 1 ; j <= m  ; ++ j)
    {
      bool f1 = 0 , f2 = 0;
      for (k = 1 ; k <= m ; ++ k)
        f1 |= (a[i][k] > a[i][j]);
      for (k = 1 ; k <= n ; ++ k)
        f2 |= (a[k][j] > a[i][j]);
      if (f1 && f2)
        goto hehehe;
    }
  hehehe:
  printf("Case #%d: " , ++ ca);
  if (i <= n)
    puts("NO");
  else puts("YES");
}

int main()
{
  freopen("~input.txt" , "r", stdin);
  freopen("~output.txt" , "w", stdout);
  int _;cin>>_;while(_--)
    work();
  return 0;
}
