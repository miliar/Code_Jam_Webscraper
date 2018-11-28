#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
using namespace std;
#define eps .0000001

double v[100], x[100];
int N;
double V, X;

int equals_d(double a, double b) {
  if(a <= b && a+eps >= b)
    return 1;
  if(b<=a && b+eps >= a)
    return 1;
  return 0;
}

int main() {

  int T;
  scanf("%d", &T); 
  
  for(int i=0; i<T; i++) {
    scanf("%d %lf %lf", &N, &V, &X);
    for(int j=0; j<N; j++) {
      scanf("%lf %lf", &v[j], &x[j]);
      x[j]-=X;
    }
    
    printf("Case #%d: ", i+1);
    if(N==1) {
      if(equals_d(x[0], 0.0))
	printf("%lf\n", V/v[0]);
      else
	printf("IMPOSSIBLE\n");
    }
    else if(N==2) {
      //printf("v0=%lf, v1=%lf, x0=%lf, x1=%lf, V=%lf, X=%lf\n", v[0],v[1],x[0],x[1],V,X);

      double alpha;
      if(equals_d(x[0],0.0) && equals_d(x[1],0.0))
	printf("%lf\n", V/(v[0]+v[1]));
      else if(equals_d(x[0],x[1]))
	printf("IMPOSSIBLE\n");
      else if(equals_d(x[1],0.0))
	printf("%lf\n", V/v[1]);
      else if(equals_d(x[0],0.0))
	printf("%lf\n", V/v[0]);
      else if(x[0]>0.0 && x[1]>0.0)
	printf("IMPOSSIBLE\n");
      else if(x[0]<0.0 && x[1]<0.0)
	printf("IMPOSSIBLE\n");
      else {
	alpha = -v[0]*x[0]/v[1]/x[1];
      //printf("%lf\n", alpha);
      //printf("%lf\n", (1+alpha)*v[0]);

	assert(alpha>0.0);
	
	double rate = (v[0]+alpha*v[1])/max(1.0,alpha);
	//printf("v[0]=%lf, v[1]=%lf, alpha=%lf\n", v[0], v[1], alpha);
	//printf("%lf\n", rate);
	printf("%lf\n", V/rate);
      }
    }
    else {
      
    }
  }

  return 0;

}
