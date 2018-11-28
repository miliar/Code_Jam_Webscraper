#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
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



void main()
{
	I32 caseCount = initSolver();

	// helpers
	I32 i,j;
	I64 r, t;
  I64 c;

	for (i = 0; i < caseCount; ++i)
	{
		read(r);
    read(t);
			
    c = 0;

    while (t >= 0)
    {
      t -= ((r + 1) * (r + 1) - r * r);
      c++;
      r+=2;
    }
    c--;
		cout << caseToString(i) << " " << c << endl; 
	}
}
