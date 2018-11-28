#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int test, f[21][10001];
char str[10001];

int main() {
     freopen("a.in", "r", stdin);
     freopen("a.out", "w", stdout);
     scanf("%d", &test);
     for (int uu = 1; uu <= test; uu++) {
          printf("Case #%d: ", uu);  
          int n, R, P, S;
          scanf("%d%d%d%d", &n, &R, &P, &S);
          bool ok = false;
          for (int i = 0; i < 3 && !ok; i++) {
               f[0][0] = i;
               for (int j = 0; j < n; j++)
                    for (int k  = 0; k < 1 << j; k++) 
                         f[j + 1][k + k] = f[j][k],
                         f[j + 1][k + k + 1] = (f[j][k] + 1) % 3;
               int rr = 0, rp = 0, rs = 0;
               for (int k = 0; k < 1 << n; k++)
                    if (f[n][k] == 0) ++rr;
                    else if (f[n][k] == 1) ++rs;
                    else ++rp;
               if (R == rr && S == rs && P == rp) {
                    string str = "";
                    for (int k = 0; k < 1 << n; k++) 
                         if (f[n][k] == 0) str += 'R';
                         else if (f[n][k] == 1) str += 'S';
                         else str += 'P';
                    for (int j = 1; j <= n; j++)
                         for (int k = 0; k < 1 << n; k += 1 << j) {
                              string str1 = "", str2 = "";
                              for (int l = k; l < k + (1 << (j - 1)); l++)
                                   str1 += str[l];
                              for (int l = k + (1 << (j - 1)); l < k + (1 << j); l++)
                                   str2 += str[l];
                              if (str1 > str2)
                                   for (int l = k, x = k + (1 << (j - 1)); l < k + (1 << (j - 1)); ++l, ++x)
                                        swap(str[l], str[x]);
                         }
                    cout << str;
                    printf("\n");
                    ok = true;
               }
          }
          if (!ok) printf("IMPOSSIBLE\n");
     }
}
