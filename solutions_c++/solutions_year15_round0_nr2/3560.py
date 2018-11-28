#include "bits/stdc++.h"
using namespace std;

const int MAXN = 1007;

int T[MAXN];
int N;

int ok (int k) {
  int res = 0;
  for (int i = 0; i < N; ++i) 
      res += (T[i]+k-1)/k - 1;
  return res + k;
}

void solve (int nr) {
  int res;
  int D = 0; // max number of pancakes in house
  scanf ("%d", &N);
  for (int i = 0; i < N; ++i) {
    scanf ("%d", &T[i]);
    D = max (D, T[i]);
  }
  res = D;
  for (int i = 1; i < D; ++i) res = min (res, ok (i));
  printf ("Case #%d: %d\n", nr, res);
}


int main (int argc, const char *argv[]) {
  int q;
  scanf ("%d", &q);
  for (int i = 1; i <= q; ++i) solve (i);
  return 0;
}
