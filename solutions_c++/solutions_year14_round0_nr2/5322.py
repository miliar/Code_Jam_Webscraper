#include <cstdio>
using namespace std;
void solve(int n){
  double C,F,X,prev = 1e100,m = 0,sum=0;
  scanf("%lf %lf %lf",&C,&F,&X);
  for(m = 0 ; ; m ++){
    double now = sum + X / (m*F + 2.0);
#ifdef DEBUG
    printf("m=%.0f ,now = %.3lf\n",m,now);
#endif
    sum += C / (m*F+2.0);
    if(now > prev){
      break;
    }
    prev = now;
  }
  printf("Case #%d: %.7f\n",n,prev);
  
}
int main(){
  int N ;
  scanf("%d",&N);
  for(int i = 1; i <= N ;i ++ ) solve(i);
}
