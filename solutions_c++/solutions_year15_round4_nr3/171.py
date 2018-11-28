#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <map>

using namespace std;

int num, test, n, len[201];
string a[201][1001];
int c[201][1001];
bool v[2][3001];
string str;
map<string, int> events;


inline void insert(int step, int status) {
     for (int i = 1; i <= len[step]; i++) v[status][c[step][i]] = true;
}

int ans() {
     int will = 0;
     for (int i = 1; i <= num; i++)  will += v[0][i] && v[1][i];
     return will;
} 

int main() {
     freopen("c.in", "r", stdin);
     freopen("c.out", "w", stdout);
     scanf("%d", &test);
     for (int uu = 1; uu <= test; uu++) {
          printf("Case #%d: ", uu);
          scanf("%d", &n); events.clear();
          char ch = getchar(); num = 0;
          for (int i = 1; i <= n; i++) {
               getline(cin, str);
               int m = str.size(); len[i] = 0;
               for (int j = 0; j < m; j++) 
                    if (str[j] >= 'a' && str[j] <= 'z') {
                         a[i][++len[i]] = "";
                         for (; j < m && str[j] >= 'a' && str[j] <= 'z'; j++) 
                              a[i][len[i]] += str[j];
                         for (int j = 1; j < len[i]; j++) 
                              if (a[i][j] == a[i][len[i]]) {
                                   --len[i];
                                   break;
                              }
                    }  
               for (int j = 1; j <= len[i]; j++) {
                    if (events.find(a[i][j]) == events.end()) events[a[i][j]] = ++num;
                    c[i][j] = events[a[i][j]];
               }
          }
          int Max = 1 << 30;
         // printf("%d\n", num);
          for (int i = 0; i < 1 << (n - 2); i++) { 
               memset(v, false, sizeof(v));
               insert(1, 0);
               insert(2, 1);
               for (int j = 0; j <= n - 2; j++)
                    if (i & (1 << j)) insert(3 + j, 0);
                    else insert(3 + j, 1);
               Max = min(Max, ans());
          }
          printf("%d\n", Max);
     }
}
          
