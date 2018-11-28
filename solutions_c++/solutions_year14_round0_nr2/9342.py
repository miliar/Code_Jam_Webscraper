//cookies.cpp
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <iomanip>
using namespace std;

class CookieMan
{
private:
  //problem parameters
  double winAmt; //how many you need to winAmt
  double farmYield; //extra cookies/sec per farm
  double farmCost; //cost of a farm
  
  double cooks; //current # of cookies
  int numFarms; //current # of farms
  double etime; //how many seconds have passed
public:
  CookieMan(double X, double F, double C) : winAmt(X), farmYield(F), farmCost(C)
  {
    cooks = 0;
    numFarms = 0;
    etime = 0;
  }
  
  double current_rate()
  {
    //# of cookies per second currently produced
    return 2 + numFarms*farmYield;
  }
  
  void wait(double t)
  {
    //accumulate cookies for t seconds
    if (t >= 0)
    {
      etime += t;
      cooks += t*current_rate();
    }
    else {cout << "careful, wait(" << t << ")" << endl;}
  }
  
  void buy_farm()
  {
    //buy a farm if I can
    if (cooks >= farmCost)
    {
      cooks -= farmCost;
      numFarms += 1;
    }
    else
    {
      cout << "careful, can't afford a farm" << endl;
    }
  }
  
  double passive_twin()
  {
    //how long until I win if I just wait
    return (winAmt - cooks)/current_rate();
  }
  
  double elapsed_time()  {return etime;}
  
  double optimal_twin()
  {
    //give the time until I can win using optimal strategy
    
    //first wait until I can afford a farm, if necessary
    while (cooks < farmCost) //should be fine as an if... but it isn't
    {
      double w = (farmCost - cooks)/current_rate();
      wait(w);
    }
    //I can afford a farm now, decision time!
    CookieMan cpy = *this;
    cpy.buy_farm();
    if (passive_twin() <= cpy.passive_twin())
    {
      //we win before we will win buying a farm
      //return how long it took from the start
      return etime + passive_twin();
    }
    else
    {
      //better to buy a farm 
      return cpy.optimal_twin();
    }
  }
  
};

int cookie_testing()
{
  //cookie testing
  CookieMan a(2000, 4.0, 500.0);
  CookieMan prediction(2000, 4.0, 500.0);
  cout << "a.passive_twin(): " << a.passive_twin() << endl;
  cout << "**prediction** optimal_twin(): " << prediction.optimal_twin() << endl;
  a.wait(250);
  CookieMan b = a;
  b.buy_farm();
  cout << "wait 250" << endl;
  cout << "a.passive_twin(): " << a.passive_twin() << endl;
  cout << "b.passive_twin(): " << b.passive_twin() << endl;
  b.wait(83.3333334);
  CookieMan c = b;
  c.buy_farm();
  cout << "wait 83.3333334" << endl;
  cout << "b.passive_twin(): " << b.passive_twin() << endl;
  cout << "c.passive_twin(): " << c.passive_twin() << endl;
  cout << "c.current_rate(): " << c.current_rate() << endl;
  c.wait(50);
  CookieMan d = c;
  d.buy_farm();
  cout << "wait 50" << endl;
  cout << "c.passive_twin(): " << c.passive_twin() << endl;
  cout << "d.passive_twin(): " << d.passive_twin() << endl;
  cout << "d.current_rate(): " << d.current_rate() << endl;
  cout << "d.elapsed_time(): " << d.elapsed_time() << endl;
  d.wait(35.71429);
  CookieMan e = d;
  e.buy_farm();
  cout << "wait 35.71429" << endl;
  cout << "d.passive_twin(): " << d.passive_twin() << endl;
  cout << "e.passive_twin(): " << e.passive_twin() << endl;
  
  
  return 0;
}

int main(int argc, char** args)
{
  if (argc < 2)  {cout << "No arg." << endl; return 1;}

  ifstream infile(args[1], ifstream::in);
  ofstream outfile(strcat(args[1], ".out"), ofstream::out);

  int totalCases;
  infile >> totalCases;
  for (int i=0; i < totalCases; i++)
  {
    outfile << "Case #" << i+1 << ": ";
    double X, F, C;
    infile >> C;
    infile >> F;
    infile >> X;
    CookieMan cooker(X, F, C);
    outfile << setprecision(11) << cooker.optimal_twin();
    outfile << endl;
  }
}