#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
#include <vector>
using namespace std;

const int maxn = 2000 + 10;
char st[maxn];
int s;

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("A_large.out", "w", stdout);
  int TextN;
  scanf("%d", &TextN);
  for (int TT = 1; TT <= TextN; TT++) {
    scanf("%d%s", &s, st);
    
    int ans = 0, cur = 0;
    for (int i = 0; i <= s; i++) {
      while (st[i] != '0' && cur < i) {
        cur += 1;
        ans += 1;
      }
      cur += st[i] - '0';
    } 
    printf("Case #%d: %d\n", TT, ans);
  }
  return 0;
}