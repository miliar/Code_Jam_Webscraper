#include <cstdio>
using namespace std;

int main(){
  int T; scanf("%d",&T);
  
  for(int t = 1; t <= T; ++t){
    double C,F,X;
    scanf("%lf %lf %lf",&C,&F,&X);
    
    double time = 0, f = 2.0;
    
    while(42){
      double ac = C / f + (X / (f + F));
      double finish = X / f;
      
      if(finish < (ac - 10e-9)){
	time += finish;
	printf("Case #%d: %.7lf\n",t, time);
	break;
      }
      
      time += C / f;
      f += F;
    }
  }
}