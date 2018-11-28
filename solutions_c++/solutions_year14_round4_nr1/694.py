#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int test, n, m, a[10001];
bool b[10001];

int main(){
     freopen("a.in", "r", stdin);
     freopen("a.out", "w", stdout);
     scanf("%d", &test);
     for (int uu = 1; uu <= test; uu++)
     {
          printf("Case #%d: ", uu);
          scanf("%d%d", &n, &m);
          memset(b, false, sizeof(b));
          for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
          sort(a + 1, a + n + 1);
          int ans = n;
          for (int i = 1; i <= n; i++)
          {
               bool ok = false;
               for (int j = n; j > i; --j)
                    if (!b[j] && a[i] + a[j] <= m)
                    {
                         ok = true;
                         --ans;
                         b[j] = true;
                         break;
                    }
               if (!ok) break;
          }
          printf("%d\n", ans);               
     }
}
