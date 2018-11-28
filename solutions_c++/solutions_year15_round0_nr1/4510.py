#define MAXCASES 100
#include "codejam.hh"

struct Audience : CaseBase {
  char nshy[10];
  U maxshy;
  U added;
  void read() {
    maxshy = GETU;
    for(unsigned i = 0, N = maxshy+1; i < N; ++i) {
      int n = GET0;
      if (i < 10) {
        nshy[i] = n;
      }
    }
    amin(maxshy, 9);
  }
  void show() {
    cerr << maxshy << ' ';
    for(unsigned i = 0, N = maxshy+1; i < N; ++i) {
      cerr << (nshy[i] + '0');
    }
  }
  void print() {
    PUTU(added);
  }
  void solve() {
    U standing = 0;
    for(unsigned i = 0, N = maxshy+1; i < N; ++i) {
      // require i to stand
      if (i > standing) {
        added += i - standing;
        standing = i;
      }
      standing += nshy[i];
    }
    assert(standing >= maxshy);
  }
};


CASES_MAIN(Audience)
