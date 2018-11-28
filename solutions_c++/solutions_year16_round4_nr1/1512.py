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

int N, R, P, S;
int N2;

void parse() {
  scanf("%d%d%d%d", &N, &R, &P, &S);
  N2 = 1 << N;
}

char pfc(char l, char r) {
  if(l == 0 || r == 0 || l == r)
    return 0;
  if(l == 'R' && r == 'S')
    return 'R';
  if(r == 'R' && l == 'S')
    return 'R';
  if(l == 'S' && r == 'P')
    return 'S';
  if(r == 'S' && l == 'P')
    return 'S';
  return 'P';
}

char comp(int n, char* w) {
  if(n == 0)
    return w[0];
  else {
    char l = comp(n-1, w);
    char r = comp(n-1, w+(1<<(n-1)));
    return pfc(l, r);
  }
}

/* brute force */
void solve() {
  char w[N2+1];
  w[N2] = '\0';
  for(int i = 0; i < P; i++)
    w[i] = 'P';
  for(int i = 0; i < R; i++)
    w[P+i] = 'R';
  for(int i = 0; i < S; i++)
    w[P+R+i] = 'S';
  sort(w, w+N2);
  do {
    if(comp(N, w)) {
      printf("%s", w);
      return;
    }
  } while(next_permutation(w, w+N2));
  printf("IMPOSSIBLE");
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
