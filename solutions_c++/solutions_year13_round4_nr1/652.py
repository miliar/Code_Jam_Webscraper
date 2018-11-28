#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
using namespace std;

#define max2(a,b) (((a) > (b)) ? (a) : (b))
#define min2(a,b) (((a) < (b)) ? (a) : (b))

#define debug(x) cout << (#x) << ": " << (x) << endl
#define echo(x) cout << (#x) << endl
#define TIMER_A(timer) int timer = clock()
#define TIMER_B(timer) cerr << (#timer) << ": " << (double)(clock() - timer) / CLOCKS_PER_SEC << endl

typedef long long LL;
const double eps = 1e-9;
const double pi = M_PI;
const int inf = 2000000000; // 2e9
const LL inf64 = 9000000000000000000LL; // 9e18

const int maxM = 1000;
const int maxL = maxM * 2;

const int MOD = 1000002013;

int TN, TC;

int N, M;

int start[maxM];
int stop[maxM];
int pass[maxM];

int L;
int vp[maxL];
LL cum[maxL];

int S;
int stx[maxL];
LL totpass[maxL];

void input ()
{
  scanf("%d%d", &N, &M);
  for (int i = 0; i < M; ++i)
    scanf("%d%d%d", &start[i], &stop[i], &pass[i]);
}

int findIdx (int pos)
{
  for (int i = 0; i < L; ++i)
    if (vp[i] == pos)
      return i;
  return -1;
}

int calcCost (int np)
{
  return ((2 * (unsigned long long)N + 1 - np) * np / 2) % MOD;
}

void solve ()
{
  memcpy(vp, start, sizeof(int) * M);
  memcpy(vp + M, stop, sizeof(int) * M);
  L = M * 2;
  sort(vp, vp + L);
  L = unique(vp, vp + L) - vp;

  memset(cum, 0, sizeof(LL) * L);
  for (int i = 0; i < M; ++i)
  {
    int a = findIdx(start[i]);
    int b = findIdx(stop[i]);
    for (int j = a; j < b; ++j)
      cum[j] += pass[i];
  }

  int cost1 = 0;
  for (int i = 0; i < M; ++i)
    cost1 = (cost1 + (LL)calcCost(stop[i] - start[i]) * pass[i] % MOD) % MOD;

  int cost2 = 0;
  S = 0;
  LL cur = 0;
  for (int i = 0; i < L - 1; ++i)
  {
    if (cum[i] > cur)
    {
      stx[S] = i;
      totpass[S] = cum[i] - cur;
      ++S;
      cur = cum[i];
    }
    else
    {
      while (cur > cum[i])
      {
        LL chx = min2(totpass[S - 1], cur - cum[i]);
        cost2 = (cost2 + (LL)calcCost(vp[i] - vp[stx[S - 1]]) * (chx % MOD) % MOD) % MOD;
        totpass[S - 1] -= chx;
        if (totpass[S - 1] == 0)
          --S;
        cur -= chx;
      }
    }
  }
  while (S > 0)
  {
    LL chx = totpass[S - 1];
    cost2 = (cost2 + (LL)calcCost(vp[L - 1] - vp[stx[S - 1]]) * (chx % MOD) % MOD) % MOD;
    --S;
  }

  int loss = (cost1 - cost2 + MOD) % MOD;
  printf("%d\n", loss);
}

int main ()
{
  scanf("%d ", &TN);
  for (TC = 1; TC <= TN; ++TC)
  {
    input();
    printf("Case #%d: ", TC);
    solve();
  }
}
