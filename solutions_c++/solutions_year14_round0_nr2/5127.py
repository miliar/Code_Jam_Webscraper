#include<iostream>
using namespace std;

int main()
{
  int T;
  double C, F, X, P;
  double limit, time;

  cin >> T;
  for(int t = 1; t <= T; t++)
  {
    P = 2.0;
    time = 0.0;
    cout.precision(15);

    cin >> C >> F >> X;
    limit = (F*X)/C - F;
    while(P < limit)
    {
      time += C/P;
      P += F;
    }
    time +=  X/P;

    cout << "Case #" << t << ": " << time << endl;
  }
  return 0;
}
