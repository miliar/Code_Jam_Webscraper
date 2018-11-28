/**
* I love coding
* @Author: Jecvay
*/

#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

#define DBG 1
#define ast(b) if(DBG && !(b)) { printf("%d!!|n", __LINE__); system("pause"); }
#define dout DBG && cout << __LINE__ << ">>| "


inline int gint() {int n;scanf("%d", &n);return n;}
inline char gchar() {char c;scanf("%c", &c);return c;}
//////////////////

#define inf 0x4F4F4F4F
const int maxn = 1e5 + 10;
char s[maxn];

/////////////////

int solve(int sm) {
  int re = 0;
  int already = 0;
  for (int i = 0; i < strlen(s); i++) {
    int x = s[i] - '0';
    if (i > already) {
      re += i - already;
      already += i - already;
    }
    already += x;
  }
  return re;
}

int main() {
  int t = gint();
  for (int cas = 1; cas <= t; cas++) {
    int a = gint();
    scanf("%s", s);
    printf("Case #%d: %d\n", cas, solve(a));
  }
  return 0;
}



/*

4
4 11111
1 09
5 110011
0 1

*/
