#include <algorithm>
#include <cstdio>
using namespace std;
#define REP(i,b) for ( int i = 0; i < int(b); ++i )
#define FOR(i,a,b) for ( int i = int(a); i <= int(b); ++i )

int main( ) {
  int    caseCnt;
  double tim, minsec, c, f, x, cps;
  scanf("%d", &caseCnt);
  FOR( caseNr, 1, caseCnt ) {
    scanf("%lf%lf%lf", &c, &f, &x);
    tim    = 0;
    cps    = 2;
    minsec = x / cps;
    while ( true ) {
      tim += c / cps;
      cps += f;
      if ( tim + x / cps > minsec )
        break;
      minsec = tim + x / cps;
    }
    printf("Case #%d: %.7f\n", caseNr, minsec);
  }
  return 0;
}