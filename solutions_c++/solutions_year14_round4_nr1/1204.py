#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <cmath>
#include <queue>
#include <algorithm>

using namespace std;

typedef unsigned long long int ull;
typedef long long int ll;

int files[100000];
int used[100000];

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("A-result-big.txt", "w", stdout);
  int T = 0;
  scanf("%d", &T);

  for (int i = 0; i < T; ++i)
  {
    int n, x;
    scanf("%d%d", &n, &x);
    for (int j = 0; j < n; ++j)
    {
      scanf("%d", &files[j]);
      used[j] = 0;
    }

    sort(files, files + n);

    int count = 0;

    for (int i = 0; i < n; ++i)
    {
      if (used[i])
        continue;

      int ind = n - 1;
      while (ind > i && (used[ind] || files[ind] + files[i] > x))
        --ind;

      if (ind != i)
      {
        used[ind] = 1;
      }
        count++;
        used[i] = 1;
    }

    printf("Case #%d: %d", i + 1, count);



    printf("\n");
  }

  fclose(stdin);
  fclose(stdout);

  return 0;
}