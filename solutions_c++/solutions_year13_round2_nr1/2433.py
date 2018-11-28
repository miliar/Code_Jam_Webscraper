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

/*-------------------------------------------------------------------------
	Helper functions			
-------------------------------------------------------------------------*/

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

template<typename T> void read(T& value) { cin >> value; cin.get(); }
template <> void read(std::string& s) { getline(cin, s); }

/*-------------------------------------------------------------------------
	Solver application				
-------------------------------------------------------------------------*/

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

bool big(I64 i, I64 j) { return i > j; }

void grow(I64& sum)
{
  sum += sum - 1;
}

void main()
{
  I32 caseCount = initSolver();

  // helpers
  I32 i,j;
  I64 a, n, sum, tmp;
  I64 firstLeftCount, firstLeftCountO;

  vector<I64> v;
  I32 o;

  for (i = 0; i < caseCount; ++i)
  {
    read(a);
    read(n);
    v.assign(n, 0);
    o = 0;
    sum = a;
    firstLeftCount = 0;
    firstLeftCountO = 0;

    for (j = 0;j < n; ++j)
    {
      read(v[j]);
    }

    sort(v.begin(), v.end());

    for (j = 0;j < n; ++j)
    {
      if (sum > v[j])
        sum += v[j];
      else
      {
        if (sum + sum - 1 > v[j])
        {
          sum += sum - 1 + v[j];
          o++;
        }
        else
        {
          I64 leftCount = n - j;

          if (firstLeftCount == 0)
          {
            firstLeftCount = leftCount;
            firstLeftCountO = o;
          }

          I64 tmpS = sum;
          I64 tmpO = 0;

          while (tmpS <= v[j] && tmpO < leftCount)
          {
            tmpS += tmpS -1;
            tmpO ++;
          }

          if (tmpO < leftCount)
          {
            if (o - firstLeftCountO + tmpO > firstLeftCount)
            {
              o = firstLeftCount + firstLeftCountO;
              break;
            }
            else
            {
              sum = tmpS + v[j];
              o += tmpO;
            }
          }
          else
          {
            if (o + leftCount < firstLeftCount + firstLeftCountO)
              o += leftCount;
            else
               o = firstLeftCount + firstLeftCountO;
            break;
          }
        }
      }
    }
  
    cout << caseToString(i) << " " << o << endl; 
  }
}
