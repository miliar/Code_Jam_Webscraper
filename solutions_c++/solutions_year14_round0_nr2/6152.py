#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	// your code goes here
  int T;
  cin >> T;
  for(int i=1;i<=T;i++){
    double C,F,X;
    cin >> C >> F >> X;
    double max = X / 2.0;
    double min = max;
    double t = 0;
    double v = 2.0;
    double t_total = 0;
    for(int n=1;n<1000000;n++){
      t += C / v;
      v += F;
      t_total = t + X / v;
      min = min > t_total ? t_total : min;
      if(t_total >= max) {
        break;
      }
    }
    printf("Case #%d: %.7lf\n",i,min);
  }
	return 0;
}
