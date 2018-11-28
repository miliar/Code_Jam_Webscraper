#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    double c, f, x;
    cin >> c >> f >> x;
    
    double rate = 2.0;
    double remain = x;
    double time = 0.0;
    
    while (remain / rate > remain / (rate + f) + (c / rate)) {
      time += c / rate;
      rate += f;
    }
    time += remain / rate;
    cout << "Case #" << i + 1 << ": " << setprecision(7) << fixed << time << endl;
  }
  return 0;
}
