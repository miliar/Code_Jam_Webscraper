#include <stdio.h>


double calculate (double c, double f, double x){
  double prodSpeed = 2.00;
  double timeLeft;
  double timePurchasing;
  double timeFactory;
  double totalTime = 0.00;
  while (1) {
    timeLeft = x/prodSpeed;
    timePurchasing = c/prodSpeed;
    timeFactory = timePurchasing + x/(prodSpeed + f);
    if (timeFactory < timeLeft){
      prodSpeed += f;
      totalTime += timePurchasing;
    
    } else {
      totalTime += timeLeft;
      break;
    }
  }

  return totalTime;
}


int main()
{
   int t;
   double c,f,x;
   
   scanf("%d",&t);
   for (int i = 1; i <= t; i++){
    scanf("%lf %lf %lf",&c,&f,&x);
    double ans;
    ans = calculate(c,f,x);
    printf("Case #%d: %.7lf\n",i,ans);
   
   };
  

   return 0;
}
