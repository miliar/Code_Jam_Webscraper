#include<bits/stdc++.h>
#include<iostream>
using namespace std;

double solve() {
  double C,F,X;
  cin>>C>>F>>X;
  double cur = 2.0;
  double ans = X/cur;
  double sum = 0;
  
  while(true) {
    sum += C/cur;
    cur += F;
    if(ans-(1e-8)<=sum+X/cur) 
      break;
    ans = sum+X/cur;
  }
  return ans;
  
}


int main() {
  int T;
  cin>>T;
  for(int i=0; i<T; i++) {
    double ans = solve();
    cout << "Case #" << i+1 << ": " ;
    printf("%.10lf\n", ans);
  }
  
  return 0;
}
