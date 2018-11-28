#include <iostream>
#include <deque>
#include <vector>
#include <iomanip>
struct gamestate
{
  double cookierate;
  double cookies;
  double time;
  gamestate()
  {
    time = 0;
    cookies = 0;
    cookierate = 2;
  }
  bool isEqual(gamestate* A)
  {
    if (A->cookies == this->cookies && A->cookierate == this->cookierate && A->time == this->time)
      {
	return true;
      }
    return false;
  }
  gamestate(double Cookies, double Cookierate, double Time)
  {
    cookies =  Cookies;
    cookierate = Cookierate;
    time = Time;

  }
  double remainingTime(double MaxCookies)
  {
    double temp = MaxCookies;
    temp -= cookies;
    return time + (temp/cookierate);
  }
  void buyFarm(double FCost, double FRate)
  {
    double temp = FCost;
    temp -= cookies;
    if ( temp <= 0 )
      {
	cookies -= FCost;
	cookierate += FRate;
      }
    time += temp/cookierate;
    cookierate+= FRate;
    return;


  }

    
};
double cookies(double maxCookies, double fCost, double fRate)
{

  gamestate A = gamestate();
  double currentLowest = A.remainingTime(maxCookies);

  while(true)
  {
    if ( A.time >= currentLowest)
      {
	break;
      }
    double temp =  A.remainingTime(maxCookies);
    if ( temp < currentLowest )
      {

	currentLowest = temp;
      }
    A.buyFarm(fCost,fRate);

    

  }
  return currentLowest;

}
int main()
{
  int cases;
  std::cin >> cases;
  std::vector<double> out;
  for (int i = 0; i < cases; ++i)
    {
      double maxCookies;
      double fCost;
      double fRate;
      std::cin >> fCost;
      std::cin >> fRate;
      std::cin >> maxCookies;
      out.push_back(cookies(maxCookies,fCost,fRate));

      


      
    }
  for (unsigned int i = 0; i < out.size(); ++i)
    {

      std::string final = "Case #" + std::to_string(i+1)+": ";
      std::cout << final << std::setprecision(10) << out.at(i) << std::endl; 
    }
  return 0;
}
