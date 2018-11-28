#include <iostream>
#include <iomanip>
using namespace std;

bool buy_farm (double i, double C, double F, double X)
{
  return (X/i) > ((C/i) + (X/(i + F)));
}


int main ()
{
  unsigned long long int T = 0;
  cin >> T;


  for (unsigned long long int i = 0; i < T; ++i)
  {
    double C, F, X;
    C = F = X = 0.0;

    double x = 2.0; // 2 cookies/sec

    cin >> C;
    cin >> F;
    cin >> X;

    double time = 0.0;

    while (buy_farm (x, C, F, X)) {
      time += C/x;
      x += F;
    }

    time += X/x;

    cout << fixed;
    cout << setprecision (8) << "Case #" << i + 1 << ": " << time << endl;
  }
}

