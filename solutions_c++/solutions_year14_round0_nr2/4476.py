#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <cstdlib>
using namespace std;

int main() {
	int T;
	double c,f,x;

	cin >> T;
	for (int i=1; i<=T; i++) {
	  cin >> c;
	  cin >> f;
	  cin >> x;
	  double time = 0.0;
	  double rate = 2.0;
    double buy, notbuy;
  
    while(1) {
      buy = time + c/rate + x/(rate+f);
      notbuy = time + x/rate;
      if (buy > notbuy) {
        time = time + x/rate;
        break;
      }
      time = time + c/rate;
      rate = rate+f;
    }
    
    printf("Case #%d: %.7lf\n", i, time);
  }
		
}

