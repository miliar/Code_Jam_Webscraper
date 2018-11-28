#include <cmath>
#include <set>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <cstring>
#include <cctype>
#include <string>
#include <sstream>
#include <stack>
#include <queue>

using namespace std;

#define maxn 100

bool isPossible(int l[][maxn + 1], int n, int m) {
  char f[maxn][maxn + 1];
  memset(f, 0, sizeof (f));

  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
      int in = 0;
      while (in < n && l[in][j] <= l[i][j]) in++;

      int im = 0;
      while (im < m && l[i][im] <= l[i][j]) im++;

      if (!(in == n || im == m)) return false;
    }

  return true;
}

int main() {
  int t;
  scanf("%d", &t);

  int n, m;
  int l[maxn][maxn + 1];

  for (int it = 0; it < t; it++) {
    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++)
        scanf("%d", &l[i][j]);

    printf("Case #%d: ", it + 1);

    if (isPossible(l, n, m)) puts("YES");
    else puts("NO");
  }

  return 0;
}
