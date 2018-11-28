#include <iostream>
#include <cstdio>

using namespace std;

int T,t;
long double cps;
long double C,F,X;
long double totalTime, farmTime, nextTotalTime, rTime;

int main(){
  cin >> T;
  t=1;
  while(t <= T){
    cin >> C >> F >> X;
    //cout << C << " " << F << " " << X << endl;
    rTime=0;
    cps = 2;
    farmTime = C/cps;
    nextTotalTime = X/(cps+F);
    totalTime = X/cps;
    while(farmTime + nextTotalTime < totalTime){
      cps += F;
      rTime+=farmTime;
      //cout << cps << " " << C/cps << " " << X/cps <<  endl;
      farmTime = C/cps;
      totalTime = X/cps;
      nextTotalTime = X/(cps+F);
    }
    rTime+=totalTime;

    printf("Case #%d: %.7Lf\n",t,rTime);
    
    t++;
  }  
}
