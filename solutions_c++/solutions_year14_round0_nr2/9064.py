#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
  int t;
  cin >> t;
  
  for (int c = 1; c <= t; c++)
  {
    double farm_cost, farm_rate, goal; //input variables
    double cookie_rate = 2.0, total_time = 0.0;

    cin >> farm_cost >> farm_rate >> goal;
    
    while(1)
    {
      double time_no_farm = goal/cookie_rate;
      
      double time_til_farm = farm_cost/cookie_rate;
      cookie_rate += farm_rate;
      double time_with_farm = goal/cookie_rate + time_til_farm;
     
      if (time_with_farm < time_no_farm)
      {
        total_time += time_til_farm;
      }
      else
      {
        total_time += time_no_farm;
        break;
      }
    }
    cout << "Case #" << c << ": "  
         << fixed << setprecision(7) << total_time
         << endl;
  }
  return 0;
}
