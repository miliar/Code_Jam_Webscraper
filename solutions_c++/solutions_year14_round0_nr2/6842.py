#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(int argc, char *argv[]) {

  int T;
  double C, F, X;

  scanf("%d", &T);

  for(int t=1; t<=T; t++) {

    //Read info
    scanf("%lf %lf %lf", &C, &F, &X);

    double cps = 2.0;
    double requiredSeconds = 0.0;

    while( true ) {
      double t0 = X/cps; //Not buy a farm
      double t1 = C/cps + X/(cps+F); //Buy a farm

      if( t0 < t1 ) {
	requiredSeconds += t0; //Add time to finish and break
	break;
      }
      else {
	requiredSeconds += C/cps; //Add time to buy a farm and continue
	cps += F;
      }
    }
    
    printf("Case #%d: %.7f\n", t, requiredSeconds);
  }

  return 0;
}
