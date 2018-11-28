#include <bits/stdc++.h>

#define MOD 1000000007

using namespace std;

typedef long long int lld;
typedef pair<int, int> pii;
typedef pair<pii, pii> line;

#define F first
#define S second

char pos[6][6];
char fin[6][6];
int ans, n;
int workers[6], ms[6];

int check_all(int cur, int mask)
{
  if (cur == n)
    return 1;

  int i, fl = 0;
  for (i = 0; i < n; i++)
    if (fin[workers[cur]][i] == '1' && !ms[i])
    {
      fl = 1;
      ms[i] = 1;
      if (!check_all(cur + 1, mask))
        return 0;
      ms[i] = 0;
    }

  return fl;
}

int check(int mask)
{
  int i, j;

  for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
      fin[i][j] = '0' + ((mask & (1 << (i * n + j))) > 0);
  for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
      if (fin[i][j] == '0' && pos[i][j] == '1')
        return 0;

  sort(workers, workers + 4);
  do {
    memset(ms, 0, sizeof ms);
    if (!check_all(0, mask))
      return 0;
  } while (next_permutation(workers, workers + n));

  return 1;
}

int calc()
{
  int i, j;
  int cost = 0;
  for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
      if (fin[i][j] != pos[i][j])
        cost++;
  return cost;
}

void print()
{
  int i, j;
  printf("\n");
  for (i = 0; i < n; i++)
  {
    for (j = 0; j < n; j++)
      printf("%c", fin[i][j]);
    printf("\n");
  }
}

int main()
{
  int t, T, i;
  scanf("%d", &T);

  workers[0] = 0;
  workers[1] = 1;
  workers[2] = 2;
  workers[3] = 3;

  for (t = 1; t <= T; t++)
  {
    scanf("%d", &n);

    for (i = 0; i < n; i++)
      scanf(" %s", pos[i]);

    ans = n * n * n;

    for (i = 0; i < (1 << (n * n)); i++)
      if (check(i))
      {
//        if (calc() == 2)
//          print();
        ans = min(ans, calc());
      }

    printf("Case #%d: %d\n", t, ans);
  }
  
  return 0;
}
