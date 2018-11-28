#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int test, c[1000001], cnt;
char str[1000001];

int main() {
     freopen("a.in", "r", stdin);
     freopen("a.out", "w", stdout);
     scanf("%d", &test);
     for (int uu = 1; uu <= test; uu++) {
          printf("Case #%d: ", uu);
          scanf("%s", str);
          int n = strlen(str);
          cnt = 0;
          int ans = 0;
          for (int i = 0; i < n; i++) 
               if (cnt && c[cnt] == str[i]) ans += 10, --cnt;
               else c[++cnt] = str[i];
          if (cnt > 1) ans += (cnt + 1) / 2 * 5;
          printf("%d\n", ans);
     }     
}
 
