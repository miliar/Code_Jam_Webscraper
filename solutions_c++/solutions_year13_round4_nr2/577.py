#include <stdio.h>
#include <assert.h>

#define MIN(a,b) (((a) < (b)) ? (a) : (b))
long long int N, P;
bool x[100];

long long int po (long long int a, long long int b) {
  long long int r = 1;
  for (long long int i = 0; i < b; i++) {
    r *= a;
  }
  return r;
}

long long int baux() {
  for (long long int i = N-1; i >= 0; i--) {
    if (!x[i]) {
      return N-1-i;
    }
  }
  return N;
}

long long int best() {
  long long int l = baux();
  //printf("%d %d\n", l, N-1);
  return MIN(po(2,l+1) - 2,po(2,N)-1);
}

bool all (long long int a, long long int v) {
  for (long long int i = 0; i < a; ++i) {
    if (x[i] != v) {
      return false;
    }
  }
  return true;
}

long long int waux() {
  for (long long int i = N-1; i >= 0; i--) {
    if (x[i]) {
      if (all(i, true)) {
        return i+1;
      } else {
        return i;
      }
    }
  }
  return 0;
}

long long int worst() {
  long long int l = waux();
  return po(2,N) - po(2,N-l);
}

int main (void) {
  int T;
  int scanned = scanf("%d", &T);
  for (int currentcase = 1; currentcase <= T; ++currentcase) {
    scanned = scanf("%lld%lld", &N, &P);
    long long int cp = P-1;
    for (long long int i = 0; i < N; i++) {
      x[i] = cp % 2;
      //printf("%d",x[i]);
      cp /= 2;
    }
    //printf("\n");
    printf("Case #%d: %lld %lld\n", currentcase, best(), worst());
  }
  return 0;
}
