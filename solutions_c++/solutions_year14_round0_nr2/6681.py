#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int main(){
  int T,t=0;
  double C,F,X;
  double tol = 0.0000001;
  scanf("%d", &T);  
  double a[100000];
  while(t++<T){
    scanf("%lf %lf %lf", &C, &F, &X);  
    a[0]=X/2;
    int i=1;
    while(a[i-1]-a[0]<tol && i<100000){
      a[i] = a[i-1] - X/( (i-1)*F + 2 ) + X/( i*F + 2 ) + C/( (i-1)*F + 2 );    
      i++;
    }
    double min = a[0];
    for(int j=1; j<i; j++){
      if(min>a[j]) min = a[j];
    }
    printf("Case #%d: %.7lf\n",t,min);
  }
}