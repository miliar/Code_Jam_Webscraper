#include <cstdio>
#include <algorithm>
using std::max;

int a[100][100];
int r[100];
int c[100];

bool run()
{
  int n,m;
  scanf("%d%d",&n,&m);

  for (int i=0; i<n; i++)
    r[i] = 0;
  for (int j=0; j<m; j++)
    c[j] = 0;

  for (int i=0; i<n; i++)
    for (int j=0; j<m; j++) {
      scanf("%d",&a[i][j]);
      r[i] = max(r[i], a[i][j]);
      c[j] = max(c[j], a[i][j]);
    }
  for (int i=0; i<n; i++)
    for (int j=0; j<m; j++) 
      if (a[i][j] < r[i] && a[i][j] < c[j])
	return false;
  return true;
}

int main()
{
  int t;
  scanf("%d",&t);
  for (int tc=1; tc<=t; tc++) {
    if (run())
      printf("Case #%d: YES\n",tc);
    else
      printf("Case #%d: NO\n",tc);
  }
}
