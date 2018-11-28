#include<iostream>
#include<cstdio>
using namespace std;
#define STARTER 2
/*
83.3+50+142
83.3+300
*/
double get(double C, double F, double X);
int main() {
  int T;
  double C,F,X;
  cin >> T;
  for ( int i=0; i<T; i++) {
      cin >>C>>F>>X;
      printf("Case #%i: %.7f\n",i+1, get(C,F,X));
  }
}

double get(double C, double F, double X) {
   double f=STARTER;
   double passed = 0;
   //timeToBuyNext = C/f;
   while( X/f >  C/f + X/(f+F)) {
    passed += C/f;

    //cout << passed<<","<<f<<" ";
    //updation
    f+= F;
   }
   //not BuyThisTime
   passed += X/f;
   return passed;
}
