#include <cstdio>
#include <algorithm>

int main(){
  for(int TT, T = (scanf("%d", &TT), 1); T <= TT; T++){
    printf("Case #%d: ", T);
    double C, F, X;
    scanf("%lf %lf %lf", &C, &F, &X);
    double ratio = 2.0;
    double ans = X / ratio, pre = 0;
    while(1){
      pre += C / ratio;
      ratio += F;
      if(pre + X / ratio >= ans){
        break;
      }
      ans = pre + X / ratio;
    }
    printf("%.7f\n", ans);
  }
  return 0;
}
