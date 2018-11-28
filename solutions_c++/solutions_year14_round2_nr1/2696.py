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

typedef std::vector<std::string> stringList;
typedef std::vector<I32> I32List;
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

bool solve(const std::string& s1, const std::string& s2, I32& moveCount)
{
  I32 i = 0;
  I32 j = 0;

  while (i < s1.length() && j < s2.length())
  {
    if (s1[i] != s2[j])
    {
      return false;
    }
    else
    {
      I32 ii = i;
      I32 jj = j;

      while (s1[ii] == s1[i])
      {
        ++ii;
      }

      while (s2[jj] == s2[j])
      {
        ++jj;
      }

      moveCount += std::abs((ii - i) - (jj - j));
      i = ii;
      j = jj;
    }
  }

  return true;
}

bool inBounds(const stringList& strList, const I32List& indexList)
{
  for (U32 i = 0; i < strList.size(); ++i)
  {
    if (indexList[i] >= strList[i].size())
    {  
      return false;
    }
  }

  return true;
}

bool keepSolving(const stringList& strList, const I32List& indexList)
{
  for (U32 i = 0; i < strList.size(); ++i)
  {
    if (indexList[i] < strList[i].size())
    {  
      return true;
    }
  }

  return false;
}

bool solve(const stringList& strList, I32& moveCount)
{
  std::vector<I32> indexList(strList.size(), 0);

  while (keepSolving(strList, indexList))
  {
    char currentChar = strList[0][indexList[0]];
    for (U32 i = 1; i < strList.size(); ++i)
    {
      if (currentChar != strList[i][indexList[i]])
      {  
        return false;
      }
    }
  
    I32 minDiff = 100; // max by def
    I32 maxDiff = 0;

    for (U32 i = 0; i < strList.size(); ++i)
    {
      I32 ii = indexList[i];
      while (strList[i][ii] == currentChar && ii < strList[i].size())
      {
        ++ii;
      }
      I32 diff = ii - indexList[i];
      if (diff > maxDiff)
        maxDiff = diff;
      if (diff < minDiff)
        minDiff = diff;

      indexList[i] = ii;
    }
    moveCount += maxDiff - minDiff;
  }

  return true;
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
    I32 strCount;
    read(strCount);
    std::vector<std::string> strList;
    std::string sTmp;
    
    for (I32 s = 0; s < strCount; ++s)
    {
      read(sTmp);
      strList.push_back(sTmp);
    }

    cout << caseToString(c) << " ";

    I32 moveCount = 0;
    if (solve(strList, moveCount))
    {
      cout << moveCount;  
    }
    else
    {
      cout << "Fegla Won";
    }
    cout << endl;
  }
}

