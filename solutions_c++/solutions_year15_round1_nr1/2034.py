#define MAXCASES 100
#define MAXN 10000
#include "codejam.hh"

struct Plate : CaseBase {
  static void init() {}
  U N;
  I m[MAXN + 1];
  U minany;
  U minsteady;

  void read() {
    N = GETU;
    REP(i, N) m[i] = GETI;
  }
  void show1() {
    cerr << N << ':';
    REP(i, N) cerr << ' ' << m[i];
  }
  void print() {
    cout << minany << ' ' << minsteady;
    verbose = 0;
  }
  void solve() {
    U overall = m[N - 1] - m[0];
    U needrate = 0;
    U nneg = 0;
    REP(i, N - 1) {
      I d = m[i + 1] - m[i];
      if (d < 0) {
        ++nneg;
        amax(needrate, -d);
        minany += -d;
      }
    }
    minsteady = (N - 1) * needrate;
    REP(i, N - 1) {
      if (m[i] < needrate) minsteady -= (needrate - m[i]);
    }
  }
};

CASES_MAIN(Plate)
