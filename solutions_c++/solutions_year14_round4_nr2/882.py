#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()

using namespace std;
typedef long long ll;

void testCase()
{
  int n;
  scanf("%d", &n);
  vector<int> a(n);
  vector<int> p(n);
  for (int i = 0; i < n; i++)
    scanf("%d", &a[i]), p[i] = i;
  vector<int> u(n);

  int ans = n * (n - 1) / 2; // +inf
  do {
    for (int i = 0; i < n; i++)
      u[i] = a[p[i]];

    int i = 0;
    for (; i < n - 1 && u[i] < u[i + 1]; i++)
      ;
    for (; i < n - 1 && u[i] > u[i + 1]; i++)
      ;
    if (i != n - 1)
      continue;

    for (int i = 0; i < n; i++)
      u[i] = p[i];

    int swaps = 0;
    for (int i = 0; i < n - 1; i++)
      for (int j = 0; j < n - 1; j++)
        if (u[j] > u[j + 1])
        {
          swap(u[j], u[j + 1]);
          swaps++;
        }
    ans = min(ans, swaps);

  } while (next_permutation(all(p)));
  printf("%d\n", ans);
}

int main() {
//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  int T;
//  cin >> T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
//    cout << "Case #" << t << ": ";
    printf("Case #%d: ", t);
    testCase();
  }
  return 0;
}
