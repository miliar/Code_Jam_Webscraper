#include <iostream>
#include <cstdio>
#include <cmath>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;

int main(){
  int n; cin>>n;
  rep(i,n){
    double ans,sum,cps=2.0;
    double C,F,X;
    cin >>C>>F>>X;

    ans = X/cps;
    sum = C/cps;
    cps += F;
    while(sum+X/cps < ans){
      ans = sum+X/cps;
      sum += C/cps;
      cps += F;
    }

    printf("Case #%d: %.7f\n", i+1, ans);
  }
}
