#include <iostream>
#include <cstdio>

using namespace std;

void solve(int test){
  cout << "Case #" << test << ": ";
  double C, F, X;
  
  scanf("%lf%lf%lf", &C, &F, &X);
  
  double speed = 2;
  double res = 1e9;
  double overall = 0;
  
  for(int i = 0; i < 1e7; ++i){
  //  cout << overall << " " << speed << " " << res << endl;
    res = min(res, X/speed + overall);
    overall += (C/speed);
    speed += F;
  }
  
  printf("%.7f\n", res);
}
int main(){
  int tests;
  cin >> tests;
  
  for(int i = 1; i <= tests; ++i){
    solve(i);
  }
}