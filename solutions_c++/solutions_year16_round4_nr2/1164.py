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

Double R[210][210];
double P[210];

int countt(int mask) {
  int k = 0;
  while (mask) {
    mask &= (mask-1);
    ++k;
  }
  return k;
}

int main()
{
  int T, t;
  scanf("%d", &T);
  for (t = 0; t < T; ++t) {
    int N, K;
    scanf("%d%d", &N, &K);
    for (int i = 0; i < N; ++i)
      scanf("%lf", &P[i]);
    sort(P, P+N);
    double res = 0;
    for (int mask = 0; mask < (1<<N); ++mask) {
      if (countt(mask) != K)
	continue;
      vector<double> p;
      for (int i = 0; i < N; ++i)
	if (mask & (1<<i))
	  p.PB(P[i]);
      for (int i = 0; i <= K; ++i)
	for (int y = 0; y <= K; ++y)
	  R[i][y] = 0;
      R[0][0] = 1;
      for (int i = 0; i < K; ++i) {
	for (int y = 0; y <= i; ++y) {
	  R[i+1][y] += R[i][y] * (1 - p[i]);
	  R[i+1][y+1] += R[i][y] * p[i];
	}
      }
      double cr = R[K][K/2];
      res = max(res, cr);
    }
    printf("Case #%d: %.9lf\n", t+1, res);
  }
  
  return 0;
};
