#include <iostream>
#include <string>
#include <iomanip>

using namespace std;
int main()
{
  int T;
  cin >> T;
   
  for (int i = 0; i< T; i++)
    {
    double rate = 2.00000;  
    double C,F,X;
    cin >> C>>F>>X;
    cout<<setprecision(5);

    double result = 0;
    while (true)
      {
      double current = X/rate;
      double next = C/rate + X/(rate+F) ;
      if (current >= next)
        {
        double time = C/rate;

        result += time;
        rate+=F;

      }
      else 
      {
        
        result += current;
        

        break;
      }
      
    }
    cout<< "Case #"<<i+1<<": ";
    cout<<fixed<<setprecision(7)<<result<<"\n";
  }
}
