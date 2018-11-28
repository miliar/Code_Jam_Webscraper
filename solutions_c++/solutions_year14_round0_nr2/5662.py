#include <iostream>
#include <list>
#include <memory.h>
#include <iomanip>

using namespace std;

  double total_time(double c, double f, double x)
  {

    double t_f = ((x - c)*f-2*c)/(c*f);
    //cout << "max farm" << t_f << endl;

    double t = 0;
    int i = 0;
    for(i  = 0; i < t_f; i++) {
      t += c/(2+i*f);
      //cout << t<<","<<i << endl;
    }

    return t + x/((i*f)+2);
    
  };

int main()
{
  //double c=500,f=4,x=2000;

  int T;

  cin >> T;

  for(int cc = 1; cc <= T; cc++)
    {
      double c,f,x;
      cin >> c >> f >> x;

      cout << setprecision(7) << fixed << "Case #" << cc << ": " << total_time(c,f,x) << endl;
    }
  
  return 0;
}
