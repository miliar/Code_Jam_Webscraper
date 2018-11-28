#include <stdio.h>
#include <set>

typedef long long int ll;

int main(int argc, char** argv) {
  FILE* fin = fopen(argv[1], "r");
  FILE* fout = fopen(argv[2], "w");

  int t;
  ll n;
  fscanf(fin, "%d\n", &t);

  int c = 1;
  while (t--) {
    fscanf(fin, "%lld\n", &n);
    if (n == 0) {
      fprintf(fout, "Case #%d: INSOMNIA\n", c++);
      continue;
    }
    std::set<ll> digits;
    ll i = 0;
    while (digits.size() < 10) {
      i += n;
      // printf("\t%lld:\n", i);
      ll j = i;
      if (j % 10 == 0)
        digits.insert(0);
      while (j > 0) {
        digits.insert(j % 10);
        j /= 10;
      }
      // for (auto it = digits.begin(); it != digits.end(); ++it)
      //   printf("%lld ", *it);
      // printf("\n");
    }
    fprintf(fout, "Case #%d: %lld\n", c++, i);
  }
  return 0;
}
