#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;
const int nmax = 10000 + 18;


int a[2][nmax];
int n, P, R, S, ni, nn;
char ans[nmax], v[nmax];
bool bans;

bool check(int x)
{
  // printf("check\n");
  ni = 0, nn = 1;
  a[ni][1] = x;
  for (int i = 1; i <= n; ++i) {
    int pi = ni ^ 1, pn = nn << 1;
    for (int j = 1; j <= nn; ++j) {
      int y = a[ni][j];
      a[pi][j * 2 - 1] = y;
      a[pi][j * 2] = (y + 1) % 3;
    }
    nn = pn, ni = pi;
  }
  int p, r, s;
  p = r = s = 0;
  for (int i = 1; i <= nn; ++i)
    if (a[ni][i] == 0)
      ++p;
    else if (a[ni][i] == 1)
      ++r;
    else
      ++s;
  if (p != P || r != R || s != S)
    return 0;
  return 1;
}

void swap(int &a, int &b)
{
  int k = a;
  a = b;
  b = k;
}

void adjust(int step)
{
  // printf("adjust: %d\n", step);
  // for (int i = 1; i <= nn; ++i)
  //   printf("%d", a[ni][i]);
  // printf("\n");
  int li = 1, ri = li + step;
  while (li <= nn) {
    // printf("(%d, %d)\n", li, ri);
    bool smaller = 0;
    for (int i = 0; i < step; ++i)
      if (a[ni][i + li] > a[ni][i + ri]) {
        smaller = 1;
        break;
      }
    if (smaller)
      for (int i = 0; i < step; ++i)
        swap(a[ni][i + li], a[ni][i + ri]);
    li += 2 * step;
    ri += 2 * step;
  }
}

void update()
{
  // printf("update\n");
  int step = 1;
  for (int i = 1; i <= n; ++i, step <<= 1)
    adjust(step);
  if (!bans) {
    bans = 1;
    for (int i = 1; i <= nn; ++i)
      ans[i] = v[a[ni][i]];
  }
  else {
    bool smaller = 0;
    for (int i = 1; i <= nn; ++i)
      if (ans[i] > v[a[ni][i]]) {
        smaller = 1;
        break;
      }
    if (smaller)
      for (int i = 1; i <= nn; ++i)
        ans[i] = v[a[ni][i]];
  }

}

int main()
{
  v[0] = 'P', v[1] = 'R', v[2] = 'S';
  int T;
  scanf("%d", &T);
  for (int cases = 1; cases <= T; ++cases) {
    scanf("%d%d%d%d", &n, &R, &P, &S);
    printf("Case #%d: ", cases);
    bool suc = 0;
    bans = 0;
    if (check(0)) suc = 1, update();
    if (check(1)) suc = 1, update();
    if (check(2)) suc = 1, update();
    if (suc) {
      for (int i = 1; i <= R + P + S; ++i)
        printf("%c", ans[i]);
    }
    else
      printf("IMPOSSIBLE");
    printf("\n");

  }
  return 0;
}
