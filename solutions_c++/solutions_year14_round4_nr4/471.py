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

string S[10];
char buf[100];
int M, N;
int mr, cr;
int P[10];

#define MOD 1000000007

int rest(int a, int b) {
  int i = 0;
  while (i < S[a].size() && i < S[b].size() && S[a][i] == S[b][i])
    ++i;
  return S[b].size() - i;
}

void F(int i, int r) {
  if (i == M) {
    for (int j = 0; j < N; ++j)
      if (P[j] == -1)
	return;
    if (r == mr) {
      cr++;
      if (cr == MOD)
	cr = 0;
    }
    if (r > mr) {
      mr = r;
      cr = 1;
    }
    return;
  }
  for (int j = 0; j < N; ++j) {
    int cr = r;
    int ppj = P[j];
    if (P[j] == -1) {
      cr += S[i].size();
    } else {
      cr += rest(P[j], i);
    }
    P[j] = i;
    F(i+1, cr);
    P[j] = ppj;
  }
}

int main()
{
  int t, T;
  scanf("%d", &T);
  for (t = 0; t < T; ++t) {
    scanf("%d%d", &M, &N);
    for (int i = 0; i < M; ++i) {
      scanf("%s", buf);
      S[i] = buf;
    }
    sort(S, S+M);
    CLEAR(P, -1);
    mr = -1;
    F(0, N);

    printf("Case #%d: %d %d\n", t+1, mr, cr);
  }

  return 0;
};
