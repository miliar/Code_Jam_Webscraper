#include <cstdint>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <math.h>
#include <algorithm>
#include <numeric>

using namespace std;

/*-------------------------------------------------------------------------
Typedefs
-------------------------------------------------------------------------*/

typedef int8_t I8;
typedef uint8_t U8;
typedef int16_t I16;
typedef uint16_t U16;
typedef int32_t I32;
typedef uint32_t U32;
typedef int64_t I64;
typedef uint64_t U64;
typedef float F32;
typedef double D64;
typedef std::vector<std::string> stringList;
typedef std::vector<I32> I32List;
typedef std::vector<U32> U32List;
typedef std::vector<U64> U64List;

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
void read(T& value) { cin >> value; cin.get(); }

void readLine(std::string& s) { getline(cin, s); }

/*--------------------------------------------------------------------------------------------------------------------
Solver helper functions
--------------------------------------------------------------------------------------------------------------------*/

string caseToString(I32 i)
{
  ostringstream oss;
  oss << "Case #" << (i + 1) << ": ";
  return oss.str();
}

/*--------------------------------------------------------------------------------------------------------------------
Solver
--------------------------------------------------------------------------------------------------------------------*/

/*--------------------------------------------------------------------------------------------------------------------
Main - int main() {} // the minimal C++ program
--------------------------------------------------------------------------------------------------------------------*/

int main()
{
  redirectInput("in.txt");
  redirectOutput("out.txt");

  U32 caseCount;
  read(caseCount);

  U32 s, f, n;
  string ppl;
  for (U32 c = 0; c < caseCount; ++c)
  {
    read(s);
    read(ppl);
   
    f = n = 0;
    for (U32 i = 0; i < ppl.length(); ++i)
    {
      if (n < i)
      {
        ++f;
        ++n;
      }
      if (ppl[i] != '0')
      {     
        n += (U32)(ppl[i] - '0');
      }
    }
    cout << caseToString(c) << f << endl;
  }
}
