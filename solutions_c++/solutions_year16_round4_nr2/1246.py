// solution by Olivier Marty

//#define ONLINE_JUDGE
#include <bits/stdc++.h>
#define fin(i, n) for(int i = 0; i < n; i++)
#define fin2(i, a, b) for(int i = a; i < b; i++)
#define pb push_back
#define mp make_pair
using namespace std;

#ifndef ONLINE_JUDGE
  #define debug(a) cerr << #a << " = " << (a) << endl
#else
  #define debug(a)
#endif

int N, K;
double P[201];
double R[201];

void parse() {
  scanf("%d%d", &N, &K);
  for(int i = 0; i < N; i++) {
    scanf("%lf", P+i);
  }
}

double prob(int i, int k) {
  if(i == K && k == 0)
    return 1.;
  if(i == K)
    return 0.;
  return R[i] * prob(i+1, k-1) + (1.-R[i]) * prob(i+1, k);
}

void solve() {
  int perm[201];
  memset(perm, 0, sizeof(perm));
  for(int i = N-K; i < N; i++)
    perm[i] = 1;
  double m = 0.;
  do {
    int j = 0;
    for(int i = 0; i < N; i++) {
      if(perm[i]) {
        R[j] = P[i];
        j++;
      }
    }
    m = max(m, prob(0, K/2));
  } while(next_permutation(perm, perm+N));

  /*sort(P, P+N);
  for(int i = 0; i < K/2; i++) {
    R[i] = P[i];
    R[K-1-i] = P[N-1-i];
  }
  printf("%.7lf", prob(0, K/2));*/
  printf("%.7lf", m);
}

int main() {
  ios::sync_with_stdio(false);
  int T;
  scanf("%d", &T);
  for(int i = 1; i <= T; i++) {
    parse();
    printf("Case #%d: ", i);
    solve();
    printf("\n");
    #ifdef DEBUG
		  fprintf(stderr, "%d / %d = %.2fs | %.2fs\n", i, T, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / i * T) / CLOCKS_PER_SEC);
    #endif
  }
  return 0;
}
