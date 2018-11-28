#include <algorithm>
#include <iterator>
#include <iostream>
#include <iomanip>
#include <utility>
#include <string>
#include <vector>

using namespace std;

int main()
{
  int t;
  
  cin >> t;
  
  for(int test = 1; test <= t; test++)
  {
    double C, F, X;
    
    cin >> C >> F >> X;
    
    double prev_get_farm_time = 0.0;
    double prev_speed = 2.0;
    double best_ans = X / prev_speed;
    
    for(int k = 1; ; k++)
    {
      double get_new_farm_time = C / prev_speed;
      prev_get_farm_time += get_new_farm_time;
      prev_speed += F;
      double new_time = X / prev_speed + prev_get_farm_time;
      
      if( new_time < best_ans )
        best_ans = new_time;
      else
        break;
    }
    
    cout << "Case #" << test << ": " << setprecision(7) << fixed << best_ans << endl;
  }
  
	return 0;
}
