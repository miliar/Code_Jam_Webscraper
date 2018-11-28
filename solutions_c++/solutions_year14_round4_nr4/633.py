#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int test, m, n, a[11], ans, way, f[11][11];
string str[11];

inline void soso(int step){
     if (step == m + 1)
     {
          int now = 0;
          bool ok = true;
          for (int i = 1; i <= n; i++)
          {
               int size = 0;
               for (int j = 1; j <= m; j++)
                    if (a[j] == i)
                    {
                         ++size;
                         int Max = 0;
                         for (int k = 1; k < j; k++)
                              if (a[k] == i) Max = max(Max, f[j][k]);
                         now += str[j].size() - Max;
                    }
               if (!size) return;
          }
          if (now > ans) ans = now, way = 1;
          else if (now == ans) ++way;
          return;
     }
     for (int i = 1; i <= n; i++) 
     {
          a[step] = i;
          soso(step + 1);
     }
}

int main(){
     freopen("d.in", "r", stdin);
     freopen("d.out", "w", stdout);
     scanf("%d", &test);
     for (int uu = 1; uu <= test; uu++)
     {
          printf("Case #%d: ", uu);
          scanf("%d%d", &m, &n);
          for (int i = 1; i <= m; i++) cin >> str[i];
          for (int i = 1; i <= m; i++)
               for (int j = 1; j < i; j++)
               {
                    f[i][j] = 0;
                    for (int k = 0; k < str[i].size() && k < str[j].size(); k++)
                         if (str[i][k] == str[j][k]) ++f[i][j];
                         else break;
               }
          ans = 0; way = 0;
          soso(1);
          printf("%d %d\n", ans + n, way);
     }
}
