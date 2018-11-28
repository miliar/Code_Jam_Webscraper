#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

int test, n, a[1001], f[1111], v[1111];
map<int, int> events;

int main(){
     freopen("b.in", "r", stdin);
     freopen("b.out", "w", stdout);
     scanf("%d", &test);
     for (int uu = 1; uu <= test; uu++)
     {
          printf("Case #%d: ", uu);
          events.clear();
          scanf("%d", &n);
          for (int i = 1; i <= n; i++) scanf("%d", &a[i]), events[a[i]] = i;
          sort(a + 1, a + n + 1);
          int ans = 0;
          for (int i = n; i; --i)
          {
               int A = 0, B = 0;
               for (int j = i + 1; j <= n; j++)
                    if (events[a[j]] < events[a[i]]) ++A;
                    else ++B;
               ans += min(A, B);
          }
          printf("%d\n", ans);
     }
}
                       
