#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>

using namespace std;

/*-------------------------------------------------------------------------
	Typedefs			
-------------------------------------------------------------------------*/

typedef __int8 I8;
typedef unsigned __int8 U8;

typedef __int16 I16;
typedef unsigned __int16 U16;

typedef __int32 I32;
typedef unsigned __int32 U32;

typedef __int64 I64;
typedef unsigned __int64 U64;

typedef float F32;
typedef double D64;

/*--------------------------------------------------------------------------------------------------------------------
Helper functions
--------------------------------------------------------------------------------------------------------------------*/

void redirectInput(const std::string& fileName)
{
	static ifstream fi(fileName, std::ios_base::in);
	std::cin.rdbuf(fi.rdbuf());
}

void redirectOutput(const std::string& fileName)
{
	static ofstream fo(fileName, std::ios_base::out);
	std::cout.rdbuf(fo.rdbuf());
}

template<typename T>
void read(T& value)
{ 
  cin >> value; cin.get();
}

template <>
void read(std::string& s)
{
  getline(cin, s);
}

/*--------------------------------------------------------------------------------------------------------------------
Solver helper functions
--------------------------------------------------------------------------------------------------------------------*/

I32 initSolver()
{
  // redirect cin & cout
  redirectInput("in.txt");
  redirectOutput("out.txt");

  // read case count
  I32 caseCount;
  read(caseCount);

  return caseCount;
}

string caseToString(I32 i)
{
  ostringstream oss;
  oss << "Case #" << (i + 1) << ":";
  return oss.str();
}

/*--------------------------------------------------------------------------------------------------------------------
Solver functions
--------------------------------------------------------------------------------------------------------------------*/

D64 timeFarm(D64 farmCost, D64& rate, D64 farmBonus)
{
  D64 farmTime = farmCost / rate;
  rate += farmBonus;

  return farmTime;
}

D64 timeGoal(D64 goalCost, D64 rate)
{
  return goalCost / rate;
}

/*--------------------------------------------------------------------------------------------------------------------
Main
--------------------------------------------------------------------------------------------------------------------*/
void main()
{
  // redirect cin & cout
  redirectInput("in.txt");
  redirectOutput("out.txt");

  I32 caseCount = initSolver();

  for (I32 c = 0; c < caseCount; ++c)
  {
    D64 farmCost, farmBonus, goalCost, rate, goalTime, farmTime, tempTime;
    read(farmCost);
    read(farmBonus);
    read(goalCost);
    rate = 2;

    goalTime = timeGoal(goalCost, rate);
    farmTime = 0;
    tempTime = 0;
    while (tempTime < goalTime)
    {
      farmTime += timeFarm(farmCost, rate, farmBonus);
      tempTime = timeGoal(goalCost, rate) + farmTime;

      if (tempTime < goalTime)
      {
        goalTime = tempTime;
        tempTime = 0;
      }
    }

    cout << caseToString(c) << " " << std::setprecision(15) << goalTime << endl;
  }
}

