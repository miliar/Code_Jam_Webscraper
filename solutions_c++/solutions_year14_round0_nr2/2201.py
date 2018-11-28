#include <iostream>

using namespace std;

int main()
{
  int N;
  cin >> N;
  for (int i = 1; i <= N; ++i)
  {
    double C, F, X;
    cin >> C >> F >> X;
    double cp = 2;
    double t = 0;
    while ((X/(cp+F)) < ((X-C)/cp))
    {
      t += C/cp;
      cp += F;
    }
    t += X/cp;
    cout << fixed;
    cout.precision(7);
    cout << "Case #" << i << ": " << t << endl;
  }
  return 0;
}
