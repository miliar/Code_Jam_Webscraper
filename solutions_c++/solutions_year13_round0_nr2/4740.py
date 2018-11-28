#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int a[102][102],n,m;
int r[102],c[102];

void init()
{
  scanf("%d %d", &n, &m);
  memset(r, 0, sizeof(r));
  memset(c, 0, sizeof(c));

  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
	scanf("%d", &a[i][j]);
  for (int i = 0; i < n; i++)
    for (int j = 0;j < m; j++)
      {
	r[i] = max(r[i], a[i][j]);
	c[j] = max(c[j], a[i][j]);
      }
}

bool check()
{
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      if (a[i][j] < r[i] && a[i][j] <c[j]) return false;
  return true;
}

int main()
{ 
  int T;
  scanf("%d",&T);
  for (int t = 1; t <= T; t++)
    {
      init();
      printf("Case #%d: ",t);
      if (check()) printf("YES\n");
      else printf("NO\n");
    }
  return 0;
}
