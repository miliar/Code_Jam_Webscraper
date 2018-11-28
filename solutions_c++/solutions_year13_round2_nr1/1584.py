#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define N 2052
int n , a[N] , m , ca;


int dfs(int i , int v)
{
  if (i > n) return 0;
  if (v > a[i])
    return dfs(i + 1 , v + a[i]);
  else
  {
    int x = 0 , y , p , q;
    if (v == 1)
      p = 1 << 30;
    else
    {
      y = v;
      while (y <= a[i]) y += y - 1 , ++ x;
      p = dfs(i + 1 , y + a[i]) + x;
    }
    q = dfs(i + 1 ,  v) + 1;
    return min(p , q);
  }
}

void work()
{
  int ans = 0 , i , x , y;
  scanf("%d%d",&m,&n);
  for (i = 1 ; i <= n ; ++ i)
    scanf("%d",&a[i]);
  sort(a + 1 , a + n + 1);
  printf("Case #%d: %d\n" , ++ ca , dfs(1 , m));
}

int main()
{
  freopen("~input.txt","r",stdin);
  freopen("~output.txt","w",stdout);
  int _;cin >> _;while(_--)
  //while (~scanf("%d",&n))
    work();
  return 0;
}
