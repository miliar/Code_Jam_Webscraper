#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<long long> v, cv;

main() {
  int T, prob=1;
  for (cin >> T; T--;) {
    long long N, p, q, r, s;
    cin >> N >> p >> q >> r >> s;
    v.resize(N);
    for (int i = 0; i < N; i++) v[i] = ((long long)i*p + q) % r + s;
    cv.resize(N+1);
    cv[0] = 0;
    for (int i = 0; i < N; i++) cv[i+1] = cv[i] + v[i];

    long long ret = 1000000000000000000LL;
    for (int i = 0, j = 0; j < N; j++) {
      long long r3 = cv[N]-cv[j+1];
      if (i > 0) i--;
      for(;;) {
        long long r1 = cv[i]-cv[0];
        long long r2 = cv[j+1]-cv[i];
        ret = min(ret, max(r1, max(r2, r3)));
        if (r1 > r2) break;
        i++;
      }
    }
    printf("Case #%d: %.10lf\n", prob++, (double)(cv[N]-ret)/cv[N]);
  }
}
