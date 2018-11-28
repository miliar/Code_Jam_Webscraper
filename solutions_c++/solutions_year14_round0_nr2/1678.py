#include <iostream>
#include <cstdio>
using namespace std;

void doproblem(int testcase){
  double C, F, X;
  cin >> C >> F >> X;
  double time = X/2.0;
  double current = 0;
  double rate = 2.0;
  while(1){
    current += C/rate;
    rate += F;
    if(current + X/rate < time){
      time = current + X/rate;
    }
    else break;
  }
  printf("Case #%d: %.9f\n", testcase, time);
}

int main(){
  int n;
  cin >> n;
  for(int i=0; i<n; i++){
    doproblem(i+1);
  }
}
