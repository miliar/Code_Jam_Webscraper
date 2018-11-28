#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

const int nmax = 25 + 18, vmax = 1 << 10;

int ab[nmax];
int ans, n;
bool suc;

void search2(int id, int mask, int theone)
{
  // printf("%d %d %d\n", id, mask, theone);
  if (suc) {
    return;
  }
  if (id > n) {
    // printf("mask %d %d\n", mask, ab[theone]);
    if ((mask | ab[theone]) == mask) {
      suc = 1;
    }
    return;
  }
  if (ab[id] == 0) {
    suc = 1;
    return;
  }
  if (id == theone)
    search2(id + 1, mask, theone);
  else {
    for (int j = 1; j <= n; ++j)
      if (ab[id] & (1 << (j - 1)))
        search2(id + 1, mask | (1 << (j - 1)), theone);
  }
}

bool check()
{
  // printf("check\n");
  // for (int i = 1; i <= n; ++i)
  //   printf("%d\n", ab[i]);
  // printf("0-------\n");
  for (int i = 1; i <= n; ++i) {
    suc = 0;
    search2(1, 0, i);
    if (suc) {
      // printf("fail at %d\n", i);
      return 0;
    }
    // if (ab[i] == (1 << n) - 1) continue;
    // mask[i] = 0;
    // for (int j = 1; j <= n; ++j)
    //   if (i != j)
    //     mask[i] |= ab[j];
    // printf("mask %d: %d %d %d\n", i, mask[i], ab[i], ab[i] | mask[i] == mask[i]);
    // if ((ab[i] | mask[i]) == mask[i]) return 0;
  }
  return 1;
}

void search(int id, int mid, int cst)
{
  if (cst >= ans)
    return;
  if (id > n) {
    // printf("%d\n", cst);
    if (check()) {
      // printf("update\n");
      ans = cst;
    }
    return ;
  }
  if (mid > n) {
    search(id + 1, 1, cst);
    return ;
  }
  // printf("%d: %d %d\n", id, ab[id], 1 << (mid - 1));
  if (ab[id] & (1 << (mid - 1)))
    search(id, mid + 1, cst);
  else {
    search(id, mid + 1, cst);
    ab[id] |= 1 << (mid - 1);
    search(id, mid + 1, cst + 1);
    ab[id] ^= 1 << (mid - 1);
  }
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int cases = 1; cases <= T; ++cases) {
    scanf("%d", &n);
    ans = n * n;
    for (int i = 1; i <= n; ++i) {
      char str[nmax];
      scanf("%s", str + 1);
      ab[i] = 0;
      for (int j = 1; j <= n; ++j)
        if (str[j] == '1')
          ab[i] |= 1 << (j - 1);
      // printf("%d: %d\n", i, ab[i]);
    }
    search(1, 1, 0);
    printf("Case #%d: %d\n", cases, ans);
  }
  return 0;
}
