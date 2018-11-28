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

Double R[1<<20];
bool RU[1<<20];
int N;

Double F(int mask) {
  Double &res = R[mask];
  if (RU[mask])
    return res;
  res = 0;
  RU[mask] = 1;
  if (mask == (1<<N) - 1)
    return res;
  for (int i = 0; i < N; ++i)
    if ((mask & (1<<i)) == 0) {
      res += N + F(mask | (1<<i));
      int p = i-1;
      if (p < 0)
	p = N-1;
      int k = 1;
      while (mask & (1<<p)) {
	res += N-k + F(mask | (1<<i));
	++k;
	--p;
	if (p < 0)
	  p = N-1;
      }
    }
  res /= N;
  return res;
}

char buf[3000];

int main()
{
  int T, t;
  scanf("%d", &T);
  for (int t = 0 ;t < T; ++t) {
    scanf("%s", buf);
    N = strlen(buf);
    int mask = 0;
    CLEAR(RU, 0);
    for (int i = 0; i < N; ++i)
      if (buf[i] == 'X')
	mask |= 1<<i;
    double res = F(mask);
    printf("Case #%d: %.12lf\n", t+1, res);
    fprintf(stderr, "Case #%d: %.12lf\n", t+1, res);
  }

  return 0;
};
