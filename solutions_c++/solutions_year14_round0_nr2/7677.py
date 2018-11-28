// CookieClickerAlpha.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"

#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <fstream>


const std::string InputPath = "C:\\CodingJam\\Qualification\\CookieClickerAlpha\\Input\\B-large.in";
const std::string OutputPath = "C:\\CodingJam\\Qualification\\CookieClickerAlpha\\Output\\B-large.out";

class Inputs
{
public:
  friend std::istream& operator>>(std::istream& in, Inputs& input)
  {
    in >> input._farmCost;
    in >> input._farmReturn;
    in >> input._cookieTarget;
    return in;
  }

  double GetFarmCost() const { return _farmCost; }
  double GetFarmReturn() const { return _farmReturn; }
  double GetTarget() const  { return _cookieTarget; }

private:
  double _farmCost;
  double _farmReturn;
  double _cookieTarget;
};

class CookieFactory
{
public:
  ///
  // CookieFactory:
  // Construction yo! 
  CookieFactory(const double initialCookieRate, const Inputs& inputs)
    :_initialCookieRate(initialCookieRate),
     _inputs(inputs)
  {}
  
  ///
  // CalculateDeliveryTime:
  // Calculate the time to deliver the target, including any
  // farm purchases in the middle
  double CalculateDeliveryTime() const
  {
    double perSecond         = _initialCookieRate;
    double perSecondWithFarm = 0.0;    

    double farmCost          = 0.0;
    double target            = 0.0;
    double farmAvailable     = 0.0;
    double timeWithFarm      = 0.0;
    double timeWithoutFarm   = 0.0;

    double timeElapsed       = 0.0;
    while (true)
    {
      farmCost = _inputs.GetFarmCost();
      target   = _inputs.GetTarget();
      
      perSecondWithFarm = perSecond + _inputs.GetFarmReturn();
      farmAvailable     = CalculateTime(farmCost, perSecond,         0.0);
      timeWithFarm      = CalculateTime(target,   perSecondWithFarm, farmAvailable);
      timeWithoutFarm   = CalculateTime(target,   perSecond,         0.0);

      if (timeWithoutFarm <= timeWithFarm)
      {
        return timeElapsed + timeWithoutFarm;
      }
      else 
      {
        timeElapsed += farmAvailable;
        perSecond = perSecondWithFarm;
      }
    }
  }

private:
  
  ///
  // CalculateTime:
  // Simple calculation to calculate the time to reach the supplied 
  // target. This could be the time to buy a factory, or a time to "win"
  // The offset supplied is a little hacky to allow me to specify a starting
  // time... this is so that we can work out the total time to reach the 
  // including the purchase of a farm in the middle
  double CalculateTime(const double target, const double perSecond, const double offset) const
  {
    // perSecond must not be 0.0! "safe" to assume it isn't in here!
    return offset + (target / perSecond);
  }

  double _initialCookieRate;
  Inputs _inputs;
};


///
// ReadInput:
// Reads the input file supplied by Google and converts it into
// the types required to solve the problemo
//
std::vector<Inputs> ReadInput(std::string filename)
{
  std::fstream file(filename, std::ios_base::in);
  
  std::vector<Inputs> inputs;

  int testCases = 0;
  file >> testCases;
  for (int testCase = 0; testCase < testCases; ++testCase)
  {
    Inputs input;
    file >> input;
    inputs.push_back(input);
  }

  return inputs;
}

int main()
{
  std::vector<Inputs> inputs = ReadInput(InputPath);

  std::fstream output(OutputPath, std::ios_base::out);
  int testCase = 1;
  for (auto input : inputs)
  {
    CookieFactory factory(2.0, input);
    output << "Case #" << testCase++ << ": " << std::fixed << std::setprecision(7) << factory.CalculateDeliveryTime() << std::endl;
  }

	return 0;
}

