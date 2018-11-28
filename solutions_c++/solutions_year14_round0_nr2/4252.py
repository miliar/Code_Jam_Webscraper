#include<cstdio>

#define REP(i,n) for(int i=0;i<(n);i++)

int T;
double C,F,X;
int K;
double sum;
double newsum;

int main(){
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    scanf("%lf %lf %lf",&C, &F, &X);
    sum = 0.0;
    newsum = C/2.0;
    K = 0;
    while(newsum + X/(2+(K+1)*F) < sum + X/(2+K*F)){
      K++;
      sum = newsum;
      newsum += C/(2+K*F);
    }
    printf("Case #%d: %.7lf\n", t, sum + X/(2+K*F));
  }
  return 0;
}
