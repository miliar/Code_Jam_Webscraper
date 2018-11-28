#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

#define MAXN 1005
#define EPS 1e-8

char num[MAXN];

int main() {
  int T;
  scanf("%d", &T);
  for (int nCase = 1; nCase <= T; ++nCase) {
    int smax;
    scanf("%d %s", &smax, num);
    int cur = 0;
    int need = 0;
    for (int i = 0; i <= smax; ++i) {
      if (cur >= i) {
        cur += num[i] - '0';
      } else {
        need += i - cur;
        cur = i + num[i] - '0';
      }
    }
    printf("Case #%d: %d\n", nCase, need);
  }
  return 0;
}

