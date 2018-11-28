#include <iostream>
#include <cstdio>

using namespace std;

int main(int argc, char **argv) {
  int cases;
  cin >> cases;
  for(int i = 1; i <= cases; i++) {
    long double C, F, X;
    cin >> C;
    cin >> F;
    cin >> X;

    long double totalTime = 0;
    long double rate = 2;

    long double thisTime;
    long double nextTime;

    while(true) {
      thisTime = X / rate;
      nextTime = (C / rate) + (X / (rate + F));
      if(nextTime < thisTime) {
	totalTime += (C / rate);	
      } else {
	totalTime += (X / rate);
	break;
      }
      rate += F;
    }

    printf("Case #%d: %.7Lf\n", i, totalTime);    

  }
}
