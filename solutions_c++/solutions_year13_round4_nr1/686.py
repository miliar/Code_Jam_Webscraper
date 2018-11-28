#include <cstdio>
#include <map>
#include <vector>
using namespace std;

#define MOD 1000002013LL

int main() {
  long long T;
  scanf("%lld", &T);
  for (long long caseno = 1; caseno <= T; caseno++) {
    long long N, M;
    map<long long,long long> inc;
    long long origsum = 0;
    scanf("%lld%lld", &N, &M);
    for (long long i = 0; i < M; i++) {
      long long o, e, p;
      scanf("%lld%lld%lld", &o, &e, &p);
      inc[o] += p;
      inc[e] -= p;
      long long z = (e-o)*(e-o-1)/2;
      z %= MOD;
      z *= p;
      z %= MOD;
      origsum += z;
      origsum %= MOD;
    }
//    fprintf(stderr, "\norigsum: %lld\n", origsum);

    long long mysum = 0;
    map<long long,long long> current;
    for (typeof(inc.begin()) it = inc.begin(); it != inc.end(); ++it) {
      long long where = it->first, count = it->second;
//      fprintf(stderr, "at %lld: add %lld\n", where, count);
      if (count > 0) {
        current[where] += count;
      }
      if (count < 0) {
        long long exiting = -count;
        while (exiting != 0) {
          long long nearest = current.rbegin()->first;
          long long here = min(exiting, current[nearest]);
//          fprintf(stderr, " %lld are from %lld\n", here, nearest);
          current[nearest] -= here;
          exiting -= here;
          if (current[nearest] == 0) current.erase(nearest);
          long long z = (where-nearest) * (where-nearest-1) / 2;
          z %= MOD;
          z *= here;
          z %= MOD;
          mysum += z;
          mysum %= MOD;
        }
      }
    }
//    fprintf(stderr, "mysum: %lld\n", mysum);

    printf("Case #%lld: %lld\n", caseno, (MOD+MOD+mysum-origsum) % MOD);
  }
}
