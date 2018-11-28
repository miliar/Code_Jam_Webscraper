#include <iostream>
#include <vector>
#include <stdio.h>
#include <cmath>
#define rep(i,n) for(int i=0;i<n;i++)
#define repn(i,m,n) for(int i=m;i<n;i++)
using namespace std;
int main(){
  int cases;cin>>cases;
  for(int caseI=1;caseI<=cases;caseI++){
    int M,N,K;
    cin>>M>>N>>K;
    int cnt=0;
    rep(i,M){
      rep(j,N){
        if((i&j)<K){cnt++;}
      }
    }
    printf("Case #%d: %d\n",caseI,cnt);
  }
  return 0;
}
