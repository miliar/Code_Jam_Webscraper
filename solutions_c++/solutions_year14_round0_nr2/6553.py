#include <iostream>
using namespace std;

int main() {
  std::cout.precision(10);
  int t;
  cin >> t;
  double c,f,x;
  for(int i =1; i<=t;i++)
  {
    double time = 0,rate=2;
    cin >> c;
    cin >> f;
    cin >> x;

    while (x/rate > (c/rate + x/(rate+f)))
    {
      time += c/rate;
      rate += f;
    }
    time += x/rate;
    cout << "Case #" << i << ": " << time << "\n";
  }
}
