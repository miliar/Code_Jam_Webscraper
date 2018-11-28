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

Int Wins(Int N, Int P) {
  --P;
  int KL = 0;
  Int b = (1LL << (N-1));
  while ((b & P) && b > 0) {
    ++KL;
    b >>= 1;
  }
  Int res = (1LL << (KL+1)) - 2;
  return res;
}

int main()
{
  int T, t;
  scanf("%d", &T);
  for (t = 0; t < T; ++t) {
    Int N, P;
    scanf("%lld%lld", &N, &P);
    Int x = Wins(N, P);
    Int y = (1LL<<N)-1 - Wins(N, (1LL<<N)-P) - 1;
    if (P == (1LL << N))
      x = y = (1LL << N) - 1;
    printf("Case #%d: %lld %lld\n", t+1, x, y);
  }

  return 0;
};
