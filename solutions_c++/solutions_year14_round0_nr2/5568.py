#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int test=1; test <= T; test++) {
  	double C, F, X;
  	double Tot = 0.0;
  	double rate = 2.0;
  	double t = 0.0;
  	double t1, t2;
  	
  	cin >> C >> F >> X;
  	while (Tot < X) {
			
			t1 = (X-Tot) / rate;
			t2 = (C / rate) + (X-Tot) / (rate+F);
			
			if (t1 < t2) {
				t += t1;
				Tot = X;
			}
			else {
				t += (C / rate);
				rate += F;	
			}
		}
          
    printf("Case #%d: %0.7f\n" ,test, t);
	}

  return 0;
}
