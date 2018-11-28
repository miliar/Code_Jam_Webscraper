#include <iostream>
#include <limits>
#include <cmath>
#include <iomanip>
using namespace std;

extern "C" int printf(const char*, ...);

/* C: cost of 1 cookie farm
 * F: cookie/second per farm
 * X: goal # of cookies
 *
 * let z be the # of farms you bough, y be the time it takes
 *   y = sum[x=0,z](C / (2 + x * F)) + X / (2 + z * F)
 * we know the min(z) = 0, max(z) = X / F , we binary search for optimal z
 */

long double eval(long double C, long double F, long double X, int z){
  long double val = 0.0L;
  for (int x = 0; x < z; ++x)
    val += C / (2.L + (long double)x * F);
  val += X / (2.L + (long double)z * F);
  return val;
}

int linZ(long double C, long double F, long double X, int ZMin, int ZMax){
  //search method 1, we add more until no longer optimal
  long double best = numeric_limits<long double>::max();
  int bestz = ZMin;
  for (int z = ZMin; z <= ZMax; ++z){
    long double test = eval(C, F, X, z);
    if (test < best){
      best = test;
      bestz = z;
    } else
      return bestz;
  }
  return bestz;
}

int binZ(long double C, long double F, long double X, int ZMin, int ZMax){
  //search method 2, binary search by slope test
  if (ZMin == ZMax) return ZMin;
  if (ZMin + 1 == ZMax){
    long double ZMinval = eval(C, F, X, ZMin);
    long double ZMaxval= eval(C, F, X, ZMax);
    if (ZMinval < ZMaxval) return ZMin;
    else                   return ZMax;
  }

  int ZMid = (ZMin + ZMax) >> 1;
  long double BZval = eval(C, F, X, ZMid-1);
  long double ZVal = eval(C, F, X, ZMid);
  if (BZval > ZVal)
    return binZ(C, F, X, ZMid, ZMax);
  if (BZval < ZVal)
    return binZ(C, F, X, ZMin, ZMid);
  return ZMid-1;
}

int main(){
  int n; cin >> n;
  for (int i = 1; i <= n; ++i){
    long double C, F, X; cin >> C >> F >> X;

    int z = binZ(C, F, X, 0, ceil(X));
    printf("Case #%d: %.7llf\n", i, eval(C, F, X, z));
  }
}
