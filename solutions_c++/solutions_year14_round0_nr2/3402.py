#include<iostream>
#include<fstream>
#include<vector>
#include <iomanip>

using namespace std;

double get_min(double c, double f, double x)
{
  double time = 0;
  double rate = 2;

  double buy_house = 0;
  double dont_buy_house = 1;

  while(buy_house < dont_buy_house)
  {
    // compute
    buy_house = (c/rate) + (x/(rate+f));
    dont_buy_house = (x/rate);
  
    if (buy_house < dont_buy_house)
    {
      time += (c/rate);
      rate += f;
    }
    else
    {
      time += dont_buy_house;
      break;
    }
  }
  return time;
}

int main()
{
  ifstream in_f("B-large.in");
  ofstream of("B-large.out");
  
  int test_cases = 0;
  in_f >> test_cases;

  double c;
  double f;
  double x;

  for(int tc=0; tc<test_cases; tc++)
  {
    // READ
    in_f >> c >> f >> x;
  
    // SOLVE
    double r = get_min(c,f,x);

    of << "Case #" << tc+1 << ": ";
    of << std::fixed << std::setprecision(7) << r;
    of << endl;
  }

  in_f.close();
  of.close();
}
