#include <iostream>
#include <iomanip>
#include <array>
#include <string>
#include <algorithm>
using namespace std;

int main(){
  int T; cin >> T;
  for(int t=1;t<=T;++t) {
    double C,F,X,cps=2.0,time=0.0,total=0.0;
    cin >> C >> F >> X;
    while(true) {
      //if(total+C > X) break;
      if(X/cps < C/cps + X/(cps + F)) break;
      total += C;
      time += C/cps;
      cps += F;
    }
    time += X/cps;
    cout << "Case #" << t << ": ";
    cout << fixed << setprecision(7) <<  time;
    cout << endl;
  }
  return 0;
}
