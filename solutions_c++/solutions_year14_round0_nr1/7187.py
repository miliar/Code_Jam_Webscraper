#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <queue>

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



/*--------------------------------------------------------------------------------------------------------------------
Main
--------------------------------------------------------------------------------------------------------------------*/
void main()
{
  // redirect cin & cout
  redirectInput("in.txt");
  redirectOutput("out.txt");

  I32 caseCount = initSolver();

  for (I32 i = 0; i < caseCount; ++i)
  {
    I32 row1, row2;
    I32 set1[16], set2[16];

    read(row1);
    for (I32 j = 0; j < 16; ++j)
    {
      read(set1[j]);
    }

    read(row2);
    for (I32 j = 0; j < 16; ++j)
    {
      read(set2[j]);
    }

    I32 card1, card2, res = 0;
    for (I32 j = 0; j < 4; ++j)
    {
      card1 = set1[(row1 - 1) * 4 + j];
      for (I32 k = 0; k < 4; ++k)
      {
        card2 = set2[(row2 - 1) * 4 + k];
        if (card1 == card2)
        {
          if (res == 0)
          {
            res = card1;
          }
          else
          {
            res = -1;
            break;
          }
        }
      }
      if (res == -1)
        break;
    }
    
    cout << caseToString(i) << " ";

    if (res == 0)
      cout << "Volunteer cheated!";
    else if (res == -1)
      cout << "Bad magician!";
    else
      cout << res;
    cout << endl;
  }
}

