#include<cstdio>
using namespace std;

long double computeSeconds(long double c, long double f, long double x) {
  long double nextXSec = x/2;

  long double nextFSec = c/2;
  long double nextFcps = 2;

  while (nextFSec < nextXSec) {
    long double cps = nextFcps+f;
    long double posNextX = nextFSec + x/cps;
    if (nextXSec > posNextX) {
      nextXSec = posNextX;
    }

    nextFSec = nextFSec + c/cps;
    nextFcps = cps;
  }
  return nextXSec;
}

int main() {
  int zet;
  scanf("%d", &zet);
  int caseNr = 0;
  while (zet--) {
    caseNr++;
    printf("Case #%d: ", caseNr);
    long double c, f, x;
    scanf("%Lf %Lf %Lf", &c, &f, &x);
    printf("%.7Lf\n", computeSeconds(c, f, x));
  }
  return 0;
}
