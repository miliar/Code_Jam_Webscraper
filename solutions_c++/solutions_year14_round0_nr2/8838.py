#include <iostream>
#include <iomanip>

using namespace std;
int main() {
  std::cout.precision(7);

  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    double C, F, X;
    cin >> C >> F >> X;

    double inc = 2;
    double time = X / inc;
    double farmTime = 0;

    while (true) {
      double nextFarmTime = farmTime + C/inc + X/(F+inc);
      if (time < nextFarmTime)
        break;
      else {
        farmTime += C / inc;
        inc += F;
        time = nextFarmTime;
      }
    
    }
  
    cout << std::fixed << "Case #" << t << ": " << time << endl;
  }


}
