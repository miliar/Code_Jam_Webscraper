#include <iostream>
#include <iomanip>      // std::setprecision

using namespace std;

int main ()
{
  int T, i;
  double ptime, C, F, X, Ctime, tick;

  cin >> T;
  for (i = 1; i <= T; ++i)
  {
    cin >> C;
    //cout << "Case #" << i << ": " << fixed << setprecision(7) << C << endl;
    cin >> F;
    //cout << "Case #" << i << ": " << fixed << setprecision(7) << F << endl;
    cin >> X;
    //cout << "Case #" << i << ": " << fixed << setprecision(7) << X << endl;

    tick = 2;
    ptime = X/2;
    Ctime = C/tick;
    tick += F;    
    while(ptime > (X/(tick) + Ctime))
    {
      ptime = X/tick + Ctime;        
      Ctime += C/tick;
      tick += F;  
    }   

    cout.precision(17);
    cout << "Case #" << i << ": " << fixed << setprecision(7) << ptime << endl;      
  }

   
  
  return 0;
}