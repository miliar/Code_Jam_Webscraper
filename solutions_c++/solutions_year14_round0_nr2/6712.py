#include <iostream>
#include <cstdio>

using namespace std;

double calc(double c, double f, double x) {
//cout<<"======================="<<endl;
  double target = x/2.0;
//printf("target %.7lf\n", target);
  double ans, prev=0.0;
  double prevFactor = 0.0;
  int count=0;
  double min = 100001;
  bool down = false;
  int first = 0;
  while( true ) {
    double factor=0.0;
//cout<<"prevans = "<<prev<<endl;
//cout<<"prevfactor = "<<prevFactor<<endl;
    factor += prevFactor + c/(count*f+2);
//cout<<"factor = "<<factor<<endl;
    prevFactor = factor;
    double remaining = x/(2+ f*(count+1));
//cout<<"rem = "<<remaining<<endl;
    ans = remaining + prevFactor;
//printf("ans %.7lf\n", ans);
    count++;
    if (first == 0){
      if( ans < min ){
        min = ans;
        down = true;
        first++;
      }
    } else {
      if( ans < min ){
        down = true;
        min = ans;
      }
      if( down && ans > prev){
        break;
      }
    }

    if( ans >= target)
      break;
    prev = ans;

  }
//cout<<"======================="<<endl;
  if( target < prev )
    return target;
  else
    return prev > 0.0 ? prev: target ;
}

main(){
  int t;
  scanf("%d", &t);
  for(int i=1;i<=t;++i) {
      double c;
      double f;
      double x;
      scanf("%lf %lf %lf", &c, &f, &x);
      printf("Case #%d: %.7lf\n", i, calc(c,f,x));
  }
}

