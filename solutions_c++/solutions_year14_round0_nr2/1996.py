#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main () {
  //ifstream in("pb.in");
  //ofstream out("pb.out");
  cout.setf(ios::fixed);
  cout.precision(7);
  double C, F, X; 
  int T, t = 1;
  cin >> T;
  double res, buy, not_buy, rate;
  while (t <= T) {
    res = 0;
    not_buy = buy = 0;
    rate = 2;
    cin >> C >> F >> X;
    
    not_buy = X / rate;
    buy = C / rate + X / (rate + F);
    while (not_buy > buy) {
      res += C / rate;
      rate += F;
      not_buy = X / rate;
      buy = C / rate + X / (rate + F);
    }
    res += X / rate;
    cout << "Case #" << t << ": " << setprecision(7) << res;
    if (t != T) cout << "\n";
    t++;
  }
  //in.close();
  //out.close();
}


