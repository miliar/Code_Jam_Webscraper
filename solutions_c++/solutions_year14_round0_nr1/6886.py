#include <cstdio>
#include <cstring>
const int nmax = 4 + 18, cmax = 16 + 18;

int ans[nmax], tot;
bool ed[cmax];
int n, m, t;

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &t);
  for (int cases = 1; cases <= t; ++cases) {
    tot = 0;
    memset(ed, 0, sizeof(ed));
    scanf("%d", &n);
    int tmp;
    for (int i = 1; i <= 4; ++i)
      for (int j = 1; j <= 4; ++j) {
	scanf("%d", &tmp);
	if (i == n)
	  ed[tmp] = 1;
      }
    tot = 0;
    scanf("%d", &m);
    for (int i = 1; i <= 4; ++i)
      for (int j = 1; j <= 4; ++j) {
	scanf("%d", &tmp);
	if (i == m)
	  if (ed[tmp])
	    ans[++tot] = tmp;
      }
    printf("Case #%d: ", cases);
    if (tot > 1)
      printf("Bad magician!");
    else if (tot == 0)
      printf("Volunteer cheated!");
    else
      printf("%d", ans[1]);
    if (cases < t) printf("\n");
  }
  return 0;
}
