#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

double minorTime(double farmValue, double incFarm, double total)
{
  vector<double> times;
  double inc = 2.0;

  double timeAux = total/inc;

  times.push_back(timeAux);

  double time = 0.0;

  int aux=1;
  
  while(true)
  {
    for(int i=1; i<=aux ; i++)
    {
      time += farmValue/inc;
      inc += incFarm;
    }

    time += total/inc;

    if(time < times[times.size()-1])
    {
      times.push_back(time);
      time = 0.0;
      inc = 2.0;
    }
    else
      break;

    aux++;
  }
  
  return times[times.size()-1];
}

int main()
{
  int n;
  cin >> n;

  for(int i=0; i<n; i++)
  {
    double c, f, x;

    cin >> c >> f >> x;

    double time = minorTime(c, f, x);
    
    cout << "Case #" << i+1 << ": " << setprecision(7) << fixed << time << endl;
  }

  return 0;
}

