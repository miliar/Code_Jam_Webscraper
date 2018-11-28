#include <iostream>
using namespace std;
int main() {
  int T,t;
  cin >> T;
  for(t=1;t<=T;t++){
    double C,F,X,rate=2.0;
    double wait;
    double total_farm = 0.0; // total farm cost so far
    cin >> C >> F >> X;
    wait = X / 2.0;
    //cout << "C " << C << " F " << F << " X " << X << endl;

    while(true) {
      //cout << "rate:" << rate << " total_farm: " << total_farm << " wait: " << wait << endl;
      total_farm += C/rate; // buy a farm
      rate += F;
      double _wait = total_farm + X/rate; // how much total wait if we don't buy any more farm
      if(_wait > wait) break; // stop, wait is the min
      wait = _wait;
    }

    cout << "Case #" << t << ": ";
    printf("%.7f\n", wait);
  }
}