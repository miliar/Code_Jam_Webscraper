#include "bits/stdc++.h"
using namespace std;

const int MAXN = 1007;

char S[MAXN];

void solve (int k) {
  int res = 0;
  int N;
  scanf ("%d", &N);
  scanf ("%s", S);
  int tmp = 0;
  for (int i = 0; i <= N; ++i) {
    if (tmp < i) { 
      res += i-tmp;
      tmp = i;
    }
    tmp += S[i] - '0';
  }
  printf ("Case #%d: %d\n", k, res);
}

int main (int argc, const char *argv[]) {
  int q;
  scanf ("%d", &q);
  for (int i = 1; i <= q; ++i) solve (i);
  return 0;
}
