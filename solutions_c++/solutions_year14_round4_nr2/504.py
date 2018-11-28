#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 1010;
const int inf = 1e8;

int dp[MaxN], N, a[MaxN], idx[MaxN];

bool cmpf (int i, int j) {
  return a[i] < a[j];
}

int f (int i) {
  if (i == N) return 0;
  if (dp[i] != -1) return dp[i];

  int j = idx[i];

  int A = 0, B = 0;
  for (int pos = j - 1; pos >= 0; --pos)
    if (a[pos] > a[j])
      ++A;

  for (int pos = j + 1; pos < N; ++pos)
    if (a[pos] > a[j])
      ++B;

  return dp[i] = min(A, B) + f(i + 1);
}

void solve (int tc) {
  memset(dp, -1, sizeof(dp));
  scanf("%d",&N);
  for (int i = 0; i < N; ++i) {
    scanf("%d",&a[i]);
    idx[i] = i;
  }
  sort(idx, idx + N, cmpf);
   
  printf("Case #%d: %d\n",tc,f(0));
}

int main (void) {
  int t;
  scanf("%d",&t);
  for (int c = 1; c <= t; ++c)
    solve(c);
  return 0;
}
