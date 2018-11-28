
#include <iostream>
#include <vector>
#include <sstream>
#include <set>
#include <stdexcept>
#include <fstream>
#include <map>
#include <limits>
#include <math.h>
#include <iomanip>
#include <iomanip>
#include <algorithm>

typedef __int64 int64_t;

using namespace std;

bool IsPalyndrome(int64_t v)
{
	ostringstream ostr;

	ostr << v;
	string res = ostr.str();
	string rev = res;

	reverse(rev.begin(), rev.end());
	return res == rev;
}

string ToString(int64_t v)
{
	ostringstream ostr;

	ostr << v;

	return ostr.str();
}


int64_t ToInt64(string str)
{
	istringstream istr(str);
	int64_t v;

	istr >> v;
	return v;
}

int64_t NextPalyndrome(int64_t v)
{		
	string res = ToString(v);
	size_t s = (res.size() + 1) / 2;
	string firstPartStr = res.substr(0, s);

	int64_t firstPartInc = 0;
	istringstream istr(firstPartStr);
	istr >> firstPartInc;
	++firstPartInc;
	
	string firstPartIncStr = ToString(firstPartInc);
	size_t newSize = res.size();
	string rev = firstPartIncStr;

	if (firstPartStr.size() < firstPartIncStr.size())
	{
		++newSize;
		if (newSize % 2 == 0)
		{
			firstPartIncStr.pop_back();
			rev.pop_back();
		}
	}			
	
	if (newSize % 2 == 1)
		rev.pop_back();
	reverse(rev.begin(), rev.end());
	
	string resultStr = firstPartIncStr + rev;	
	
	return ToInt64(resultStr); 
}

int64_t SafeSolve(int64_t a, int64_t b)
{
	int64_t res = 0;
	for (int64_t i = a; i <= b; ++i)
	{
		int64_t square = sqrt(i);

		if (square * square ==i && IsPalyndrome(i) && IsPalyndrome(square))
			++res;
	}

	return res;
}


set<int64_t> GetFairSquare(int64_t min, int64_t max)
{
	int64_t res = 0;
	set<int64_t> fairSquare;

	for (int64_t i = sqrt(min); i <= sqrt(max) + 1; )
	{
		int64_t root = i * i;
		
		if (root >= min && root <= max && IsPalyndrome(i) && IsPalyndrome(root))
		{
			cout << root << endl;
			fairSquare.insert(root);
		}
			
		i = NextPalyndrome(i);
	}

	return fairSquare;
}


int64_t FastSolve(const set<int64_t>& fairSquare, int64_t a, int64_t b)
{
	int64_t res = 0;

	for (auto v: fairSquare)
	{
		if (v >= a && v <= b)
			++res;
	}

	/*if (res != SafeSolve(a, b))
	{
		throw exception();
	}*/
	return res;
}



int main(int argc, char** argv)
{
	const string inputFilename = "C-large-1.in";
	const string outputFilename = inputFilename + ".out";
	ifstream ifs( inputFilename.c_str() );
	ofstream file( outputFilename.c_str());
	int nbTest = 0;

	ifs >> nbTest;
	string line;
	getline(ifs, line);


	set<int64_t> fairSqure = GetFairSquare(0, 1000000000000000 + 1);

	for( int test = 1; test <= nbTest; ++test )
	{
		ostringstream ostr;
		int64_t a, b;

		ifs >> a >> b;
						
		ostr << "Case #" << test << ": ";
		ostr << FastSolve(fairSqure, a, b);;
		ostr << endl;

		cout << ostr.str();
		file << ostr.str();
	}

	cout << "Finish" << endl;
	return 0;
}



