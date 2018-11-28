#include <bits/stdc++.h>
using namespace std;

int main() {
  int T; scanf("%d",&T);
  for (int _t=1; _t<=T; _t++) {
    long long N;
    scanf("%lld",&N);
    if (N == 0) {
      printf("Case #%d: INSOMNIA\n",_t);
    }else {
      bool seen[10]; fill(seen,seen+10,false);
      bool seenAll = false;
      long long origN = N;
      while (!seenAll) {
        long long temp = N;
        if (temp <= 0) {
          printf("ERROR\n");
          exit(-1);
        }
        while (temp > 0) {
          long long dig = temp % 10;
          seen[dig] = true;
          temp = temp / 10;
        }
        int j = 0;
        for (; j<10; j++) if (!seen[j]) break;
        if (j == 10) seenAll = true;
        if (seenAll) {
          printf("Case #%d: %lld\n",_t,N);
          break;
        }else {
          N = N + origN;
        }
      }
    }
  }
  return 0;
}
