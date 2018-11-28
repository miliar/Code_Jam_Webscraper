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

int A[1010];

int main()
{
  int T, t;
  scanf("%d", &T);
  for ( t= 0 ; t < T; ++t) {
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i)
      scanf("%d", &A[i]);

    int res = 0;
    for (int i = 0; i < N-1; ++i) {
      int mp = -1;
      int pmp = 0;
      for (int j = 0, p = 0; j < N; ++j) {
	if (A[j] == -1)
	  continue;
	if (mp == -1 || A[j] < A[mp]) {
	  mp = j;
	  pmp = p;
	}
	p++;
      }

      res += min(pmp, N-i - 1 - pmp);
      A[mp] = -1;
    }

    printf("Case #%d: %d\n", t+1, res);
  }

  return 0;
};
