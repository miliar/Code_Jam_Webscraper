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

struct Edge {
  int a, b, wmin, wmax;
} E[2010];

int A[22][22];
int Way[510];

int main()
{
  int T ,t;
  scanf("%d", &T);
  for (t = 0;t < T; ++t) {
    int N, M, P;
    scanf("%d%d%d", &N, &M, &P);
    for (int i = 0; i < M; ++i) {
      scanf("%d%d%d%d", &E[i].a, &E[i].b, &E[i].wmin, &E[i].wmax);
      --E[i].a;
      --E[i].b;
    }
    for (int i = 0; i < P; ++i) {
      scanf("%d", &Way[i]);
      --Way[i];
    }


    CLEAR(A, -1);
    int res = 0;
    for (int mask = 0; mask < (1<<M); ++mask) {
      CLEAR(A, -1);
      for (int i = 0; i < M; ++i) {
	int w;
	if (mask & (1<<i))
	  w = E[i].wmin;
	else
	  w = E[i].wmax;
	if (A[E[i].a][E[i].b] == -1 || A[E[i].a][E[i].b] > w)
	  A[E[i].a][E[i].b] = w;
      }
      for (int i = 0; i < N; ++i)
	A[i][i] = 0;
      for (int k = 0; k < N; ++k)
	for (int i = 0; i < N; ++i)
	  if (A[i][k] != -1)
	    for (int j = 0; j < N; ++j)
	      if (A[k][j] != -1) {
		if (A[i][j] == -1 || A[i][j] > A[i][k] + A[k][j])
		  A[i][j] = A[i][k] + A[k][j];
	      }

      int sum = 0;
      int cr = P;
      for (int i = 0; i < P; ++i) {
	int ei = Way[i];
	if (mask & (1<<ei))
	  sum += E[ei].wmin;
	else
	  sum += E[ei].wmax;
	if (sum + A[E[ei].b][1] > A[0][1]) {
	  cr = i;
	  break;
	}
      }
      res = max(res, cr);
    }

    if (res == P)
      printf("Case #%d: Looks Good To Me\n", t+1);
    else
      printf("Case #%d: %d\n", t+1, Way[res]+1);
    fprintf(stderr, "Case #%d\n", t+1);

  }

  return 0;
};
