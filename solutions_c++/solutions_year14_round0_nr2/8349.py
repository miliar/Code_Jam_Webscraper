#include<stdio.h>
#include<stdlib.h>

int number;
double cost, fast, sum;
double speed = 2.0;
double result = 0.0;

void calculate(){
  while(((cost/speed)+(sum/(speed+fast))) < (sum/speed)){    
    result += (cost/speed);
    speed += fast;    
  }
  result += (sum/speed);
}

void run(){
  scanf("%lf", &cost);
  scanf("%lf", &fast);
  scanf("%lf", &sum);
  calculate();
  printf("%.7f", result);
  result = 0.0;
  speed = 2.0;
}

int main(){
  scanf("%d", &number);
  for(int i=1; i<=number; ++i){
    printf("Case #%d: ", i);
    run();
    printf("\n");
  }
  return 0;
}
