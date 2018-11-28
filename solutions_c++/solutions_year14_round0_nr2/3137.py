#include<iostream>
#include<cstdio>
using namespace std;

int main() {
  int T,t;
  double C,F,X,N,n,r;
  cin >> T;
  t = 0;
  while(t++<T) {
    cin >> C >> F >> X;
    if (X <= C) {
      printf("Case #%d: %.7lf\n", t, X/2);
    } else {
      r = 0;
      for (int i=0; 1; i++) {
	double buy, nobuy;
	buy = C/(2+i*F)+X/(2+F+i*F);
	nobuy = X/(2+i*F);
	if (nobuy < buy) {
	  r+=nobuy;
	  printf("Case #%d: %.7lf\n", t, r);
	  break;
	} else {
	  r+=C/(2+i*F);
	}
      }
    }
  }
}
