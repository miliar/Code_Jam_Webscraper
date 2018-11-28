#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory.h>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef long long Int;
typedef pair<int, int> PII;

#define FOR(i, n, m) for(i = n; i < m; ++i)
#define RFOR(i, n, m) for(i = (n) - 1; i >= (m); --i)
#define CLEAR(x, y) memset(x, y, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

Int A[40];

Int cnt(Int h) {
  if (h <= 0)
    return 0;
  Int s = 0;
  for (int i = 0; i < 37; ++i)
    if (h >= A[i])
      s += (h-A[i]);
  return s;
}

Double F(Int h, Int B) {
  //  cout << "F(" << h << ") = ???" << endl;

  if (h <= 0)
    return 0;
  Int c = cnt(h);
  if (c > B)
    return 0;
  Double res = 0;

  Double s = 0;
  int kw = 0;
  for (int i = 0; i < 37; ++i) {
    if (A[i] <= h) {
      s += h-A[i];
      ++kw;
    }
  }
  Int bet = c;
  if (kw == 0)
    return 0;
  Double r = s * 36 / kw - bet;
  if (r > res)
    res = r;

  for (int p = 36; p > 0; --p) {
    if (A[p] > h)
      continue;
    if (bet == B)
      break;
    ++bet;
    s = 0;
    kw = 0;
    for (int i = 0; i < p; ++i)
      if (A[i] <= h) {
	s += h-A[i];
	++kw;
      }
    r = s * 36 / kw - bet;
    if (r > res)
      res = r;
  }

  //  cout << "F(" << h << ") = " << res << endl;
  return res;
}

int main()
{
  int T, t;
  scanf("%d", &T);
  for (t = 0; t < T; ++t) {
    Int B;
    int N;
    scanf("%lld%d", &B, &N);
    int i;
    for (i = 0; i < N; ++i)
      scanf("%lld", &A[i]);
    while (i < 37) {
      A[i] = 0;
      ++i;
    }
    N = 37;

    sort(A, A+N);
    Double res = 0;
    for (i = 0; i < N; ++i) {
      Double r = F(A[i]-1, B);
      if (r > res)
	res = r;
      r = F(A[i], B);
      if (r > res)
	res = r;
    }

    Int lb = 0, ub = 3000000000000LL, cb;
    while (ub - lb > 1) {
      cb = ((ub+lb) >> 1);
      Int c = cnt(cb);
      if (c <= B)
	lb = cb;
      else
	ub = cb;
    }
    Double r = F(lb-1, B);
    if (r > res)
      res = r;
    r = F(lb, B);
    if (r > res)
      res = r;

    printf("Case #%d: %.9lf\n", t+1, (double)res);
    fprintf(stderr, "Case #%d: %.9lf\n", t+1, (double)res);
  }

  return 0;
};
