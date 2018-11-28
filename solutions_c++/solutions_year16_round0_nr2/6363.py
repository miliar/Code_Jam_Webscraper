/*zhen hao*/
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

char str[110];

int slove() {
  int ret = 0, n = strlen(str);
  for (;;) {
    int pos = -1;
    for (int i = 0; i < n; i++) {
      if (str[i] == '-') pos = i;
      str[i] = (str[i] == '+') ? '-' : '+';
    }
    if (pos == -1) break;
    else n = pos;
    ret++;
  }
  return ret;
}

int main() {
//  freopen("B-small-attempt0.in", "r", stdin);
//  freopen("B-large.in", "r", stdin);
//  freopen("case.in", "w", stdout);
  int T, tcase = 0;
  cin >> T;
  while (T--) {
    scanf("%s", str);
    printf("Case #%d: %d\n", ++tcase, slove());
  }
  return 0;
}
